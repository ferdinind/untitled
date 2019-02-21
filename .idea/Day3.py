import string
# var1=input("请输入第一个人的生日")
# var2=input("请输入第二个人的生日")
# list1=var1.split("-");
# list2=var2.split("-");
# if int(list1[0])>int(list2[0]):
#     print("第一个年龄大")
# elif int(list1[0])<int(list2[0]):
#     print("第二个年龄大")
# else:
#     if int(list1[1])>int(list2[1]):
#         print("第一个年龄大")
#     elif int(list1[1]) < int(list2[1]):
#         print("第二个年龄大")
#     else:
#         if int(list1[2]) > int(list2[2]):
#             print("第一个年龄大")
#         elif int(list1[2]) < int(list2[2]):
#             print("第二个年龄大")
#         else:
#             print("两个一样大")
# print(list1)
# print(list2)
# import random
# var1=int(random.choice(range(0,10)))
# var2=[]
# for i in range(10):
#     var2+=str(random.choice(range(0,10)))
#     if int(var2[i])==var1:
#         print("找到了个相同数%d"%var1)
# print("随机生成的序列:",var2)
# print("随机生成的数字:",var1)
# name=input("输入用户姓名")
# sex=input("输入性别")
# if sex=='女':
#     print("%s女士你好"%name)
# else:
#     print("%s先生你好"%name)
# s=[1,2,3,5,8,6]
# print(s.reverse())
# s1=[1,2,3,5,8,6]
# s2=[]
# for i in str(s).__len__():
#     s2+=str(s[i]+s1[i])
# print(s2)
# 4.实现100-200里面所有的质数字,打印这些质数并且求出个数
# for i in range(100,200):
#     if i%2!=0 and i%3!=0 and i%5!=0:
#    print(i)    s  s1
# 1.有一列分数序列，2／1， 3／2， 5／3， 8／5。。。求出前20项之和

#
# q=2
# h=1
# j=0
# s=0
# for i in range(20):
#     s+=q/h
#     j=q+h
#     h=q
#     q=j
#     print(q,h)
# print(s)
#

# 2.二 输入一个数求1！+2！+3！+4！+n！=？
# 3.有四个数字1，2，3，4，能组成多少个互不相同的三位数
#try:
#    print("请输入一个数字：")
#    user=input()
#    print(int(user)+1)
#except ValueError:
#    print("只能输入数字！")
#except (IOError,Valueerror):
#    print("文件夹错误")
#except Exception:
#    print("WRONG!")
#except ValueError:
#    print("111")
#print("hello world")
#IOError
#KeyError
#ValueError
# #Exception(所有异常的基类)
# try:
#     print("a")
#     print("b")
#     raise(ValueError)
#     print("c")
# except:
#     print("我想在这里先停下来")
# else:#没有发生异常时执行的代码
#     print("这里没有发生异常哦")
# finally:#无论是否发生异常都一定要执行的语句！
#     print("你们要好好学习！")
# print("hallo world")
#

#讲师-韩希庆15764388980 2019/2/21 11:05:44
#电脑随机生成1~100随机数，用户输入一个数字，电脑提示用户大或者小，猜错，继续提示；猜对，则程序终止

# import random
# import string
# i=1
# while 1:
#     bj = int(input("请输入你的选择"))
#     s = random.choice(range(1, 101))
#     print("摇出的号是：",s)
#
#     if s>bj:
#         print("太小了")
#
#     elif s==bj:
#         print("猜对了")
#         break
#     else:
#        print("太小了")
#
import string
# list1={1,2,5,4,5,6,55,689,45,21,5463,13}
# list2={1,2,5,4,5,6}
# list3={}
# list4=[1,2,5,4,5,6,55,689,45,21,5463,13]
# list3=list1|list2
# print(sorted(list4,1))
# def fa(n):
#     s=0
#     for i in range(n+1):
#         if n>=i:
#             s+=i
#     print(s)
# fa(int(input("请输入任意一个数来求他的和")))
