#函数的参数是函数
#加
# def add(x,y):
#     return x+y
#
# #减
# def sub(x,y):
#     return x-y
#
#
# #乘
# def mul(x,y):
#     return x*y
#
# #除
# def div(x,y):
#     return x/y
#
# #计算
# def calc(x,y,oper):
#     return oper(x,y)
# print(calc(2,3,add))  #传递的是函数的运算逻辑


#---------------------------匿名函数-------------------------------------------
# def out_line():
#     print('------')
# out_line()
#
# out_line1=lambda :print('----')
# out_line1()
#
#
# def add(x,y):
#     return x+y
# print(add(3,4))
#
# add1=lambda x,y:x+y
# print(add1(3,4))



#按字符个数排序
# data_list=["c++","as","java","javascript"]
# print(data_list)
# data_list.sort()
# print(data_list)
# data_list.sort(key=lambda i:len(i),reverse=True)  #reverse是sort函数中用来排序的，reverse=True从大到小，reverse=False从小到大，默认不写就是false   key是sort函数中用来获取值的
# print(data_list)


#-----------------------递归------------------------------------------------------
#案例1：计算n的阶乘
#递归调用(先层层递进，在逐层回归)：指的是在函数中自己调用自己的情况(得有终点)
# def jc(n):
#     if n==1:
#         return 1
#     else:
#         return n*jc(n-1)
#
# print(jc(10))


# 案例2:定义一个用于根据传入的一批商品信息(商品名、价格、数量)、优惠(优惠券、积分抵扣)、运费信息计算订单的总金额的函数。
# 具体规则如下:
# 1. 优惠券需要商品金额满5000才可以使用,且优惠券金额不能超过商品总价。
# 2. 积分抵扣需要商品总金额满5000才可以使用,100积分抵扣1元(且抵扣金额不能超过商品总价,积分只能整百抵扣)。
# def calc_order_cost(*args,coupon=0,score=0,express=0):
#     """
#     根据传入的一批商品信息(商品名、价格、数量)、优惠(优惠券、积分抵扣)、运费信息计算订单的总金额
#     :param args: 商品信息(商品名，价格，数量)
#     :param coupon: 优惠券
#     :param score:积分
#     :param express:运费
#     :return:订单的总金额
#     """
#     #订单的总金额=商品总金额-优惠券-积分抵扣+运费
#     #1.计算商品总金额
#     total=[goods[1]*goods[2] for goods in args]
#     total_cost=sum(total)
#
#     #2.扣减优惠券
#     if total_cost>=5000 and coupon<=total_cost:
#         total_cost-=coupon
#     #3.扣减积分抵扣
#     if total_cost>=5000 and score//100<=total_cost:
#         total_cost-=score//100
#     #4.添加运费
#     total_cost+=express
#     return total_cost
#
# total=calc_order_cost(("鼠标",188,2),("键盘",388,1),("手机",3999,1),coupon=10,score=4000,express=9.99)
# print(total)
# total=calc_order_cost(("鼠标",188,2),("键盘",388,1),("手机",6999,1),coupon=10,score=4000,express=9.99)
# print(total)




#购物车系统（函数时重构版）
cart=[]
def show_menu():
    print("\n==========购物车系统=============")
    print("1.添加商品")
    print("2.删除商品")
    print("3.查看购物车")
    print("4.结算并退出")
    print("==================================")

def add_item():
    global cart
    item=input("请输入商品名称")
    cart.append(item)
    print("添加成功！")
def remove_item():
    global cart
    if len(cart)==0:
        print("购物车是空的")
        return
    print("\n当前购物车商品：")
    for i in range(len(cart)):
        print(f"{i+1}:{cart[i]}")

    try:
        num=int(input("请输入要删除的商品编号："))
        if 1<=num<=len(cart):
            removed=cart.pop(num-1)
            print(f"{removed}已删除")
        else:
            print("编号超出范围")
    except ValueError:
        print("请输入数字编号!")

def view_cart():
    global cart
    if len(cart)==0:
        print("购物车为空！")
    else:
        print("\n购物车列表：")
        for i in range(len(cart)):
            print(f"{i+1}:{cart[i]}")
        print(f"共计{len(cart)}件商品")

def check_cart():
    global cart
    if len(cart)==0:
        print("购物车为空！")
        return False
    else:
        for i in range(len(cart)):
            print(f"{i+1}:{cart[i]}")
        print(f"共计{len(cart)}件商品")
        return True

def main():
    while True:
        show_menu()
        choice=input("请输入您的选择:")
        if choice=="1":
            add_item()
        elif choice=="2":
            remove_item()
        elif choice=="3":
            view_cart()
        elif choice=="4":
            if check_cart():
                break
        else:
            print("输入错误，请重新输入")
main()






