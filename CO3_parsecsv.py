import csv
csv_strings="""1,2,3,4,5,6,7,8,9"""
print("Original String :")
print(csv_strings)
lines=csv_strings.splitlines()
print("List of csv formatted strings")
print(lines)
reader=csv.reader(lines)
parsed_csv=list(reader)
print("\nList Representation of csv file :")
print(parsed_csv)
