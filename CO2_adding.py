str=input("Enter the string")
revend=str[-1:-4:-1]
end=revend[::-1]
if end=="ing":
    print(str,end="ly")
else:
    print(str,end="ing")
