# -------------------------------#全局变量：在函数外部或函数内部都是可以访问的------------------------------------------------
# num=100
#
# #定义函数
# def circle_area(radius):
#     #局部变量：只能在函数内部使用
#     pi=3.14159
#     area=pi*radius**2
#
#     global num
#     num=1000
#     print(num)
#
#     return area
#
# print(circle_area(5))
# print(num)



#--------------------------------------------位置参数，关键字参数---------------------------------------------------------
# def reg_stu(name,age,gender,city):
#     print(f"注册成功，姓名{name}，年龄{age}，性别{gender}，城市{city}")
#     return {"name":name,"age":age,"gender":gender,"city":city}
#
# #传参方式1：位置参数
# stu=reg_stu("张三",36,"女","上海")
# print(stu)
#
# #传参方式1：关键字参数
# stu=reg_stu(name="张三",age=36,gender="女",city="上海")
# print(stu)
#
# stu=reg_stu(age=36,name="张三",city="上海",gender="女")
# print(stu)
#
# #传参方式1：位置+关键字参数----->位置参数在前，关键字参数在后
# stu=reg_stu("张三",age=36,city="上海",gender="女")
# print(stu)



#--------------------------------------------------默认参数   默认值可以有多个---------------------------------------------
# def reg_stu(name,age,gender="男",city="北京"):
#     print(f"注册成功，姓名{name}，年龄{age}，性别{gender}，城市{city}")
#     return {"name":name,"age":age,"gender":gender,"city":city}
# print(reg_stu("lis",12))
# print(reg_stu("lis",12,city="上海"))
# print(reg_stu("lis",12,"女"))




# #-------------------------不定长参数(位置参数 *args-->元组)-----------------------------------------------------------
# def calc_data(*args):
#     min_data=min(args)
#     max_data=max(args)
#     avg_data=sum(args)/len(args)
#     return min_data,max_data,avg_data
# print(calc_data(1,2,3,4,5,6,7,8,9))
# print(calc_data(1,2,3,4,5,6,7,8,9,32,11))

#-------------------------不定长参数(关键字参数 **kwargs-->字典)-----------------------------------------------------------
# def calc_data(*args,**kwargs):
#     """
#
#     :param args: 不定长位置参数，需要计算的这批数据
#     :param kwargs: 不定长关键字参数
#         round:保留的小数位个数
#         print:是否打印输出
#     :return: 最小值，最大值，平均值
#     """
#     min_data=min(args)
#     max_data=max(args)
#     avg_data=sum(args)/len(args)
#
#     if kwargs.get('round') is not None:
#         avg_data=round(avg_data,kwargs.get('round'))
#     if kwargs.get('print'):
#         print(f"最小值：{min_data},最大值:{max_data},平均值：{avg_data}")
#
#     return min_data,max_data,avg_data
# print(calc_data(1,2,3,4,5,6,7,8,9))
# print(calc_data(1,2,3,4,5,6,7,8,9,32,11,round=3,print=True))
# print(calc_data(1,2,3,4,5,6,7,8,9,32,11,round=3))


