num =int(input("Enter the Value:"))
temp = num
rev = 0

while(num > 0):
    r = num % 10
    rev = rev * 10 + r
    num = num // 10

if(temp == rev):
    print("Palindrome Number!")
else:
    print("Not Palindrome Number!")
