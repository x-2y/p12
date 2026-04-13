#基于match……case实现一个简易的计算器，可以实现 + - * /运算，用户输入需要运算的两个书及运算符之后，就可以进行计算
# num1=float(input("请输入第一个数："))
# num2=float(input("请输入第二个数："))
# oper=input("请输入运算符(+ - * /)：")
# match oper:
#     case "+":
#         print(f"{num1}+{num2}={num1+num2}")
#     case "-":
#         print(f"{num1}-{num2}={num1-num2}")
#     case "*":
#         print(f"{num1}*{num2}={num1*num2}")
#     case "/" if num2!=0:       #可以支持加条件判断
#         print(f"{num1}/{num2}={num1/num2}")
#     case _:
#         print("操作不支持！！")


#根据玩家输入的不同指令，控制游戏角色执行相应的动作
# stru=input("请输入指令：")
# match stru:
#     case "上"|"w"|"W":
#         print("角色向上移动")
#     case "下" | "s" | "S":
#         print("角色向下移动")
#     case "左" | "a" | "A":
#         print("角色向左移动")
#     case "右" | "d" | "D":
#         print("角色向右移动")
#     case "跳" | " ":
#         print("角色跳跃")
#     case "攻击" | "j" | "J":
#         print("角色发起攻击")
#     case "退出" | "esc" | "ESC":
#         print("角色退出游戏")


