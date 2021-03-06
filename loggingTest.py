import logging
from datetime import datetime

# to_day = datetime.now()
# log_file_path = "test_{}_{}_{}.log".format(to_day.year, to_day.month, to_day.day)

# logging.basicConfig(
#     level=logging.WARNING,
#     filename=log_file_path,
#     format='%(asctime)s %(filename)s [line:%(lineno)d] %(levelname)s : %(message)s',
#     # datefmt='%a, %d %b %Y %H:%M:%s'  #修改日期格式
# )
# logger = logging.getLogger(__name__)

# if __name__ == '__main__':
#     logger.warning("this is a fun1 waring")



#其他文件使用日志
# from logginTest import logger
# logger.warning("111111111")

import logging
from datetime import datetime
import os

to_day = datetime.now()
logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

f_handler = logging.FileHandler(
    os.getcwd() + "/logFiles/twitter_{}_{}_{}.log".format(
        to_day.year, to_day.month, to_day.day),
    encoding="utf-8")
f_handler.setLevel(logging.DEBUG)
f_handler.setFormatter(
    logging.Formatter(
        "%(asctime)s - %(levelname)s - %(filename)s[:%(lineno)d] - %(message)s"
    ))

st_handler = logging.StreamHandler()
st_handler.setLevel(logging.DEBUG)
st_handler.setFormatter(
    logging.Formatter(
        "%(asctime)s - %(levelname)s - %(filename)s[:%(lineno)d] - %(message)s"
    ))

logger.addHandler(f_handler)
logger.addHandler(st_handler)