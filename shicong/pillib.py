"""
pil模块
"""
from PIL import Image, ImageEnhance, ImageFilter
from io import BytesIO
import pytesseract


from shicong.html_parserlib import ReParser

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
    如果文件打开错误，返回 IOError 错误。
    :param filename: 图片文件名
    :return: Image
    """
    return Image.open(filename)

def convert_other_format(filename, format):
    """
    转换为png图片
    :param filename: 图片文件名
    :return:
    """
    img = Image.open(filename)
    rp = ReParser()
    c_filename = rp.replace(r'\..*$', format, filename)
    img.save(c_filename)


def recognition(img):
    """
    识别图片
    :param img: Image
    :return: 字符串
    """
    return pytesseract.image_to_string(img)

def remove_grayscale(image):
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

def remove_interference_line(img):
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

def remove_noise(img):
    """
    去噪点
    :param img: 图片对象
    :return: 去除背景的图片
    """
    return ImageEnhance.Sharpness(img).enhance(3)

def get_img_properties(img):
    """
    获取文件的属性
    >>> from __future__ import print_function
    >>> print(im.format, im.size, im.mode)
    PPM (512, 512) RGB
    format 这个属性标识了图像来源。如果图像不是从文件读取它的值就是None, 也就是这个图片是什么类型的图片，比如a.tif, 那么就是TIFF
    size属性是一个二元tuple，包含width和height（宽度和高度，单位都是px)。
    mode 属性定义了图像bands的数量和名称，以及像素类型和深度。常见的modes
         有 “L” (luminance) 表示灰度图像, “RGB” 表示真彩色图像, and “CMYK” 表示出版图像。
    :param img: 加载过的图片对象
    :return: (format, size, mode)
    """
    return (img.format, img.size, img.mode)

def show(img):
    """
    显示图像
    注解 标准的 show() 效率并不高，它需要保存图像到临时文件
    然后通过 xv 显示图像。你需要先安装 xv ，显示图像有助于调试和测试。
    :param img: 加载到内存中的图片
    :return:
    """
    img.show()

def create_thumbnail(img, width, height):
    """
    创建缩略图
    缩略图的意思就是缩小
    :param img: 图片对象
    :param width: 宽
    :param height: 高
    :return:
    """
    size = (width, height)
    img.thumbnail(size)
    return img

def cut(img, left, above, right, down):
    """
    从图像中复制出一个矩形选区

    box = (100, 100, 400, 400)
    region = im.crop(box)
    矩形选区有一个4元元组定义，分别表示左、上、右、下的坐标。这个库以左上角为坐标原点，
    单位是px，所以上诉代码复制了一个 300x300 pixels 的矩形选区

    :param img: 加载到内存的图片
    :param left: 左
    :param above: 上
    :param right: 右
    :param down: 下
    :return:
    """
    box = (left, above, right, down)
    region = img.crop(box)
    return region

def paste(region, img, left, above, right, down):
    """
    将扣的图粘贴到制定图片上
    当你粘贴矩形选区的时候必须保证尺寸一致。此外，矩形选区不能在图像外。然而你不必保证矩形选区和原图的颜色模式一致，
    因为矩形选区会被自动转换颜色，遗憾的是，只能扣矩形图。

    :param region: 扣出的图
    :param img: 指定图片
    :param left: 左
    :param above: 上
    :param right: 右
    :param down: 下
    :return: 被修改过的图片对象，还在内存中，未保存。
    """
    region = region.transpose(Image.ROTATE_180)
    box = (left, above, right, down)
    img.paste(region, box)
    return img

def split_color_channel(img):
    """
    分离颜色通道
    :param img: 加载到内存的图片
    :return: 颜色通道
    """
    return img.split()

def merge_color_channel(mode, *params):
    """
    合并颜色通道
    :param mode: 颜色通道
    :param params: 颜色通道元组参数
    :return: 合并后的图像
    """
    return Image.merge(mode, params)

def resize(img, width, height):
    """
    更改图片大小
    :param img:
    :param width:
    :param height:
    :return: 更改后的图片
    """
    return img.resize((width, height))

def rotate(img, angle):
    """
    旋转图片
    :param img: 图片
    :param angle: 度数
    :return: 新图片
    """
    return img.rotate(angle)

def filter(img, filter_class):
    """
    图像滤波

    TODO：由于关于滤波方面的图像处理技术，历史可以追溯到1980年左右，所以，学些这方面的算法的时间需要一定的时间，看来源码
          原作者写了很多的滤波器，所以，得研究下每种滤波器的优缺点，使用场景。
    :param img:
    :param filter_class:
    :return:
    """
    pass