#if条件判断，如果分数大于680，就上清华
# score=700
# if score>680:
#     print("清华欢迎你！！")
#     print("祝你大学生活愉快！！")

#正确的账号和密码
# b_account="18888888"
# b_password="78787878"
#
# #1.接收用户输入的账号和密码
# account=input("请输入您的账号：")
# password=input("请输入您的密码：")
#
# #2.判断账号和密码是否完全正确
# if account==b_account and password==b_password:
#     print("登陆成功！欢迎您！")
# else:
#     print("登陆失败！")
#     print("账号或密码错误！")


#判断是否是闰年（能被4整除且不能被100整除 或者 能被400整除 ）
# year=int(input("请输入需要判定的年份:"))
# if (year%4==0 and year%100!=0) or (year%400==0):
#     print(f"{year}是闰年！")
# else:
#     print(f"{year}是平年！")

#根据用户输入的数字，判断该数字是奇数还是偶数
# num1=int(input("请输入需要判断的数字:"))
# if num1%2==0:
#     print(f"{num1}是偶数")
# else:
#     print(f"{num1}是奇数")

#根据用户输入的年龄判断是否成年
# age=int(input("请输入你的年龄："))
# if age>=18:
#     print(f"{age}岁已经成年！")
# else:
#     print("你还没有成年！")

#输入一个数判断是正数还是负数
# num2=int(input("请输入需要判断的数字："))
# if num2>0:
#     print("%s是正数"%num2)
# elif num2<0:
#     print("%s是负数"%num2)
# else:
#     print("%s是0"%num2)

#根据用户输入的成绩判断是否及格
# score=int(input("请输入你的成绩："))
# if score>=85:
#     print("优秀！")
# elif score>=60:
#     print("及格！")
# else:
#     print("不及格！")


#当金额>=500打8折   300<=金额<500打9折   100<=金额<300打95折  金额<100无折扣
# money=int(input("请输入金额："))
# if money>=500:
#     money*=0.8
#     print(f"应付{money}元")
# elif money>=300:
#     money*=0.9
#     print(f"应付{money}元")
# elif money>=100:
#     money*=0.95
#     print(f"应付{money}元")
# else:
#     print(f"应付{money}元")
#

#根据用电度数，计算电费
# d=int(input("请输入用电度数："))
# if d<2880:
#     df=d*0.4883
#     print(f"需要缴{df}元")
# elif d<=4800:
#     df = d * 0.5383
#     print(f"需要缴{df}元")
# else:
#     df = d * 0.7883
#     print(f"需要缴{df}元")


