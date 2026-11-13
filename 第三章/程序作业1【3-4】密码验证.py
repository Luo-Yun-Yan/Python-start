#正确密码:password123
correct_psw='password123'
i=0
while i<3:
    use_input = input('请输入密码:')
    if use_input==correct_psw:
        print(f'{chr(9989)}验证成功!欢迎进入系统。')
        break
    else:
        print(f'{chr(10060)}密码错误!请重试。')
    i=i+1
else:
    print('错误次数过多，账号已锁定。')