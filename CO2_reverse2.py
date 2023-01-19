num = input("Enter the number :")
reverse = ''
for i in range(len(num), 0, -1):
     reverse = reverse + num[i-1]
print('The reverse number is =', reverse)
