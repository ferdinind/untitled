var=[153,156,125,136]
head=""
ph=input("请输入一个手机号")
try:
    int(ph)
    if len(ph)==11:
        bool=False
        print(ph)
        head=ph[0:3]

        for i in var:
            if int(head)==i:
                bool=True
                break
        if bool:
                print("输入正确")
        else:
                print("输入错误")
    else:
        print("不够11位数字")
except ValueError:
    print("手机号只可以是数字")