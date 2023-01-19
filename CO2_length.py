n=int(input("Enter number of terms"))
a=[]
for i in range (n):
    num=input("Enter list")
    a.append(num)
max1=len(a[0])
temp=a[0]
for i in a:
    if (len(i)>max1):
        max1=len(i)
        temp=i
print("Longest word is :",temp,"and length is ",max1)
