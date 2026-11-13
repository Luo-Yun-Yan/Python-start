import random
import string
def gen_pwd(length:int=12):#(length:int=12)默认值
    chars=string.ascii_letters+string.digits
    return ''.join(random.choice(chars) for _ in range(length))
print(gen_pwd(12))#gen_pwd(12)实际值