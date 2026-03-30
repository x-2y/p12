#案例：输入两个数x和y，计算x+y以及x-y的结果并输出
# x=int(input("请输入x的值："))
# y=int(input("请输入y的值："))
# print(f"x+y={x+y},x-y={x-y}")
#计算输入的三个整数的平均数
# num1=int(input("请输入第一个数："))
# num2=int(input("请输入第二个数："))
# num3=int(input("请输入第三个数："))
# print(f"这三个数的平均数是：{(num1+num2+num3)/3}")
#要求输入梯形的上底，下底，高然后计算梯形的面积
# sd=int(input("请输入梯形的上底："))
# xd=int(input("请输入梯形的下底："))
# h=int(input("请输入梯形的高："))
# s=(sd+xd)*h/2
# print("梯形的面积为：",s)
#要求输入圆的半径，然后计算圆的周长和面积
# r=int(input("请输入圆的半径："))
# c=2*3.14*r
# s=3.14*r**2
# print(f"周长为：{c},面积为{s}")
#BMI的计算BMI=体重/身高的平方
# w=float(input("请输入体重(单位kg)："))
# h=float(input("请输入身高(单位m)："))
# print(f"BMI为{w/h**2}")

#键盘录入，判断是否在10-20之间
# num=int(input("请输入一个数："))
# print(f"{num}是否在10-20之间",num>=10 and num<=20)
# print(f"{num}是否在10-20之间", 10 <= num <= 20)  #简化，答案一样

#键盘录入，判断是否不在10-20之间
num=int(input("输入这个数字："))
print(f"{num}是否不在10-20之间",num<=10 or num>=20)