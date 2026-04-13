# #字符串 -->不可修改，有序性，可迭代性
# s="Hello World"
# print(s[6])  #正向索引
# print(s[-5])  #反向索引
#
# #可迭代性
# for i in s:
#     print(i)
#
# #切片
# print(s[0:5:1])  #Hello
# print(s[:5:1])   #Hello
# print(s[:5:])    #Hello
# print(s[:5])     #Hello
#
# #步长-->正数:从前往后截取；负数:从后往前截取
# print(s[-1:-7:-1])
# print(s[::-1])   #dlroW olleH  s[-1:-12:-1]
# print(s[-1:-12:-1])
from mimetypes import init

# s="  Hello-Python-Hello-World  "
#
# #find(),找第一次出现的位置
# index=s.find("-")   #7
# print(index)
#
# #count(),统计子串在字符串中出现的次数
# c=s.count("-")     #3
# print(c)
#
# #upper(),转为大写
# su=s.upper()
# print(su)
# #lower(),转为小写
# sl=s.lower()
# print(sl)
#
# #split(),将字符串按照指定字符串切割成列表
# slist=s.split("-")    #['  Hello', 'Python', 'Hello', 'World  ']
# print(slist)
#
# #strip(),去除字符串两端的空格
# ss=s.strip()    #Hello-Python-Hello-World
# print(ss)
#
# #replace,将字符串中指定的子串替换为新的内容
# sr=s.replace("-","*")      #  Hello*Python*Hello*World
# print(sr)
#
# #startswith()/endswith(),判断字符串是否以指定的字符串开头/结尾，返回布尔值
# print(s.startswith("Hello"))   #False
# print(s.endswith("Python"))    #False
#
# print(s)    #原字符串s还是没有改变，因为字符串不允许改变  Hello-Python-Hello-World

#写一个程序，输入带空格的字符串，去除首尾空格后统计"单词"个数。
# s=input("请输入：")
# if s=="":
#     count=0
# else:
#     s1=s.strip()
#     s1=s1.split()   # 使用split()按空白字符分割，得到单词列表  ['Hello', 'Baby', 'Girl']
#     count=len(s1)   #len() 是 Python 的内置函数，用来返回一个对象（字符串、列表、元组等）的长度（元素个数）。
# print(count)


# #BMI计算器
# # 1. 输入姓名、身高(m)、体重(kg)
try:
    while True:
        name = input("请输入您的姓名：")
        h=float(input("请输入您的身高(m)："))
        w=float(input("请输入您的体重(kg)："))
    # 2. 计算BMI = 体重 / 身高^2
        BMI = w / h ** 2
        if BMI < 18.5:
            print(f"{name}您好，您的BMI指数是：", BMI,"体重过轻")
        elif BMI < 24:
            print(f"{name}您好，您的BMI指数是：", BMI,"正常范围")
        elif BMI < 28:
            print(f"{name}您好，您的BMI指数是：", BMI,"超重")
        else:
            print(f"{name}您好，您的BMI指数是：", BMI,"肥胖")
        s=input("是否继续(y/n):")
        if s=="y":
            continue
        elif s=="n":
            break
except Exception as e:
    print("请输入正常的数字",e)
finally:
    print("资源释放~")

# 3. 输出：XXX您好，您的BMI指数是：XX.X
# 4. 健康建议：
#    - < 18.5: 体重过轻
#    - 18.5-24: 正常范围
#    - 24-28: 超重
#    - >= 28: 肥胖
# 5. 处理输入非数字的情况（try-except）




