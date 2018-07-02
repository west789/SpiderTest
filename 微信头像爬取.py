from numpy import *
import itchat
import PIL.Image as Image
from os import listdir

def get_image():
    itchat.auto_login(hotReload=True)
    friends = itchat.get_friends(update=True)[1:101]
    num = 0
    for i in friends:
        img = itchat.get_head_img(userName=i["UserName"])
        with open( "./icon/" + str(num) + ".jpg",'wb') as fileImage:
            fileImage.write(img)
        num += 1
def get_big_img():
    pics = listdir("icon")
    numPic = len(pics)
    print(numPic)
    toImage = Image.new("RGB", (450, 450))
    x = 0
    y = 0
    for i in pics:
        try:
            img = Image.open("icon/{}".format(i))
        except IOError:
            print("Error: 没有找到文件或读取文件失败",i)
        else:
            img = img.resize((45, 45), Image.ANTIALIAS)
            toImage.paste(img, (x * 45, y * 45))
            x += 1
            if x == 10:
                x = 0
                y += 1
            print (i)
    toImage.save("icon/touxiang.jpg")
    itchat.send_image("icon/touxiang.jpg", 'filehelper')

get_image()
get_big_img()