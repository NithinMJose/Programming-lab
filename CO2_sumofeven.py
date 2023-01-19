limit = int(input("Enter the Limit  :"))
a = 1
sumodd = 0
sumeven = 0
while a <= limit:
    if a%2 == 0:
        sumeven = sumeven + a
    else:
        sumodd = sumodd + a
    a = a+1
print("Sum of Odd Numbers:",sumodd)
print("Sum of Even Numbers:",sumeven)
