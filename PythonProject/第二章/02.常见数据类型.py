# #常见数据类型--->type()
# print("hello")
# print(type(23))    #<class 'int'>
# print(type(-2))    #<class 'int'>
# print(type(0.3))   #<class 'float'>
# print(type(True))  #<class 'bool'>
# print(type(None))  #<class 'NoneType'>
# num=100
# print(num)
# print(type(num))   #<class 'int'>
#
# #常见数据类型-->isinstance(数据，类型)-->bool值-->判定数据是否是指定的类型，如果是True，否则False
# print(isinstance(2,int))     #True
# print(isinstance(num,str))   #False


#字符串
# s1="hell'o"  #双引号 hell'o
# s2='hi,"n'    #单引号 hi,"n
# s3="""
# hello:
#     我是人
# """       #三引号
# print(s1)
# print(s2)
# print(s3)
# print(type(s1))
# print(type(s2))
# print(type(s3))


#定义字符串 -->It's very good
#转义字符 \'  \"  \n  \t
#msg='It's very good'  #×
# msg='It\'s very good'
# print(msg)
# msg2="It's very good"
# print(msg2)
# msg3="hello就是\"您好"
# print(msg3)
# msg4='hello就是"您好"'
# print(msg4)
# print("\t欢迎大家\n\t谢谢大家")


#字符串拼接(只能拼接字符串，非字符串需转换成字符串)
# s1="人生苦短""我用python"  ",ok"
# s2="人生苦短"+"我用python"
# print(s2)             #人生苦短我用python
# print(s1)             #人生苦短我用python,ok
# msg1="人生苦短"
# msg2="我用python"
# print(msg1,msg2)      #人生苦短 我用python
# print(msg1+","+msg2)  #人生苦短,我用python

#str(int)将int类型的数据转为字符串
name="yy"
age=20
major="软件工程"
hobby="撸狗"
print("大家好，我是"+name+",今年"+str(age)+",学习的专业是"+major)
print("大家好，我的爱好是%s"%hobby)  #占位符
print("大家好，我是%s,今年%s,学习的专业是%s"%(name,age,major))  #占位符
print("%i"%age)
s1="闫鸿燕"
print(f"我是{s1}")
print(f"大家好，我是{name}，今年{age}，学习的专业是{major}")