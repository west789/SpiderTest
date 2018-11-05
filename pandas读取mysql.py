import pandas as pd
from sqlalchemy import create_engine

def matchCol(colName):
    return lambda x: x.endswith(colName) and 'total' not in x

def matchBankCol(colName):
    return 'diebank' in colName


def simplyLatestMain():
    # 1.创建数据库连接,pandas读取数据库表
    # MySQL的用户：root, 密码:147369, 端口：3306,数据库：mydb
    try:
        engine = create_engine('mysql+pymysql://root:123qwe@10.209.152.109:3306/reportdata')
        selSql = 'select * from latestReport'
        latestDf = pd.read_sql_query(selSql, engine)
        # 2.新建一个df表
        newLatestDf = pd.DataFrame(columns=['wait', 'run', 'hold', 'fg', 'ship', 'bank'])
        # 3.循环这个latestdf表，再循环列字段，将含有wait,run,hold,fg,ship,bank,kgd_bank等放入对应字段列下
        latestCols = latestDf.columns
        waitCols = list(filter(matchCol('wait'), latestCols))
        runCols = list(filter(matchCol('run'), latestCols))
        holdCols = list(filter(matchCol('hold'), latestCols))
        fgCols = list(filter(matchCol('fg'), latestCols))
        shipCols = list(filter(matchCol('ship'), latestCols))
        bankCols = list(filter(matchBankCol, latestCols))
        for i in range(0, len(latestDf)):
            waitNum = latestDf.loc[i, waitCols].sum()
            runNum = latestDf.loc[i, runCols].sum()
            holdNum = latestDf.loc[i, holdCols].sum()
            fgNum = latestDf.loc[i, fgCols].sum()
            shipNum = latestDf.loc[i, shipCols].sum()
            bankNum = latestDf.loc[i, bankCols].sum()
            newLatestDf.loc[i] = [waitNum, runNum, holdNum,
                                  fgNum, shipNum, bankNum]
        
        # print(newLatestDf)

        # 4.导出excel表
        newLatestDf.insert(0, 'product_family', latestDf['product_family'])
        newLatestDf.insert(1, 'full_part_number', latestDf['full_part_number'])
        newLatestDf.insert(2, 'item', latestDf['item'])
        newLatestDf['gross_die'] = latestDf['gross_die']
        newLatestDf['yield_cp'] = latestDf['yield_cp']
        newLatestDf['yield_assy'] = latestDf['yield_assy']
        newLatestDf['yield_mt'] = latestDf['yield_mt']
        newLatestDf['yield_ft'] = latestDf['yield_ft']
        newLatestDf['kgd_bank'] = latestDf['kgd_bank']
        newLatestDf.insert(3, 'vendor', latestDf['vendor'])
        newLatestDf.insert(4, 'phase', latestDf['phase'])
        newLatestDf['report_date'] = latestDf['report_date']
        connection = engine.raw_connection()
        try:
            cursor = connection.cursor()
            cursor.callproc("delete_simplyLatest", args=())
            cursor.close()
            connection.commit()
        finally:
            connection.close()
        newLatestDf.to_sql('simplyLatest', engine,index=False)
    except Exception:
        raise

if __name__ == '__main__':

    simplyLatestMain()