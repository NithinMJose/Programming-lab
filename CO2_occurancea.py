list1=[]
num=int(input("enter the number of elements"))
m=0
for i in range(num):
    l=input("enter the name")
    list1.append(l)
for i in list1:
    c=i.count("a")
    m=m+c

print("count of a is ",m)
