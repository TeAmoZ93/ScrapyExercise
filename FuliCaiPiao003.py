#-*- coding:utf-8 -*-
'''
Created on 2020年7月10日
@author: Administrator
'''
import random
import xlwt
import xlrd
from pyecharts import Line
from pyecharts import Bar
import numpy as np

#1th:循环指定次数，生成随机数列表
#2nd:统计小球出现的次数，并写入excel
def WriteExcel():
    A=[]
    B=[]
    row = 0
    col = 0
    for i  in range(1,100001):
        a=random.sample(range(1,34),6)
        for aa in a:
            A.append(aa)
        b=random.randint(1,16)
        B.append(b)
    workbook = xlwt.Workbook()
    fileName = 'shaungseqiu.xls'
    file = xlwt.Workbook(encoding = 'utf-8')
    sheet1 = file.add_sheet('RED BALL', cell_overwrite_ok=True)
    sheet2 = file.add_sheet('BLUE BALL', cell_overwrite_ok=True)
    for t in range(1,34):
        sheet1.write(row,col,'红球%s'%t)
        col+=1
        sheet1.write(row,col,A.count(t))
        row += 1
        col = 0
#     print('写入成功') 

    roww = 0
    coll = 0
    for tt in range(1,34):
        sheet2.write(roww,coll,'蓝球%s'%tt)
        coll+=1
        sheet2.write(roww,coll,B.count(tt))
        roww += 1
        coll = 0
#     print('写入成功') 
    file.save(fileName)
    
def HuiTu():
#画图（可视化处理）
    y=''
    y1=''
    data = xlrd.open_workbook('shaungseqiu.xls')
    table = data.sheets()[0]
    table1= data.sheets()[1]
    y=table.col_values(1)#读取列的值
    y1=table1.col_values(1)#读取列的值
    pr=np.linspace(1,33,len(y))#等间隔取值
    bar=Bar("小球出现次数","统计如下")#主副标题
    bar.add("红球次数统计",pr,y,mark_point=["min","max"])#标题
    bar.add("蓝球次数统计",pr,y1,mark_point=["max"])#标题
    bar.render(r"500.html")

def ShuChuRes():
    WriteExcel()
    HuiTu()
    f1=xlrd.open_workbook('shaungseqiu.xls')
    sheet=f1.sheet_by_index(0)
    rows=sheet.nrows
    data=[[]for i in range(rows)]
    for i in range(0,rows):
        data[i] = sheet.row_values(i)[0:2]
    Tui=sorted(data,key=(lambda x:x[1]))
    print ('本期双色球推荐%s,%s,%s,%s,%s,%s'%(Tui[0][0],Tui[1][0],Tui[2][0],Tui[3][0],Tui[4][0],Tui[5][0]))

    sheet1=f1.sheet_by_index(1)
    rows1=sheet1.nrows
    data1=[[]for i in range(rows1)]
    for i in range(0,rows1):
        data1[i]=sheet1.row_values(i)[0:2]
    Tui1=sorted(data1,key=(lambda x:x[1]))
    print ('本期双色球推荐%s'%Tui1[17][0])
    
if __name__=='__main__':
    ShuChuRes()





