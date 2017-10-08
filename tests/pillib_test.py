from shicong.pillib import (open_img, remove_noise, remove_grayscale, remove_interference_line, recognition,
                            get_img_properties, convert_other_format, create_thumbnail, cut, paste, split_color_channel,
                            merge_color_channel, rotate, resize)
from unittest import TestCase, main

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

main()