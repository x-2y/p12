#列表操作
#定义列表 -list
# s=[1,42,"ss",True,"s",89]
# print(type(s))              #<class 'list'>
#
# #访问列表元素
# print(s[0])                 #1 正向索引
# print(s[-6])                #1 反向索引
#
# #修改
# s[2]=77
# print(s)
#
# #删除
# del s[2]
# print(s)


#列表list-切片
# s=[1,42,"ss",True,"s",89]
# print(s[0:5:1])             #[1, 42, 'ss', True, 's']
# print(s[:5:1])              #[1, 42, 'ss', True, 's']
# print(s[:5:])               #[1, 42, 'ss', True, 's']
# print(s[:5])                #[1, 42, 'ss', True, 's']
# print(s[::-1])              #[89, 's', True, 'ss', 42, 1]
# print(s[1:-1:1])            #[42, 'ss', True, 's']


#list-方法
# s=[89, 's', True, 'ss', 42, 1]
#
# #append():在列表尾部追加元素
# s.append("yyy")
# print(s)
#
# #insert():在指定索引之前，插入元素
# s.insert(1,56)
# print(s)
#
# #remove():删除列表中第一个匹配到的值
# s.remove(1)
# print(s)
#
# #pop():删除列表中指定索引位置的元素，如果未指定，默认删除最后一个
# s.pop(2)
# print(s)
#
# s1=[89, 56, 32, 42, 1, 76]
# #sort():排序
# s1.sort()                   #[1, 32, 42, 56, 76, 89]
# print(s1)
#
# #reverse():反转列表元素
# s.reverse()
# print(s)



#案例1，将用户输入的10个数字，存储到一个列表中，并将列表中的数字进行排序，输出其中最小值最大值平均值
# i=0
# s=[]
# while i<10:
#     n=int(input("请输入数字："))
#     s.append(n)
#     i+=1
# print("数字列表：",s)
# s.sort()
# print("排序后的数字列表：",s)
# print("最小值：",s[0])
# print("最大值：",s[-1])
# print("平均值：",sum(s)/len(s))     #sum()求和;len()获取元素的个数(列表的长度)


#案例2，合并两个列表中的元素，并对合并后的元素去重操作
# list1=[1,2,3,11,22,43,23,2,1]
# list2=[18,21,31,1,2,233,26,22]
#
# #方法1：
# # for i in list2:
# #     list1.append(i)
# # print("合并后的原始列表：",list1)
#
# #方法2：
# #* 解包：将列表这一类容器解开成一个一个独立的元素
# #组包：将多个值合并到一个容器
# # list3=[*list1,*list2]
# # print("合并后的原始列表：",list3)
#
# #方法3：
# list3=list1+list2
# print("合并后的原始列表：",list3)
#
# new_list=[]
# for i in list1:
#     #判断new_list中是否存在i元素，如果不存在在添加
#     if i not in new_list:     #in用于判断元素是否存在列表中
#         new_list.append(i)
# print("去重后的原始列表：",new_list)



#案例3，生成1-20的平方的一个列表
#方法1：
# list=[]
# for i in range(1,21):
#     list.append(i**2)
# print(list)

#方法2：列表推导式-->就是一个可以快速生成一个列表的方法  格式：[要插入的值 for i in 序列/列表 if 条件] (这里的if条件可以不写)
# list=[i**2 for i in range(1,21)]
# print(list)



# #案例4：从一个数字列表中提取所有的偶数，并计算他的平方，组成一个新列表
# list=[2,11,23,32,78,90,54,31,87]
# list1=[]
# #方法1
# for i in list:
#     if i%2==0:
#         list1.append(i**2)
# print(list1)          #[4, 1024, 6084, 8100, 2916]
# #方法2
# list2=[i**2 for i in list if i %2==0]
# print(list2)          #[4, 1024, 6084, 8100, 2916]


# 使用列表存储商品
store=[]
# 程序循环显示菜单：1.添加商品 2.删除商品 3.查看购物车 4.结算退出
while True:
    print("\n======购物车======")
    print("1.添加商品")
    print("2.删除商品")
    print("3.查看购物车")
    print("4.结算推出")
    choice=input("请输入你的选择：")

    # 添加商品时输入商品名
    if choice=="1":
        item=input("请输入添加的物品名称：")
        store.append(item)
        print(f"{item}添加成功！")
    # 删除商品时展示当前商品编号，输入编号删除，处理索引越界
    elif choice=="2":
        if len(store)==0:
            print("购物车为空，不能删除")
        else:
            for i in range(len(store)):
                print(f"{i+1}.{store[i]}")
            try:
                num=int(input("请输入你要删除的商品编号："))
                if 1<=num<=len(store):
                    item=store.pop(num-1)
                    print(f"{item}已成功删除！")
                else:
                    print("编号超出范围!")
            except Exception as e:
                print(e)
    elif choice=="3":
        if len(store)==0:
            print("购物车为空")
        else:
            for i in range(len(store)):
                print(f"{i+1}.{store[i]}")
    # 结算时显示购物车商品列表和总件数
    elif choice=="4":
        print(f"商品总数为：{len(store)}")
        for i in range(len(store)):
            print(f"{i+1}.{store[i]}")
        break














