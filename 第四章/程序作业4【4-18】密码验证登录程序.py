users = {"张三": {"昵称": "豆丁", "密码": "123abc"},
         "王五": {"昵称": "苹果", "密码": "456def"}}

print("系统用户列表：")
for username, info in users.items():
    print(f"{username} (昵称: {info['昵称']})")

times = 3
t = 0

while t < times:
    username = input("\n请输入用户名：")
    if username not in users.keys():
        t += 1
        print(f"用户不存在，剩余尝试次数：{times - t}")
    else:
        break

while t < times and username in users:
    password = input("请输入密码：")
    user = users.get(username)
    if password == user["密码"]:
        print(f"\n登录成功！欢迎 {user['昵称']}")
        print("您的账户信息：")
        for key, value in user.items():
            print(f"{key}: {value}")
        break
    t += 1
    print(f"密码错误，剩余尝试次数：{times - t}")

if t >= times:
    print("\n账户已锁定，请稍后再试")