#根据用户输入的账号密码执行登陆操作
#admin/111222，zhangsan/888888，togo/000111
# while True:
#     username=input("请输入你的用户名：")
#     password=input("请输入你的密码：")
#     if username=="" or password=="":
#         print("输入的用户名和密码不能为空！请重新输入！")
#         continue
#     elif username=="admin" and password=="111222":
#         print("登陆成功！")
#         break
#     elif username=="zhangsan" and password=="888888":
#         print("登陆成功！")
#         break
#     elif username=="togo" and password=="000111":
#         print("登陆成功！")
#         break
#     else:
#         print("用户名或密码错误，请重新输入！")

#猜数字
# import random
# r=random.randint(1,100)
# print(r)
# while True:
#     m=int(input("请输入你猜的数字："))
#     if m==r:
#         print("恭喜你，猜对了！！数字是%s"%m)
#         break
#     elif m>r:
#         print("猜大了，请继续！")
#         continue
#     elif m<r:
#         print("猜小了，请继续！")
#         continue

#将1-1000(包括100)之间所有5的倍数的数字加起来
# total=0
# for i in range(1,1001):
#     if i%5==0:
#         total+=i
# print(total)

#统计有多少个j和f
s="jssfjdlaja;ffnxjfsihfei"
# n=s.count("j")
# m=s.count("f")
# print(n,m)
# n=0
# m=0
# for i in s:
#     if i=='j':
#         n+=1
#     elif i=='f':
#         m+=1
# print(n,m)




