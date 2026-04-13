try:
    print("_____________")
    print(1/0)   #division by zero
    #print(a)    #name 'a' is not defined
except Exception as e:  #捕获所有异常
    print("程序运行出错了，请联系管理员，错误信息：",e)
finally:     #无论程序是否正常运行，finally代码块中的代码都会运行
    print("资源释放~")
