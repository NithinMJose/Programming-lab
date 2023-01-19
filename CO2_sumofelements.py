n=int(input("enter the limit"))
list1=[]
for i in range(n):
    num=int(input("enter the number"))
    list1.append(num)
sum=0
for i in list1:
    sum=sum+i
print("The sum is",sum)
