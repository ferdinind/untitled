import random
s='The column above illustrates apparently' \
  ' the polularity of people ' \
  'doing exercise in a certain year ' \
  'from 2013 to 2018.Based upon the data,' \
  'we can see that python is wonderful. ' \
  'python is wonderful. Python '
print(s)
s=s.replace("."," ")
print(s)
s=s.split(" ")
s.pop()

dict={}
for i in s:
    key=dict.get(i)
    if (key==None):
        dict[i]=1
    else:
        dict[i]+=1
dict1={}
sv=list(dict.values())
sv.sort()
sv=set(sv)

for i in sv:
    for j in dict:
        if dict[j]==i:
            dict1[j]=i
print(dict1)
