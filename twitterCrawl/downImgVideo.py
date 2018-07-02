import requests
import os

headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.99 Safari/537.36"}
basePath = os.path.join(os.getcwd(), "twitterCrawl")
def downloadVideo(videoUrl):
    try:
        videoUrl = videoUrl.split("?")[0]
        if not os.path.exists(basePath+"/videos"):
            os.mkdir(basePath+"/videos")
        baseVideoPath = os.path.join(basePath, "videos")
        videoName = os.path.basename(videoUrl)
        response = requests.get(videoUrl, headers=headers)
        videoContent = response.content
        with open(baseVideoPath+"/%s"%videoName, "wb") as f:
            f.write(videoContent)
        videoPath = os.path.join(baseVideoPath, videoName)
        return videoName
    except Exception as e:
        print(e)
        return ""

def downloadImg(imgUrl):
    try:
        if not os.path.exists(basePath + "/images"):
            os.mkdir(basePath + "/images")
        imgName = os.path.basename(imgUrl)
        response = requests.get(imgUrl, headers=headers)
        imgContent = response.content
        # with open(baseName+"/%s"%imgName, 'wb') as f:
        with open(basePath + "/images" + "/%s" % imgName, 'wb') as f:
            f.write(imgContent)
        imgPath = basePath + "/images" + "/%s" % imgName
        return imgName
    except Exception as e:
        print(e)
        return ""

def downloadHead(profileImgUrl):
    try:
        if not os.path.exists(basePath + '/images/headImg'):
            os.mkdir(basePath + '/images/headImg')
        profileImgName = os.path.basename(profileImgUrl)
        response = requests.get(profileImgUrl, headers=headers)
        with open(basePath + '/images/headImg/+%s'% profileImgName, 'wb') as f:
            f.write(response.content)
        return profileImgName
    except Exception as e:
        print(e)
        return ""
# if __name__ == '__main__':
#     path = os.getcwd()
#     print(path)
#     # downloadImg("http://pbs.twimg.com/media/Dgt3WaGV4AEzGny.jpg")
#     downloadVideo("https://video.twimg.com/amplify_video/1012022754457948160/vid/720x720/3SE7Lcd4A3FfvKW1.mp4?tag=3")
