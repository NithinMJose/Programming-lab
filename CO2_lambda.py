choice=int(input(" 1. Area of Rectangle \n 2. Area of Square \n 3. Area of Triangle \n ENTER YOUR CHOICE : "))
if (choice==1):
    a = int(input("Enter length"))
    b = int(input("Enter breadth"))
    area1 = lambda a, b: a * b
    print("AREA is ", area1(a,b))
elif (choice==2):
    a = int(input("Enter length"))
    area2 = lambda a: a * a
    print("AREA is ", area2(a))
elif (choice==3):
    a = int(input("Enter length"))
    b = int(input("Enter height"))
    area3 = lambda a, b: (a * b) / 2
    print("AREA is ", area3(a, b))
