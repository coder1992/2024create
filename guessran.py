import random
num=random.randint(1,10)
print(num)
gussnum=int(input("请输入一个1-10之间的整数"))

if gussnum==num:
    print("恭喜你猜对了")
elif gussnum>num:
    print("你猜的数字大了，请再猜一下")
else :
    print("你猜的数字小了，请再猜一下")

gussnum=int(input("请再输入一个1-10之间的整数"))

if gussnum==num:
    print("恭喜你猜对了")
elif gussnum>num:
    print("你猜的数字大了，请再猜一下")
else :
    print("你猜的数字小了，请再猜一下")

gussnum=int(input("请再输入一个1-10之间的整数"))
if gussnum==num:
    print("恭喜你猜对了")
else :
    print("三次机会用完了，很遗憾没有猜中")