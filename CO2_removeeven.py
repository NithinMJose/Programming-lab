list1=[]
n=int(input("Enter number of elements"))
i=0
while(i<n):
    element=int(input())
    list1.append(element)
    i=i+1
for i in list1:
    if (i%2==0):
        list1.remove(i)
print("\nList items :",list1)
