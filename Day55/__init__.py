# 1. 通过用户输入数字，计算阶乘。（30分）
try:
    var=int(input("请输入一个数字来计算它的阶乘"))
    i=1
    sum=0;
    for i in range(var):
        if i!=var:
            sum+=i*(i+1)
        else:
            break
    print(sum)
except ValueError:
    print("阶乘需要数字来求")




# 3. 将一个列表的数据复制到另一个列表中，并反向排序输出。（40分）
