import os
# os.mkdir("测试1")
# s=open("C://Users//LP//PycharmProjects//untitled//bean//测试1//test.txt", 'w')
# for i in range(100):
#     open("C://Users//LP//PycharmProjects//untitled//bean//测试1//test%d.txt"%i,'w')
# for i in range(100):
#     s.write(str(i)+"--")
# s=open("C://Users//LP//PycharmProjects//untitled//bean//测试1//test.txt",'r')
# f=s.read(50)
# print(f)
# def line(s):
#     file=open("test1.txt",'w')
#     file.write(s)
#
# strs=input("请输入你需要存入的字符串")
# line(strs)
def line(s):
    file=open("test1.txt",'w')
    file.write(s)

strs=input("请输入你需要存入的字符串")
line(strs)