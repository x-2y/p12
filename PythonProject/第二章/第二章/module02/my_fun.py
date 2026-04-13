#__all__=[] 指定from...import * 导入的是哪些功能，如果没有__all__则代表所有功能
# __all__=["log_separator1","NAME"]
#常量(不会发生变化的数据；常量的名称为全部大写)
PI=3.1415926
NAME="李玉"

#函数
def log_separator1():
    print("- "*30 )         #30个-
def log_separator2():
    print("我是my_fun中调用过的函数")
def log_separator3():
    print("# "*30 )
def log_separator4():
    print("* "*30 )


#测试函数
#__name__:python中内置变量，表示的当前模块的名字(直接运行当前的模块，__name__的值为"__main__"；
#                                          当该模块被导入时，__name__的值就是模块名。(如果my_fun文件被main文件导入的话，__name__="my_fun") )
#用处在于
if __name__=='__main__':   #如果相等说明是在当前文件中执行，如果等于‘my_fun就说明在其他文件中了’
    log_separator2()       #也就是说执行当前文件，则会执行该行代码；如果被当成模块导入，这行代码就不执行

