from datetime import date
def calculateage(birthDate):
    today = date.today()
    age = today.year - birthDate.year -((today.month, today.day) < (birthDate.month, birthDate.day))
    return age
year=int(input("Enter the year of birth"))
month=int(input("Enter the month of birth (in integer form)"))
date1=int(input("Enter the date of birth"))
print(calculateage(date(year,month,date1)), "years")
