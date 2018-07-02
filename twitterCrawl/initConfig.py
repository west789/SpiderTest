#import configparser
import tweepy
import json

# def initKey():
#     #加载config文件
#     cf = configparser.ConfigParser()
#     cf.read("twitterCrawl/config.txt")
#     consumer_key = cf.get("API", "consumer_key")
#     consumer_secret = cf.get("API", "consumer_secret")
#     access_token = cf.get("API", "access_token")
#     access_token_secret = cf.get("API", "access_token_secret")

#     #提交KEY和SECRET
#     auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
#     auth.set_access_token(access_token, access_token_secret)

#     #获取api对象
#     api = tweepy.API(auth, wait_on_rate_limit=True)
#     return api

def init():
    with open("twitterCrawl/config.json", 'r') as f:
        data = json.load(f)
    consumer_key = data.get("consumer_key")
    consumer_secret = data.get("consumer_secret")
    access_token = data.get("access_token")
    access_token_secret = data.get("access_token_secret")
    #提交KEY和SECRET
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)

    #获取api对象
    api = tweepy.API(auth, wait_on_rate_limit=True)
    return api

# if __name__ == "__main__":
#     init()