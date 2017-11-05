"""
csv 模块
"""
import xlwt


class CSVWriter(object):
    def __init__(self):
        self.csv = xlwt.Workbook()
        self.sheet = self.csv.add_sheet('default')

    def write(self, x, y, value):
        self.sheet.write(x, y, value)

    def save(self, filename):
        self.csv.save(filename)
