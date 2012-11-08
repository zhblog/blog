#!/usr/bin/python

import sys
from pyExcelerator import XFStyle, Borders, Alignment, Workbook
import copy

reload(sys)
sys.setdefaultencoding('utf8')


def returnStyle():
    borders = Borders()
    borders.left = 0
    borders.right = 0
    borders.top = 0
    borders.bottom = 0
    #borders.Font.Size = 10
    borders.Font = "10"

    al = Alignment()
    al.horz = Alignment.HORZ_CENTER
    al.vert = Alignment.VERT_CENTER

    style = XFStyle()
    style.borders = borders
    style.alignment = al
    return style


def returnReadList(filename):
    vals = []
    tvals = []
    fp = open(filename, 'r')
    lines = fp.readlines()
    NAME = ""
    for line in lines:
        values = []
        lline = line.strip('\n').split("\t")
        name = lline[0]
        if NAME:
            pass
        else:
            NAME = name
        for for2 in lline:
            if for2:
                values.append(for2)
            else:
                values.append("--")
        if name == NAME:
            pass
        else:
            NAME = name
            if len(vals) > 0:
                tvals.append(copy.deepcopy(vals))
                vals = []
        if len(values) > 0:
            vals.append(copy.deepcopy(values))
    if len(vals) > 0:
        tvals.append(copy.deepcopy(vals))
    fp.close()
    return tvals


def returnLast(tvals):
    yblist = []
    maxnum = 0
    for vals in tvals:
        flag = 0
        for ll in vals:
            flag = flag + 1
        if flag > maxnum:
            maxnum = flag
            yblist = vals
    newval = []
    for vals in tvals:
        valtest = []
        for ybv in yblist:
            if ybv[1] == vals[0][1]:
                break
            else:
                valtest.append([vals[0][0], ybv[1], "--", "--"])
        if valtest:
            vals = valtest + vals
        newval.append(vals)
    return newval


def writeExle(wbsave, ws, style, tvals, outfile):
    ws.write(0, 0, "\\", style)
    zflag = 1
    for vals in tvals:
        flag = 1
        for ll in vals:
            ws.write(0, zflag, unicode(ll[0]), style)
            ws.write(flag, zflag, ll[2], style)
            ws.write_merge(flag, flag + 1, 0, 0, ll[1], style)
            flag = flag + 1
            ws.write(flag, zflag, ll[3], style)
            flag = flag + 1
        zflag = zflag + 1
    wbsave.save(outfile)

if __name__ == "__main__":
    wbsave = Workbook()
    ws = wbsave.add_sheet('sheet1')
    style = returnStyle()
    outfile = "end.xls"
    infile = "in.txt"
    if len(sys.argv) > 2:
        outfile = sys.argv[2]
        infile = sys.argv[1]
    filelist = returnReadList(infile)
    tvals = returnLast(filelist)
    writeExle(wbsave, ws, style, tvals, outfile)
