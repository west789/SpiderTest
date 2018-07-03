import tweepy
from downImgVideo import downloadImg, downloadVideo, downloadHead, mkdirThreeFiles
from datetime import datetime
import re
import asyncio

def getTweetsUser(api,username,twitterPip):
    try:
        idList = twitterPip.get_twitterIdList()
        mkdirThreeFiles()
        userInfoDict = {}
        tweetInfoDict = {}
        userInfo = api.get_user(username)
        # print(userInfo)
        accountName = userInfo.name
        screenName = userInfo.screen_name
        twitterId = userInfo.status.id
        location = userInfo.location
        description = userInfo.description
        url = userInfo.url
        profileImage = getProfileImg(userInfo.profile_image_url)
        statusesCount = userInfo.statuses_count
        friendsCount = userInfo.friends_count
        followersCount = userInfo.followers_count
        favoritesCount = userInfo.favourites_count
        accountTime = userInfo.status.created_at
        userInfoDict["accountName"] = accountName
        userInfoDict["screenName"] = screenName
        userInfoDict["twitterId"] = str(twitterId)
        userInfoDict["location"] = location
        userInfoDict["description"] = description
        userInfoDict["url"] = url
        userInfoDict["profileImage"] = profileImage
        userInfoDict["statusesCount"] = statusesCount
        userInfoDict["friendsCount"] = friendsCount
        userInfoDict["followersCount"] = followersCount
        userInfoDict["favoritesCount"] = favoritesCount
        userInfoDict["accountTime"] = accountTime
        #插入数据库
        if idList == None or len(idList)==0:
            twitterPip.insert_userInfo(userInfoDict)
        elif idList != None and str(twitterId) in idList:
            twitterPip.update_userInfo(userInfoDict, twitterId)
        #获取当前账户下的推文
        accountId = twitterPip.get_accountId(userInfo.status.id)
        sinceId = twitterPip.get_sinceId(accountId)
        if sinceId != None:
            public_tweets = api.user_timeline(screenName, since_id=int(sinceId))
        else:
            public_tweets = api.user_timeline(screenName, count=20)
        try:
            public_tweets.reverse()      #将列表翻转序列
            flag = 0
            startTime = datetime.now()
            #使用协程
            loop = asyncio.get_event_loop()
            tasks = [tweetTask(tweet, tweetInfoDict, accountId, public_tweets, twitterPip, flag)
                    for tweet in public_tweets]
            loop.run_until_complete(asyncio.wait(tasks))
            loop.close()
            # for tweet in public_tweets:
            #     pass
        except Exception as e:
            print("错误信息:", e)
        finally:
            endTime = datetime.now()
            runningTime = endTime-startTime
            print("花费时间为：%s"%runningTime)
        twitterPip.close()
        print("账户：%s,一共更新: %d 条记录"%(accountName, flag))
    except Exception as e:
        print (e)
        print("错误信息")

#获取视频照片
def get_imgvideoUrl(tweet):
    if hasattr(tweet, "extended_entities"):
        extended_entities = tweet.extended_entities
        if "video_info" in extended_entities["media"][0]:
            videoUrl = extended_entities["media"][0]["video_info"]["variants"][0]["url"]
            if 'm3u8' in videoUrl:
                videoUrl = extended_entities["media"][0]["video_info"]["variants"][1]["url"]
            videoUrl = downloadVideo(videoUrl)
        else:
            videoUrl = ""
        imageUrl = extended_entities["media"][0]["media_url"]
        imageUrl = downloadImg(imageUrl)
        return (videoUrl, imageUrl)
    else:
        return ("", "")

#获取头像路径
def getProfileImg(profileImg):
    return downloadHead(profileImg)

def tweetTask(tweet, tweetInfoDict, accountId, public_tweets, twitterPip, flag):               
    tweetsText = tweet.text
    tweetsUrl = "https://twitter.com/%s/status/%d"%(tweet.user.screen_name, tweet.id)
    twitterId = str(tweet.id)
    imgvideoUrl =  get_imgvideoUrl(tweet)
    videoUrl = imgvideoUrl[0]
    imageUrl = imgvideoUrl[1]
    retweetCount = tweet.retweet_count
    favoriteCount = tweet.favorite_count
    tweetTime = tweet.created_at
    tweetInfoDict["accountId"] = accountId
    tweetInfoDict["tweetsText"] = tweetsText
    tweetInfoDict["tweetsUrl"] = tweetsUrl
    tweetInfoDict["twitterId"] = twitterId
    tweetInfoDict["videoUrl"] = videoUrl
    tweetInfoDict["imageUrl"] = imageUrl
    tweetInfoDict["retweetCount"] = retweetCount
    tweetInfoDict["favoriteCount"] = favoriteCount  
    tweetInfoDict["tweetTime"] = tweetTime.strftime("%Y-%m-%d %H:%M:%S")
    tweetNum = public_tweets.index(tweet)+1
    print ("第%d个文件："%tweetNum)
    flag = twitterPip.insert_tweetInfo(tweetInfoDict, flag)