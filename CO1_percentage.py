#Receiving the data from the user
name=input("Enter your Name   : ")
mark_1=int(input("Enter marks of Photo Electronics  : "))
mark_2=int(input("Enter marks of Chemistry  : "))
mark_3=int(input("Enter marks of Quantum Mechanics  : "))
mark_4=int(input("Enter marks of Mathematics  : "))
mark_5=int(input("Enter marks of Programing in C  : "))

#Calculating Total marks and Percentage
total=mark_1+mark_2+mark_3+mark_4+mark_5
percent=(total/500)*100

#Printing the results
print("\nTotal marks   : ",total,"/500")
print("percentage  : ",percent,"%")
