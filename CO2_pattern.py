n = int(input("Enter number of lines of stars do you need to print  :"))
i = 0
j = 0

while (i < n):
    j = 0
    while (j <= i):
        print("*", end=" ")
        j = j + 1
    print("\n")
    i = i + 1
i = n - 1
while (i >= 0):
    j = 1
    while (j <= i):
        print("*", end=" ")
        j = j + 1
    print("\n")
    i = i-1
