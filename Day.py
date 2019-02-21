# import random
# print(random.choice(range(10)))
import random
# var=print(random.choice(range(7,9)))
# print(var)
# print(random.choice(['w','e']))
# print(random.randrange (1,99,3))
# print ("randrange(1,100, 2) : ", random.randrange(1, 100, 2))
# print(random.random()*100)
# print(random.seed(10));
# list=[1,2,5,3,22,8,47,5];
# random.shuffle(list);
#
# print(list)

# print(random.uniform(5,10))
# print(random.randint(5,10))
#
# var1="sello";
# var2="Word";
# if 'H' in var1:
#     print("H在var1")
# else:
#     print("H不在var1")
# if 'H' not  in var2:
#     print("ss")
# a="Hello"
# c=a.rjust(10)
# print(c)
# for i in range(10,0,-1):
#     print(i)
# import cmath

# var="asdasdasdASDASDASD";
# var1=var.lower();
#
# var2=var.upper();
# var3=var.swapcase();        #swapcase 大写转小写  小写转大写
# print(var1)
# print(var2)
# print(var3)
#
# dict = {'Alice': '2341', 'Beth': '9102', 'Cecil': '3258'}
# dict1 = { 'abc': 456 };
# dict2 = { 'abc': 123, 98.6: 37 };
#
# print(dict)
# a="hello world I am Anna"
# print(a.find("Anna",0,21))
# print(a.index("Anna",10,21))
# print(a.count("Anna"))
# b=a.replace("Anna","AAAA",2)
# print(b)
# b=a.split(" ",1);
# print(b)
# b=a.capitalize();
# print(b)
# b=a.startswith("h");
# print(b)
# b=a.endswith("a");
# print(b)
# list1 = ['Google', 'Runoob', 1997, 2000];
# list2 = [1, 2, 3, 4, 5 ];
# list3 = ["a", "b", "c", "d"];
# # print(list1+list2+list3)
# list1[0]='baidu';
# del list3[1]
# print(list3)
# var=(2,2,2,3,3213,34,2,4,234)
# var1=(2,)
# print(var)
# print(var1)
# import random
# random.seed()
# print ("使用默认种子生成随机数：", random.random())
# random.seed(10)
# print ("使用整数种子生成随机数：", random.random())
# random.seed("hello",2)
# print ("使用字符串种子生成随机数：", random.random())
# var="sssdddsssadddadafasfaf";
# b=input("请输入");
# s=var.count(b);
# if s>1:
#     print("重复");
#     print(b)
# else:
#     print("不重复")
#
#
# var=[]
# str ='qweasdzxcqweasdzxcljjkk'
# cf=''
# bcf=''
# i=0
# while i<len(str):
#     if str.count(str[i])>1:
#         if str[i] in cf:
#             i+=1
#             continue
#         cf += str[i]
#     else:
#         bcf+=str[i]
#     i+=1
# print('重复元素有：%s'%cf)
# print('不重复重复元素有：%s'%bcf)
var=[1,1,2,2,2,3,2,2,2]
print(len(var))
print(len(set(var)))



