from PIL import Image
from io import BytesIO

def get_img_from_bytes(content):
    """
    从二进制数据中返回一张图片对象
    :param content: 图片二进制数据
    :return: Image
    """
    return Image.open(BytesIO(content))