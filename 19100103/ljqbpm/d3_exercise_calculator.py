#加减乘除计算器

def get_number(i):#获取输入的数字
    print('请输入运算的第',i,end='')
    a = float(input(' 个数字'))
    return a

cal=input('请输入运算符（仅支持+、-、*、/）')
if cal=='+':
    print('运算结果为：',get_number(1)+get_number(2))
elif cal=='-':
    print('运算结果为：',get_number(1)-get_number(2))
elif cal=='*':
    print('运算结果为：',get_number(1)*get_number(2))
elif cal=='/':
    print('运算结果为：',get_number(1)/get_number(2))
else:
    print('输入错误')