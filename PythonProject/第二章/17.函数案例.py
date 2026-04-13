#案例1：定义一个函数：根据传入的底和高计算三角形面积的函数
# def s_sjx(d,h):
#     """
#     定义一个函数：根据传入的底和高计算三角形面积的函数
#     :param d:三角形的底
#     :param h:三角形的高
#     :return:三角形的面积
#     """
#     s=d*h/2
#     return s
# print(s_sjx(2,3))

#案例2：定义一个函数：计算传入的字符串中元音字母的个数（aeiouAEIOU）
# def count_aeiou(s):
#     """
#     统计字符串中元音字母的个数
#     :param s: 字符串
#     :return: 元素个数
#     """
#     num=0
#     for i in s:
#         if i in "aeiouAEIOU":
#             num+=1
#     return num
# print(count_aeiou("aaaijf"))


#案例3：定义一个函数：计算传入班级学员高考成绩列表的最高/低分/平均分
# def cal_score(score):
#     """
#     计算传入班级学员高考成绩列表的最高/低分/平均分
#     :param score: 成绩列表
#     :return: 列表的最高/低分/平均分
#     """
#     max_score = max(score)
#     min_score = min(score)
#     avg_score = round(sum(score)/len(score),1)
#     return max_score,min_score,avg_score
# s_list=[654,555,340,548,590,632]
# max_score,min_score,avg_score=cal_score(s_list)
# print(max_score,min_score,avg_score )


#定义一个函数，根据传入的分数，计算对应的分数等级并返回
# def dj(score):
#     if score>=90:
#         print("A")
#     elif score>=75:
#         print("B")
#     elif score>=60:
#         print("C")
#     elif score<65:
#         print("D")
# dj(89)

#定义一个函数，用于判断一个字符串是否是回文串，返回bool值
#把字符串反转，如果还跟之前一样就是回文数 abcba
# def hws(s):
#     if str(s)==str(s)[::-1]:
#         print(f"{s}是回文数")
#     else:
#         print(f"{s}不是回文数")
# hws(122211)

#定义一个函数，实现时间转换功能，将传入的秒转换为时分秒
# def time_sfm(s):
#     h=s//3600
#     m=(s%3600)//60
#     s=s%60
#     print(f'{h}时:{m}分:{s}秒')
# time_sfm(3665)


# 定义一个函数：根据传入的三角形三个边的边长，判断三角形的类型
# def triangle(c,w,h):
#     """
#
#     :param c: 三角形长
#     :param w: 三角形宽
#     :param h: 三角形高
#     :return: 三角形类型
#     """
#     x,y,z=sorted([c,w,h])    #排序
#     if x+y<=z:
#         print("不能构成三角形！")
#     else:
#         if x==y==z:
#             print("等边三角形！")
#         elif x==z or x==y or y==z:
#             if x**2+y**2==z**2:
#                 print("等腰直角三角形！")
#             else:
#                 print("等腰三角形！")
#         elif x**2+y**2==z**2:
#                 print("直角三角形！")
#         else:
#             print("普通三角形！")
# triangle(2,3,1)

