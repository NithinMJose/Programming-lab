num = input('Enter the number: ')
i = 0
length = len(num)
for i in range(length):
    if num[i] != num[-1 - i]:
        print(num, 'is not a Palindrome')
        break
else:
    print(num, 'is a Palindrome')
