#导入tweepy  
import tweepy  
from saveData import TwitterPip
import re

#填写twitter提供的开发Key和secret  
consumer_key = '8Iy4wqdi99Zte6xwmFg0Z7ub6'  
consumer_secret = 'owskEyssBY0u4v47gHa3WZrV0eY66XorNkrJ9FKYV0WvJOJSm7'  
access_token = '1715166764-EiOl7SStz5Vcipj6Xz0mDvleit0GWKBBiaKkF2N'  
access_token_secret = 'd7vcrwwk9TeibLp1BIQUIWSWW9uGrIABO99GLtw7ky7Cz'  

#提交你的Key和secret  
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)  
auth.set_access_token(access_token, access_token_secret)  

#获取类似于内容句柄的东西  
api = tweepy.API(auth, wait_on_rate_limit=True, proxy="127.0.0.1:1080")  #tweepy初始化中添加此选项，以便在达到速率限制时等待而不是失败
  
#打印我自己主页上的时间轴里的内容  
# public_tweets = api.home_timeline() 
# 打印其他用户主页上的内容，其中""里面的是用户昵称即@后面的名字
# for item in tweepy.Cursor(api.user_timeline, id="GoogleAI").items(200):
#     print (item)
# public_tweets = api.user_timeline("HBO",since_id=1013864067537227778)
# public_tweets.reverse()
# for item in public_tweets:
#     print(item.text)
public_tweets = api.get_user("CNN")
# print(public_tweets)
# public_tweets = api.me()
def get_imgvideoUrl(public_tweets):
    if hasattr(public_tweets, public_tweets.extended_entities):
        extended_entities = public_tweets.extended_entities
        if extended_entities["media"][0].has_key("video_info"):
            videoUrl = extended_entities["media"][0]["video_info"]["variants"][0]["url"]
        else:
            videoUrl = ""
        imageUrl = extended_entities["media"][0]["media_url"]
        return (videoUrl, imageUrl)
    else:
        return ("", "")

public_tweets = api.get_status(1027056874057859072) #查看具体推文的状态
# imgvideoUrl = get_imgvideoUrl(public_tweets)

# tweetsText = public_tweets.text
tweetsText = "app 📲https://t.co/Xgo5kjIt8c"
#替换emogi表情
# highPoints = re.compile("[^\\uD800-\\uDBFF][\\uDC00-\\uDFFF]")
highPoints = re.compile(r"[\uD800-\uDFFF]")

tweetsText1 = highPoints.sub("", tweetsText)
print  (tweetsText1)
# tweetsUrl = "https://twitter.com/%s/status/%d"%(public_tweets.user.screen_name, public_tweets.id)
# imageUrl = public_tweets.entities["media"][0]["media_url"]

# videoUrl = imgvideoUrl[0]
# imageUrl = imgvideoUrl[1]

retweetCount = public_tweets.retweet_count
favoriteCount = public_tweets.favorite_count
tweetTime = public_tweets.created_at

print(public_tweets)
twitterpip = TwitterPip()
# for tweet in public_tweets:  
#     print (tweet.text)
#     twitterpip.process_item(tweet.text)
twitterpip.close()   
#搜索具有League of Legends(lol英雄联盟的全称)的关键词的帐号  
# for tweet in tweepy.Cursor(api.search,q='artificial intelligence').items(10):  
#     print('Tweet by: @' + tweet.user.screen_name)
