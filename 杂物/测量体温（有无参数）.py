# 无参数
# def check_temperature():
#     temp=eval(input('请输入体温:'))
#     print('体温'+('正常'if 36<=temp<=37.5 else'异常'))
# check_temperature()
# print()
# 有参数
def check_temperature(temp):
    return('体温'+('正常'if 36<=temp<=37.5 else'异常'))
temp = eval(input('请输入体温:'))
print(check_temperature(temp))
