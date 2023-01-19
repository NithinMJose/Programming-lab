class Rectangle():
    def __init__(self,length,breadth):
        self.length=length
        self.breadth=breadth
    def area(self):
        return self.length*self.breadth
    def perimeter(self):
        return 2*(self.length + self.breadth)
l1=float(input("Enter the length of the rectangle : "))
b1=float(input("Enter the bteadth of the rectangle : "))
l2=float(input("Enter the length of the rectangle 2 : "))
b2=float(input("Enter the breadth of the rectangle2 : "))
rect1=Rectangle(l1,b1)
rect2=Rectangle(l2,b2)
print("area of recangle 1 is ", rect1.area(), " and perimeter is " ,rect1.perimeter())
print("area of recangle 1 is ", rect2.area(), " and perimeter is " ,rect2.perimeter())
print("Rectangle1 is larger :",rect1.area()>rect2.area())
