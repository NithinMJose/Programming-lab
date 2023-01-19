#Program to enter Height and Radius of a cylinder & to calculate its Volume

#Receiving the data from the user
rad=int(input("Enter the Radius of the cylinder  : "))
height=int(input("Enter the Height of the cylinder  : "))

#Calculating the volume
pi=3.14
vol=pi*(rad*rad)*height

#Printing the results
print("\nThe Volume of the cylinder  : ",vol)
