from unittest import TestCase

from shicong.image.pillib import (open_img, get_img_properties, convert_other_format, create_thumbnail, cut, paste,
                                  split_color_channel, get_size, save,
                                  merge_color_channel, rotate, resize, GPS)
from shicong.oslib import getsize

class PillibTestCase(TestCase):
    def test_get_img_properties(self):
        img = open_img('pillib_data/0.tif')
        print(get_img_properties(img))

    def test_convert_other_format(self):
        filename = 'pillib_data/0.tif'
        convert_other_format(filename, '.png')

    def test_create_thumbnail(self):
        img = open_img('pillib_data/0.png')
        img = create_thumbnail(img, 5, 5)
        # img.show()

    def test_cut_paste(self):
        img_src = open_img('pillib_data/a50f4bfbfbedab64876212cdf136afc379311eae.jpg')
        img_dst = open_img('pillib_data/a50f4bfbfbedab64876212cdf136afc379311eae.jpg')
        region = cut(img_src, 100, 100, 400, 400)
        paste(region, img_dst, 200, 200, 500, 500)
        # img_src.show()
        # img_dst.show()

    def test_split_color_channel(self):
        img = open_img('pillib_data/a50f4bfbfbedab64876212cdf136afc379311eae.jpg')
        r, g, b = split_color_channel(img)
        print(r, g, b)
        # r.show()
        # g.show()
        # b.show()

        img = open_img('pillib_data/0.png')
        r, g, b = split_color_channel(img)
        print(r, g, b)
        # r.show()
        # g.show()
        # b.show()

    def test_merge_color_channel(self):
        # 对灰度颜色通道的图片没有效果
        img = open_img('pillib_data/0.png')
        img.show()
        print(get_img_properties(img))
        r, g, b = split_color_channel(img)
        # 这里颠倒顺序之后，原图会被改变。
        img = merge_color_channel('RGB', g, b, r)
        img.show()

    def test_rotate_resize(self):
        img = open_img('pillib_data/0.png')
        img = rotate(img, 45)
        # img.show()
        img = resize(img, 100, 100)
        # img.show()

    def test_gps(self):
        img = open_img("pillib_data/mmexport1507584906988.jpg")
        print(GPS().get_gps(img))

    def test_resize(self):
        src = "pillib_data/我.jpg"
        dst = 'pillib_data/缩小的我.jpg'

        src_size = getsize(src)
        print('源文件的大小为：', src_size)

        img = open_img(src)
        # img.show()
        width, height = get_size(img)
        print(width, height)
        img = resize(img, width // 2, height // 2)
        save(dst, img)

        dst_size = getsize(dst)
        print('目标文件的大小：', dst_size)