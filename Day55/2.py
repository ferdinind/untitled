# 2. 判断101-200之间有多少个素数，并输出所有素数。
# 程序分析：判断素数的方法：用一个数分别去除2到sqrt(这个数)，
# 如果能被整除，则表明此数不是素数，反之是素数。（30分）

for i in range(101,200):
    if i%2!=0 and i%3!=0 and i%5!=0:
        print(i)
    # print("这个是i的值",i)
    # for j in (2,i):
    #     print("这个是j的值",j)
    #     if i%j!=0:
    #         print(i)
    #     else:
    #         # continue
