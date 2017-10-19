"""
pdf模块
"""
import os

from PyPDF2 import PdfFileWriter, PdfFileReader
from reportlab.lib.units import cm
from reportlab.pdfgen import canvas


def create_watermark(f_jpg, pdf_out):
    """创建图片水印pdf
    """
    f_pdf = pdf_out
    w_pdf = 20 * cm
    h_pdf = 20 * cm

    c = canvas.Canvas(f_pdf, pagesize=(w_pdf, h_pdf))
    c.setFillAlpha(0.5)  # 设置透明度
    c.drawImage(f_jpg, 5 * cm, 5 * cm, 5 * cm, 5 * cm)  # 这里的单位是物理尺寸 c.save()


def add_watermark(pdf_file_in, pdf_file_mark, pdf_file_out):
    """添加水印
    """
    pdf_output = PdfFileWriter()
    input_stream = open(pdf_file_in, 'rb')
    pdf_input = PdfFileReader(input_stream)

    # PDF文件被加密了
    if pdf_input.getIsEncrypted():
        print('该PDF文件被加密了.')
        # 尝试用空密码解密
        try:
            pdf_input.decrypt('')
        except Exception as e:
            print('尝试用空密码解密失败.')
            return False
        else:
            print('用空密码解密成功.')
    # 获取PDF文件的页数
    page_num = pdf_input.getNumPages()
    # 读入水印pdf文件
    pdf_watermark_input_stream = open(pdf_file_mark, 'rb')
    pdf_watermark = PdfFileReader(pdf_watermark_input_stream)
    # 给每一页打水印
    for i in range(page_num):
        page = pdf_input.getPage(i)
        page.mergePage(pdf_watermark.getPage(0))
        page.compressContentStreams()  # 压缩内容
        pdf_output.addPage(page)
    output_stream = open(pdf_file_out, "wb")
    pdf_output.write(output_stream)
    input_stream.close()
    pdf_watermark_input_stream.close()
    output_stream.close()


def compress(pdf_in, pdf_output):
    """
    mac下安装 brew install ghostscript
    :param pdf_in:
    :param pdf_output:
    :return:
    """
    cmd = 'gs -dNOPAUSE -dBATCH -sDEVICE=pdfwrite -dCompatibilityLevel=1.4 -dPDFSETTINGS=/screen -sOutputFile=%s %s'
    cmd = cmd % (pdf_output, pdf_in)
    os.system(cmd)
