import csv
reader=csv.reader(open('Sample.csv'))
no_lines=len(list(reader))
print(no_lines)
