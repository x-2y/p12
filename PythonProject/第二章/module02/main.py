import my_fun                            #运行这条语句的时候会直接把里面的代码走一遍

print(my_fun.NAME)
print(my_fun.PI)
print(my_fun.log_separator2())
print(my_fun.log_separator3())


# from my_fun import *    #因为my_fun有__all__所以，只能使用NAME和log_separator1()这俩功能
# print(NAME)
# log_separator1()