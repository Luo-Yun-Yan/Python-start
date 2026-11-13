alpha_count=0
digit_count=0
other_count=0
text=input('请输入一段字符串:')
for char in text:
    if char.isalpha()and char.isascii():
        alpha_count+=1
    elif char.isdigit():
        digit_count+=1
    else:
        other_count+=1
print(f'英文字母个数:{alpha_count}')
print(f'数字个数:{digit_count}')
print(f'其他字符个数:{other_count}')