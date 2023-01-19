n1=int(input("Enter the limit"))
list1=[]
for i in range(n1):
    num=int(input("Enter the number"))
    list1.append(num)
n2=int(input("Enter the limit"))
list2=[]
for i in range(n2):
    num=int(input("Enter the number"))
    list2.append(num)

print(list1)
print(list2)

#To check lists are of same length
a=len(list1)
b=len(list2)

if(a==b):
    print("The length of both lists are the same")
else:
    print("Lengths of lists are not same")


#Sum of list
sum1=0
for i in list1:
    sum1=sum1+i
sum2=0
for i in list2:
    sum2=sum2+i

if(sum1==sum2):
    print("sum of both lists are ;",sum1)
else:
    print("The sum are not the same")


#same elements
set1=set(list1)
set2=set(list2)

y=set2.intersection(set1)
newlist=list(y)

print("Common elements are :", newlist)
