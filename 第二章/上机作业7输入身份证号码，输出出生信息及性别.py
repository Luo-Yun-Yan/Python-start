def parse_id_card():
    id_num = input('请输入18位身份证号码: ')
    
    # 简单校验长度
    if len(id_num) != 18:
        print('身份证号码必须为18位')
        return

    # 提取出生年月日 (索引 6 到 13)
    year, month, day = id_num[6:10], id_num[10:12], id_num[12:14]
    
    # 提取第17位判断性别 (索引16)，奇数为男，偶数为女
    is_male = int(id_num[16]) % 2 != 0 
    
    print(f'--- 信息解析结果 ---')
    print(f'出生日期: {year}年{month}月{day}日')
    print(f'性别: {"男" if is_male else "女"}')

parse_id_card()