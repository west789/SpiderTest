#导入相关包
from initConfig import init
from saveData import TwitterPip
from tweetInfo import getTweetsUser

#主函数
def main():
    api = init()

    #实例化对象
    twitterPip = TwitterPip()

    #获取Tweeter账号信息
    getTweetsUser(api, "HBO", twitterPip)


if __name__ == '__main__':
    main()