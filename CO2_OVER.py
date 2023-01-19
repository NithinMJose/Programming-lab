list1=[]
n=int(input("enter the limit"))
for i in range(n):
    value=int(input("enter the number"))
    if value>100:
        value="over"
    list1.append(value)
print(list1)
