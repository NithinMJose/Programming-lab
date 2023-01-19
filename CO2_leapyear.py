limit=int(input("enter the limit"))
print("The leap years are:")
for i in range(2022,limit+1):
    if i%4==0:
        print(i,"\n")
