num = input()
for i in num:#len用来判断字符串的长度，range表示循环的范围
    if num[i] in ['0']:
        print("零", end="")#end就表示print将如何结束，默认为end="\n"（换行）
    elif num[i] in ['1']:
        print("一", end="")
    elif num[i] in ['2']:
        print("二", end="")
    elif num[i] in ['3']:
        print("三", end="")
    elif num[i] in ['4']:
        print("四", end="")
    elif num[i] in ['5']:
        print("五", end="")
    elif num[i] in ['6']:
        print("六", end="")
    elif num[i] in ['7']:
        print("七", end="")
    elif num[i] in ['8']:
        print("八", end="")
    else:
        print("九", end="")