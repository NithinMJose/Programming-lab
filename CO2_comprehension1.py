num=int(input("enter the limit"))
list1=[]
for i in range(num):
    a=int(input("enter the element"))
    list1.append(a)
print("the list you entered is:",list1)
newlist=[i for i in list1 if i>0]
print("the new list is",newlist)
