s=str (input("Enter the string"))
print("The entered string is %s",s)

first=s[0]
last=s[-1]
length=len(s)
middle=s[1:(length-1)]
final=last+middle+first

print("The edited string is :",final)
