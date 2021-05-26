#TempConvert.py
##eval() 函数用来执行一个字符串表达式，并返回表达式的值。

TempStr = input("请输入带有符号的温度值：")
if TempStr[-1] in ['F','f']:
    C = (eval(TempStr[0:-1])-32)/1.8
    print("转化后的温度是{:.2f}C".format(C))
elif TempStr[-1] in ['C','c']:
    F = 1.8*eval(TempStr[0:-1]) + 32
    print("转化后的温度是{:.2f}F".format(F))
else:
    print("输入格式错误")
