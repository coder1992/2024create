from math import ceil

//weight表示快递的重量
weight=float(input("请输入重量"))
//pos表示所在地区的邮编代号
pos=int(input("请输入地区编号"))
if pos==1:
    cost=ceil(weight-2)*3+13
elif pos==2:
    cost=ceil(weight-2)*2+12
else :
    cost=ceil(weight-2)*4+14
print("费用是",cost,"元")
