#它是一种无序的，不可重复，可修改的数据容器
#定义集合
# s1={"a","b","c",1}
# print(s1)
#
# #定义空集合
# s2=set()
# print(s2)

#常见方法：
# s1={100,200,300,400,500,600}
# print(s1)
#
# #add():添加元素到集合
# s1.add(900)
# print(s1)
#
# #remove():移除指定元素
# s1.remove(200)
# print(s1)
#
# #pop():随即删除集合中的元素并返回
# num=s1.pop()
# print(num)
# print(s1)
#
# #clear():清空集合
# s1.clear()
# print(s1)               #set()
#
#
# #difference():求两个集合的差集(包含在第一个集合中，不在第二个集合里)
# s3={100,200,300,400,500,600}
# s2={"aaa","bbb","ccc",100}
# print(s3.difference(s2))        #{200, 300, 400, 500, 600}
#
# #union():两个集合的并集
# print(s3.union(s2))             #{'ccc', 'bbb', 100, 'aaa', 200, 300, 400, 500, 600}
#
# #intersection():两个集合的交集
# print(s3.intersection(s2))      #{100}



#选修足球学生名单
football_set={"王林","曾牛","徐立国","遁天","天运子","韩立","厉飞雨","乌丑","紫灵"}
#选修篮球学生名单
basketball_set={"张铁","墨居仁","王林","姜老道","曾牛","王蝉","韩立","天运子","李化元","厉飞雨","云露"}
#选修法语学生名单
french_set={"许木","王卓","十三","虎咆","姜老道","天运子","红蝶","厉飞雨","韩立","曾牛"}
#选修艺术学生名单
art_set={"遁天","天运子","韩立","虎咆","姜老道","紫灵"}

#1.找出同时选修法语和艺术的学生
#方式1：
print(french_set.intersection(art_set))

#方式2：
fa_set=french_set & art_set
print(fa_set)

#2.找出同时选修了所有四门课程的学生
#也可以用 &
print(art_set.intersection(basketball_set,football_set,french_set))

#3.找出选修了足球没选篮球的学生
#方法1：
print(football_set.difference(basketball_set))

#方法2：用减号 -
fb_set=football_set - basketball_set
print(fb_set)

#方法3：推导式
fb_set1={s for s in football_set if s not in basketball_set}
print(fb_set1)

#获取每一个学生选修的课程数量
#(1)获取到学生名单---并集(|)
all_student=football_set.union(basketball_set).union(french_set).union(art_set).union(football_set)
#all_student=football_set | basketball_set | french_set |art_set
print(all_student)

#(2)获取每一个学生选修的课程数量
all_list=[*football_set,*basketball_set,*french_set,*art_set]  #*解包操作
for s in all_student:
    print(f"{s}选修了{all_list.count(s)}门课程")













