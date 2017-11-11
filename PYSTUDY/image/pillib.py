"""
pil模块
遗憾的是原作者早在2009年就停止了维护
感叹的是，中国无人，这些伟大的开源项目都是国外人发明的。
看看中国的人，是多么的浮躁，国家也是处于虚强。如果我有能力
我也想移民美国。毕竟在温水里，怎么可能有善终。
"""
from PIL import Image, ImageEnhance, ImageFilter
from PIL.ExifTags import TAGS, GPSTAGS
from io import BytesIO
import pytesseract
from PYSTUDY.debuglib import trace_info


from PYSTUDY.html_parserlib import ReParser

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
    更改图片大小，只能更改磁盘空间的大小。
    :param img:
    :param width:
    :param height:
    :return: 更改后的图片
    """
    return img.resize((width, height), Image.ANTIALIAS)

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

class GPS:
    def get_exif_data(self, image):
        """Returns a dictionary from the exif data of an PIL Image item. Also converts the GPS Tags"""
        exif_data = {}
        info = image._getexif()
        if info:
            for tag, value in info.items():
                decoded = TAGS.get(tag, tag)
                if decoded == "GPSInfo":
                    gps_data = {}
                    for t in value:
                        sub_decoded = GPSTAGS.get(t, t)
                        gps_data[sub_decoded] = value[t]

                    exif_data[decoded] = gps_data
                else:
                    exif_data[decoded] = value

        return exif_data

    def _get_if_exist(self, data, key):
        if key in data:
            return data[key]

        return None

    def _convert_to_degress(self, value):
        """Helper function to convert the GPS coordinates stored in the EXIF to degress in float format"""
        d0 = value[0][0]
        d1 = value[0][1]
        d = float(d0) / float(d1)

        m0 = value[1][0]
        m1 = value[1][1]
        m = float(m0) / float(m1)

        s0 = value[2][0]
        s1 = value[2][1]
        s = float(s0) / float(s1)

        return d + (m / 60.0) + (s / 3600.0)

    def get_lat_lon(self, exif_data):
        """Returns the latitude and longitude, if available, from the provided exif_data (obtained through get_exif_data above)"""
        lat = None
        lon = None

        if "GPSInfo" in exif_data:
            gps_info = exif_data["GPSInfo"]

            gps_latitude = self._get_if_exist(gps_info, "GPSLatitude")
            gps_latitude_ref = self._get_if_exist(gps_info, 'GPSLatitudeRef')
            gps_longitude = self._get_if_exist(gps_info, 'GPSLongitude')
            gps_longitude_ref = self._get_if_exist(gps_info, 'GPSLongitudeRef')

            if gps_latitude and gps_latitude_ref and gps_longitude and gps_longitude_ref:
                lat = self._convert_to_degress(gps_latitude)
                if gps_latitude_ref != "N":
                    lat = 0 - lat

                lon = self._convert_to_degress(gps_longitude)
                if gps_longitude_ref != "E":
                    lon = 0 - lon

        return lat, lon

    def get_gps(self, image):
        """获取经度，纬度"""
        exif_data = self.get_exif_data(image)
        return self.get_lat_lon(exif_data)

    def set_gps(self, image, lat, lon):
        pass

def get_size(img):
    """"""
    return img.size

def save(filename, img):
    img.save(filename)
