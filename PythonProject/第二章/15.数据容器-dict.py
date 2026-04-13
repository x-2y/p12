#字典  --key不能重复(如果重复，后面的值会覆盖前面的值)，key必须是不可变类型(str,int,float,tuple)
#定义字典
# dict={"潇洒":680,"李玉":682,"小燕":689,"月月":685}
# print(dict)

# 访问
# print(dict["月月"])
# dict["月月"]=700   #修改value
# print(dict)

#----------字典 常见操作----------
# dict={"王五":890,"李四":789,"赵六":678,"小玉":888}
# print(dict)
#
# #添加
# dict["燕子"]=999
# print(dict)
#
# #修改
# dict["燕子"]=99
# print(dict)
#
# #查询
# print(dict["小玉"])           #888
# print(dict.get("小玉"))       #888
#
# print(dict.keys())             #获取所有key
# #dict_keys(['王五', '李四', '赵六', '小玉', '燕子'])
# print(dict.values())           #获取所有value
# #dict_values([890, 789, 678, 888, 99])
# print(dict.items())            #获取所有键值对 key:value
# #dict_items([('王五', 890), ('李四', 789), ('赵六', 678), ('小玉', 888)

# #删除
# score=dict.pop("王五")
# print(score)
# print(dict)
#
# del dict["李四"]
# print(dict)

#遍历
# for k in dict.keys():
#     print(f"{k}:{dict[k]}")
#
# for i in dict.items():
#     print(f"{i[0]}:{i[1]}")         #dict_items([('王五', 890), ('李四', 789), ('赵六', 678), ('小玉', 888)因为是元组
#
# for i,j in dict.items():           #解包
#     print(f"{i}:{j}")


# shopping_cart={}
# menu="""
# ##########购物车系统##########
# #        1.添加购物车        #
# #        2.修改购物车        #
# #        3.删除购物车        #
# #        4.查询购物车        #
# #        5.退出购物车        #
# """#Alt+Shift列选中
# print("欢迎使用购物车管理系统~")
#
# while True:
#     print(menu)
#     choice=input("输入你想进行的操作(1-5)：")
#     #1.添加购物车，录入商品名称，价格，数量，保存到购物车
#     match choice:
#         case "1":
#             name = input("请输入商品的名称：")
#             if name in shopping_cart.keys():
#                 print("该商品已经存在，请重新选择~")
#             else:
#                 price = float(input("请输入商品的价格："))
#                 num = int(input("请输入商品的数量："))
#                 # shopping_cart={"shangpin":{"price":jg,"num":sl},}
#                 shopping_cart[name] = {"price": price, "num": num}
#                 print("添加成功！")
#         case "2":
#             # 2.修改购物车，输入要修改的商品名称，价格，数量，修改该商品信息
#             name = input("请输入要修改商品的名称：")
#             if name not in shopping_cart.keys():
#                 print("商品不存在，请重新选择~")
#             else:
#                 price = float(input("请输入商品的新价格："))
#                 num = int(input("请输入商品的新数量："))
#                 shopping_cart[name] = {"price": price, "num": num}
#                 print("修改成功！")
#
#         case "3":
#             # 3.删除购物车，输入要删除的购物车名称，根据名称删除购物车中的商品
#             name = input("请输入商品的名称：")
#             if name not in shopping_cart.keys():
#                 print("商品不存在，请重新选择~")
#             else:
#                 del shopping_cart[name]
#                 print("删除成功！")
#
#         case "4":
#             # 4.查询购物车，格式为“商品名称：xxx，商品价格：xxx，商品数量：xxx”
#             for k in shopping_cart.keys():
#                 sp = shopping_cart[k]  # {"price":jg,"num":sl}
#                 print(f"商品名称：{k},商品价格：{sp["price"]},商品数量：{sp["num"]}")
#         case "5":
#             # 5.退出购物车
#             print("bye~")
#             break
#         case _:
#             print("非法操作，不支持！")






# 联系人管理系统
# contacts={}
# # 功能：
# while True:
#     print("1.添加联系人")
#     print("2.删除联系人")
#     print("3.修改联系人")
#     print("4.查询联系人")
#     print("5.显示所有联系人")
#     print("6.退出程序")
#     choice=input("请输入你的选择：")
# # 1. 添加联系人（姓名、电话）
#     if choice=="1":
#         name = input("请输入名字：")
#         if name not in contacts:
#             phone = input("请输入电话：")
#             contacts[name] = phone
#             print("添加成功！")
#         else:
#             print(f"{name}已存在！")
# # 2. 删除联系人（根据姓名）
#     elif choice=="2":
#         try:
#             name=input("请输入要删除的名字：")
#             if name not in contacts:
#                 print("没有该联系人")
#             else:
#                 del contacts[name]
#                 print(f"{name}删除成功！")
#         except Exception as e:
#             print(e)
#
#
# # 3. 修改联系人电话
#     elif choice=="3":
#         name=input("请输入要修改电话的名字:")
#         new_phone=input("请输入修改后的电话:")
#         if name not in contacts:
#             print("没有该联系人")
#         else:
#             contacts[name] = new_phone
#
# # 4. 查询联系人（根据姓名显示电话）
#     elif choice=="4":
#         name=input("请输入要查询的联系人的姓名：")
#         if name not in contacts:
#             print("没有该联系人")
#         else:
#             print(contacts[name])
#
# # 5. 显示所有联系人
#     elif choice=="5":
#         if len(contacts)==0:
#             print("联系人为空！")
#         else:
#             for name,phone in contacts.items():
#                 print(f"{name}:{phone}")
# # 6. 退出程序
#     elif choice=="6":
#         print("bye~")
#         break
#     else:
#         print("无效的操作，请重新输入！")
# #



student={}
while True:
    print("1.添加学生信息")
    print("2.修改学生信息")
    print("3.删除学生信息")
    print("4.查询学生信息")
    print("5.列出学生信息")
    print("6.统计班级成绩")
    print("7.退出系统")
    choice=input("请输入你的选择(1-7)：")
#1. 添加学生信息:根据提示录入学生姓名、语文、数学、英语成绩,录入完成保存到系统中。
    if choice == "1":
        name = input("请输入姓名：")
        if name not in student:
            while True:
                chinese = float(input("请输入语文成绩："))
                if 0 <= chinese <= 100:
                    math = float(input("请输入数学成绩："))
                    if 0 <= math <= 100:
                        english = float(input("请输入英语成绩："))
                        if 0 <= english <= 100:
                            break
                        else:
                            print("请输入1-100之间的数")
                    else:
                        print("请输入1-100之间的数")
                else:
                    print("请输入1-100之间的数")
            student[name] = {"语文": chinese, "数学": math, "英语": english}
        else:
            print("该学生已存在，请重新输入！")


    # 2. 修改学生信息:要求输入要修改的学生姓名,然后再提示输入语文、数学、英语成绩,输入完成后修改学员信息。
    elif choice=="2":
        name=input("请输入要修改的学生姓名：")
        if name not in student:
            print("没有该学生")
        else:
            while True:
                new_chinese = float(input("请输入新的语文成绩(0-100)："))
                if 0 >new_chinese or new_chinese > 100:
                    print("请输入0-100之间的数")
                    continue
                new_math = float(input("请输入新的数学成绩(0-100)："))
                if 0 >new_math or new_math > 100:
                    print("请输入0-100之间的数")
                    continue
                new_english = float(input("请输入新的英语成绩(0-100)："))
                if 0 >new_english or new_english > 100:
                    print("请输入0-100之间的数")
                    continue
                student[name] = {"语文": new_chinese, "数学": new_math, "英语": new_english}
                print("修改成功！")
                break


# 3. 删除学生信息:要求输入要删除的学生姓名,根据姓名删除学生信息。
    elif choice=="3":
        name=input("请输入要删除的学生姓名：")
        if name not in student:
            print("没有该学生")
        else:
            del student[name]
            print("删除成功！")

# 4. 查询学生信息:要求输入要查询的学生姓名,根据姓名查询学生信息并输出。
    elif choice=="4":
        name=input("请输入要查询的学生姓名：")
        if name not in student:
            print("没有该学生")
        else:
            print(f"{name}\t语文：{student[name]["语文"]}数学：{student[name]["数学"]}英语：{student[name]["英语"]}")


# 5. 列出所有学生:遍历所有学生信息并输出。
    elif choice=="5":
        if len(student)==0:
            print("没有学生信息")
        else:
            for name,info in student.items():
                print(f"{name}\t语文：{info["语文"]}数学：{info["数学"]}英语：{info["英语"]}")

# 6. 统计班级成绩:统计班级语文、数学、英语成绩的最高分、最低分、平均分,以及语文、数学、英语最高分和最低分的学
# 员姓名。

    elif choice=="6":
        #统计班级语文、数学、英语成绩的最高分、最低分、平均分
        chinese_list=[]
        math_list=[]
        english_list=[]
        for c in student.values():
            chinese_list.append(c["语文"])
            math_list.append(c["数学"])
            english_list.append(c["英语"])

        max_c = max(chinese_list)
        min_c = min(chinese_list)
        avg_c = (sum(chinese_list)) / len(chinese_list)
        max_c_name = [name for name, score in student.items() if score["语文"] == max_c]
        min_c_name = [name for name, score in student.items() if score["语文"] == min_c]
        print(f"语文最高分是:{max_c}\t语文最低分是:{min_c}\t语文平均分是:{avg_c}")
        print(f"语文最高分:{max_c_name}\t语文最低分:{min_c_name}")

        max_m = max(math_list)
        min_m = min(math_list)
        avg_m = (sum(math_list)) / len(math_list)
        max_m_name = [name for name, score in student.items() if score["数学"] == max_m]
        min_m_name = [name for name, score in student.items() if score["数学"] == min_m]
        print(f"数学最高分是:{max_m}\t数学最低分是:{min_m}\t数学平均分是:{avg_m}")
        print(f"数学最高分:{max_m_name}\t数学最低分:{min_m_name}")

        max_e = max(english_list)
        min_e = min(english_list)
        avg_e = (sum(english_list)) / len(english_list)
        max_e_name = [name for name, score in student.items() if score["英语"] == max_e]
        min_e_name = [name for name, score in student.items() if score["英语"] == min_e]
        print(f"英语最高分是:{max_e}\t英语最低分是:{min_e}\t英语平均分是:{avg_e}")
        print(f"英语最高分:{max_e_name}\t英语最低分:{min_e_name}")


    # 7. 退出系统。
    elif choice=="7":
        print("bye~")
        break
    else:
        print("无效的操作，请重新输入!")




