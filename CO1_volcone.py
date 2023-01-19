#Program to enter Height and Radius of a Cone and to Calculate its volume

#Receiving the data from the user
rad=int(input("Enter the Radius of the Cone  : "))
height=int(input("Enter the Height of the Cone  : "))

#Calculating the volume
pi=3.14
vol=pi*(rad*rad)*height/3

#Printing the results
print("\nThe Volume of the cone  : ",vol)
