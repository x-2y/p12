# #注意：函数定义的时候并不会执行，只有在调用函数的时候，函数体的逻辑才会执行；函数必须先定义后调用
# #函数定义：
# def out_line():
#     print("____________________________")
#
# #函数调用
# out_line()
import math


#函数的参数与返回值
#函数1：计算圆的面积
# def circle_area(r):
#     s=3.14*r**2
#     print(s)
#
# circle_area(2)

#长方形面积
# def rectangle_area(n,m):
#     """
#     该函数用于根据长方形的长和宽来计算长方形的面积      --->函数的说明文档
#     :param n: 长方形的长
#     :param m: 长方形的宽
#     :return: 长方形的面积
#     """
#     s=n*m
#     return s
# print(rectangle_area(3,4))

#函数3：计算圆的面积周长，如果返回值有多个，多个返回值之间逗号分割，多个返回值会封装到元组之中
# def circle_area_len(r):
#     return round(3.14*r**2,1),round(2*3.14*r,1)  #round( ,1)保留一位小数
# print(circle_area_len(10))


#函数的嵌套调用
# def function_a():
#     print("a...before")
#     function_b()
#     print("a...after")
# def function_b():
#     print("b...before")
#     function_c()
#     print("b...after")
# def function_c():
#     print("c...before")
#     print("c...after")
# function_a()





