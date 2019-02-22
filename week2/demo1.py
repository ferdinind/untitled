# 要对手机号的号段进行判断，号段任意给出6个作为模拟号段即可.
# 判断手机号码是否是由数字组成的
phone=input("请输入手机号：")
var=[152,156,155,169,185]
h=""
try:
    int(phone)
    if (len(phone)==11):
        h=phone[0:3]
        bool=False
        for i in var:
            print(h)
            if (int(h)==(i)):
                bool=True
                break
        if (bool):
            print("手机号输入正确")
        else:
            print("手机号输入错误")
    else:
                print("手机号位数不对")
except ValueError:
    print("手机号只能是数字")

