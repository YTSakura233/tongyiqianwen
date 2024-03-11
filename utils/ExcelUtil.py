"""
Excel读取的相关方法
@author zhaoyukun
"""
import openpyxl
import xlrd
from openpyxl.styles import PatternFill
from xlwt import Pattern
from xlwt import XFStyle


class ExcelUtil:
    @staticmethod
    def read_excel(excel_file):
        book = ''
        if excel_file.endwith('xls'):
            book = xlrd.open_workbook(excel_file)
        elif excel_file.endwith('xlsx'):
            book = openpyxl.load_workbook(excel_file)
        return book
