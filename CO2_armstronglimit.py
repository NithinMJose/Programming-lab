l1 = int(input("Enter limit 1: "))
l2 = int(input("Enter limit 2: "))

while l1 <= l2:
   length = len(str(l1))
   sum = 0
   temp = l1

   while temp > 0:
      rem = temp % 10
      sum = sum + rem ** length
      temp = temp//10

   if l1 == sum:
      print(l1)

   l1= l1+1
