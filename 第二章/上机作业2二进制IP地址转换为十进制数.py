#基础版
# bin_str=input('请输入32位二进制IP地址(由0和1组成):')
# p1=int(bin_str[0:8],2)
# p2=int(bin_str[8:16],2)
# p3=int(bin_str[16:24],2)
# p4=int(bin_str[24:32],2)
# ip='.'.join([str(p1),str(p2),str(p3),str(p4)])
# print(ip)
# print()
#高级版
# bin_str=input('请输入32位二进制IP地址(由0和1组成):')
# ip='.'.join([str(int(bin_str[i:i+8],2)) for i in range(0,32,8)])
# print(ip)
#超级版
raw_input=input('请输入32位二进制IP地址(由0和1组成,建议每4位用空格隔开):')
#bin_str=raw_input.replace(' ','').strip()
bin_str=''.join(raw_input.split())
if len(bin_str)!=32:
    print(f'错误:输入长度是{len(bin_str)}位,请检查是否输漏或混入其它符号!')
else:
    ip = '.'.join([str(int(bin_str[i:i + 8], 2)) for i in range(0, 32, 8)])
    print(f'转换后的IP地址是:{ip}')