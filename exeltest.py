#!/usr/bin/python3

from pathlib import Path
import openpyxl as xls

def main():
    wb = xls.load_workbook(filename='Python_xls_test.xlsx')

    print(wb.sheetnames)


if '__name__' == __name__:
    main()
