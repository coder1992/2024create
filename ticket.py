//height表示身高
height=float(input("请输入您的身高，单位cm："))
//身高120以下的用户免费游玩
if height>=120:
    print("您的身高超过了120cm，需要补票10元")
else:
    print("可以免费游玩")
print("祝您游玩愉快")
