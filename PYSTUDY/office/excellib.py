"""
excel操作模块
"""

import xlwt


class ExcelWriter(object):
    def __init__(self):
        self.excel = xlwt.Workbook()
        self.sheet = self.excel.add_sheet('default')

    def write(self, x, y, value):
        self.sheet.write(x, y, value)

    def save(self, filename):
        self.excel.save(filename)
