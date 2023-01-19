n = int(input("Fibonacci series upto : "))
n1 = 0
n2 = 1
count = 0

if n <= 0:
   print("Please Enter a Positive integer")
else:
   while n1 < n:
       print(n1)
       n3 = n1 + n2
       n1 = n2
       n2 = n3
       count = count +1
print("No. of items :",count)
