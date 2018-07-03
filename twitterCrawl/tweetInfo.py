import tweepy
from downImgVideo import downloadImg, downloadVideo, downloadHead
from datetime import datetime
import re

def getTweetsUser(api,username,twitterPip):
    try:
        idList = twitterPip.get_twitterIdList()
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
        if idList == None:
            twitterPip.insert_userInfo(userInfoDict)
        elif idList != None and str(twitterId) in idList:
            twitterPip.update_userInfo(userInfoDict, twitterId)
        # print (userInfoDict)
        #获取当前账户下的推文
        public_tweets = api.user_timeline(screenName, count=200)
        try:
            highpoints = re.compile(u'[\uD800-\uDBFF][\uDC00-\uDFFF]') 
            for tweet in public_tweets:
                # print (tweet)
                accountId = twitterPip.get_accountId(userInfo.status.id)
                tweetsText = tweet.text
                tweetsText = highpoints.sub("--emoji--", tweetsText)
                tweetsUrl = "https://twitter.com/%s/status/%d"%(tweet.user.screen_name, tweet.id)
                imgvideoUrl = get_imgvideoUrl(tweet)
                videoUrl = imgvideoUrl[0]
                imageUrl = imgvideoUrl[1]
                retweetCount = tweet.retweet_count
                favoriteCount = tweet.favorite_count
                tweetTime = tweet.created_at
                tweetInfoDict["accountId"] = accountId
                tweetInfoDict["tweetsText"] = tweetsText
                tweetInfoDict["tweetsUrl"] = tweetsUrl
                tweetInfoDict["videoUrl"] = videoUrl
                tweetInfoDict["imageUrl"] = imageUrl
                tweetInfoDict["retweetCount"] = retweetCount
                tweetInfoDict["favoriteCount"] = favoriteCount  
                tweetInfoDict["tweetTime"] = tweetTime.strftime("%Y-%m-%d %H:%M:%S")
                tweetNum = public_tweets.index(tweet)+1
                print ("第%d个文件："%tweetNum)
                twitterPip.insert_tweetInfo(tweetInfoDict)
        except Exception as e:
            print("错误信息:", e, tweetsUrl)
        twitterPip.close()
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
