"""
pil模块
"""
from PIL import Image
from io import BytesIO
import pytesseract

def get_img_from_bytes(content):
    """
    从二进制数据中返回一张图片对象
    :param content: 图片二进制数据
    :return: Image
    """
    return Image.open(BytesIO(content))

def open_img(filename):
    """
    从文件中打开图片
    :param filename: 图片文件名
    :return: Image
    """
    return Image.open(filename)

def convert_png(filename):
    """
    转换为png图片
    :param filename: 图片文件名
    :return:
    """
    img = Image.open(filename)
    img.save('')

def recognition(img):
    """
    识别图片
    :param img: Image
    :return: 字符串
    """
    return pytesseract.image_to_string(img)

def to_gray(image):
    """
    转化为灰度
    :param image:
    :return:
    """
    return image.convert('L')

def binarizing(img,threshold):
    """
    二值化
    :param img:
    :param threshold:
    :return:
    """
    pixdata = img.load()
    w, h = img.size
    for y in range(h):
        for x in range(w):
            if pixdata[x, y] < threshold:
                pixdata[x, y] = 0
            else:
                pixdata[x, y] = 255
    return img

def depoint(img):
    """
    去除干扰线
    :param img:
    :return:
    """
    pixdata = img.load()
    w,h = img.size
    for y in range(1,h-1):
        for x in range(1,w-1):
            count = 0
            if pixdata[x,y-1] > 245:
                count = count + 1
            if pixdata[x,y+1] > 245:
                count = count + 1
            if pixdata[x-1,y] > 245:
                count = count + 1
            if pixdata[x+1,y] > 245:
                count = count + 1
            if count > 2:
                pixdata[x,y] = 255
    return img