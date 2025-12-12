

year = int(input("Enter a year: "))

if(year % 400 == 0 and year % 100 ==0):
    print(year,"The year is leap year")
elif (year %4 == 0 and year % 100 !=0):
    print(year , "Year is leap year")
else:
    print(year , "Year is not leap year")