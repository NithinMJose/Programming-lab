# # Program for the Simple Calculator

# Receiving the mode of calculation from user
print("Select the Operation. \n 1.Addition \n 2.Subtraction \n 3.Multiplication \n 4.Division\n")
choice = input("Enter the Choice  (1/2/3/4): ")

# Receiving the numbers and print result if choice is valid
if choice in ('1', '2', '3', '4'):
    num1 = float(input("\nEnter First Number: "))
    num2 = float(input("Enter Second Number: "))
    if choice == '1':
        print(num1, "+", num2, "=", num1 + num2)
    elif choice == '2':
        print(num1, "-", num2, "=", num1 - num2)
    elif choice == '3':
        print(num1, "*", num2, "=", num1 * num2)
    elif choice == '4':
        print(num1, "/", num2, "=", num1 / num2)

# Printing invalid choice
else:
    print("Invalid Input")

