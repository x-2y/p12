#元组基本操作 -tuple -->元素可以重复，有序，不可修改
#定义
# t1=(1,2,3,"i",2,True)
# print(t1)
# print(type(t1))    #<class 'tuple'>
#
# #索引访问
# print(t1[0])
# print(t1[-1])
#
# #切片
# print(t1[0:3:])    #(1, 2, 3)
#
# #count()统计元素个数
# print(t1.count(1))     #2
# #index()获取元素的索引(第一次出现的位置)
# print(t1.index(1))     #1
#
# #如果定义单元素的元组，单个元素之后需要加上逗号，比如(100,)
# t2=(2,)
# print(t2)              #(2,)


#组包操作
# t1=(5,7,9,10,23)
# t2=5,7,9,10,23    #系统会知道这个是元组
# print(t1)
# print(t2)
#
# #解包操作
# #基础解包(变量数量与容器的元素的个数一致)
# a,b,c,d,e=t1
# print(a,b,c,d,e)     #a=5 b=7 c=9 d=10 e=23
#
# #扩展解包(* 收集剩余的所有元素，封装列表list中)
# first,*other,last=t1
# print(first,other,last)  #first=5 other=[7, 9, 10] last=23
#
# *other,last=t1
# print(other,last)        #other=[5, 7, 9, 10] last=23



#案例1:现有两个变量，a,b将他们的值互换一下
# a=10
# b=20
# #组包
# t=a,b
# #解包
# b,a=t
# #也可以直接写成
# # b,a=a,b
#
# print(a,b)        #a=20,b=10
#
# #案例2:现有三个变量，a,b,c将他们的值分别赋给c,a,b
# a=100
# b=50
# c=20
# c,a,b=a,b,c
# print(a,b,c)
#


student=(
("S001","王琳",85,92,78),
("S002","李牧碗",89,98,70),
("S003","十三",78,96,65),
("S004","朝九",89,76,76),
("S005","潇洒",90,87,95),
("S006","小王",76,92,87),
("S007","遁地",87,92,78),
("S008","燕子",90,91,99),
("S009","月月",91,89,97),
("S010","小虎",87,94,70),
)
print("学号\t\t姓名\t\t语文\t\t数学\t\t英语\t\t总分\t\t平均分")
#1. 计算每个学生的总分、各科平均分,然后一并输出出来。
#方式1：
# for i in student:
#     totol=i[2]+i[3]+i[4]
#     avg=totol/3                                                          #{avg:.1f}-->保留一位小数
#     print(f"{i[0]} \t {i[1]} \t {i[2]} \t {i[3]} \t {i[4]} \t {totol} \t {avg:.1f}")

#方式2：元组解包
for id,name,chines,math,english in student:
    totol=chines+math+english
    avg=totol/3
    print(f"{id} \t {name} \t {chines} \t {math} \t {english} \t {totol} \t {avg:.1f}")

#2. 统计各科成绩的最低分、最高分、平均分,并输出。
#2.1获取到各科成绩的列表
chinese_score=[i[2]for i in student]
math_score=[i[3]for i in student]
E_score=[i[4]for i in student]
#2.2统计各科成绩的最低分、最高分、平均分,并输出
print(f"语文最低分:{min(chinese_score)}语文最高分:{max(chinese_score)}语文平均分:{sum(chinese_score)/len(chinese_score)}")
print(f"数学最低分:{min(math_score)}数学最高分:{max(math_score)}数学平均分:{sum(math_score)/len(math_score)}")
print(f"英语最低分:{min(E_score)}英语最高分:{max(E_score)}英语平均分:{sum(E_score)/len(E_score)}")


#3. 查找成绩优秀(平均分大于90)的学生,并输出。
print("------优秀生列表------")
#方式1：
for i in student:
    avg=(i[2]+i[3]+i[4])/3
    if avg>=90:
        print(f"学号：{i[0]} 姓名：{i[1]} 平均分：{avg:.1f}")
# 方式2：元组解包
# for id, name, chines, math, english in student:
#     avg = (chines + math + english)/ 3
#     if avg>=90:
#         print(f"学号：{id} 姓名：{name} 平均分：{avg:.1f}")




