#!/usr/bin/python
from xlrd import open_workbook
import sys
from pyExcelerator import *

DAY = 5

infile = "start.xlsx"
outfile = "end.xlsx"

if len(sys.argv) > 2:
    infile = sys.argv[1]
    outfile = sys.argv[2]


borders = Borders()
borders.left = 0
borders.right = 0
borders.top = 0
borders.bottom = 0

al = Alignment()
al.horz = Alignment.HORZ_CENTER
al.vert = Alignment.VERT_CENTER

style = XFStyle()
style.borders = borders
style.alignment = al

wbsave = Workbook()
ws = wbsave.add_sheet('sheet1')

wb = open_workbook(infile, 'rb')
vals = []
tvals = []
for s in wb.sheets():
    if s.name == "Sheet1":
        flag = 0
        for row in range(s.nrows):
            values = []
            print row
            if row < 1:
                continue
            for col in range(s.ncols):
                if len(s.cell(row, col).value) > 0:
                    values.append(s.cell(row, col).value)
            print ",".join(values)
            if len(values) > 0:
                vals.append(values)
            else:
                continue
            flag = flag + 1
            if flag == DAY:
                if len(vals) > 0:
                    tvals.append(vals)
                flag = 0
                print  vals
                vals = []

        print


print tvals
ws.write(0, 0, "ll[2]", style)
zflag = 1
for vals in tvals:
    flag = 1
    for ll in vals:
        ws.write(0, zflag, ll[0], style)
        ws.write(flag, zflag, ll[2], style)

        ws.write_merge(flag, flag + 1, 0, 0, ll[1], style)

        flag = flag + 1

        ws.write(flag, zflag, ll[3], style)

        flag = flag + 1
    zflag = zflag + 1

wbsave.save(outfile)
