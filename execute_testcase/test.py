#!/usr/bin/env python
#coding=utf-8

from utils import common

ws = common.get_sheet('../TestCase/TestCase.xlsx', 'TestCase')
rows = ws.rows
columns = ws.columns
for i in rows:
    num = ws.cell(i, 0).value
    num1 = ws.cell(i, 1).value
    num2 = ws.cell(i, 2).value
    num3 = ws.cell(i, 3).value
    num4 = ws.cell(i, 4).value
    num5 = ws.cell(i, 5).value
    num6 = ws.cell(i, 6).value
    num7 = ws.cell(i, 7).value
    print num
    print num1
    print num2
    print num3