from shicong.pdflib import *

if __name__ == '__main__':
    # 水印pdf文件名
    pdf_water = '供应链图片.pdf'
    pdf_in = '被盖章的.pdf'
    pdf_out = '输出.pdf'
    pdf_compressed = '输出_压缩的.pdf'
    create_watermark('猎芯供应链.png', pdf_water)
    add_watermark(pdf_in, pdf_water, pdf_out)
    compress(pdf_out, pdf_compressed)