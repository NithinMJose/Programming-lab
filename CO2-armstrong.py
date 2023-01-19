num = int(input("Enter the number: "))
length = len(str(num))
sum = 0
temp = num
for i in range(0,temp):
   rem = temp % 10
   sum = sum + rem ** length
   temp = temp//10
if num == sum:
   print(num ,"is an Armstrong number")
else:
   print(num ,"is not an Armstrong number")
