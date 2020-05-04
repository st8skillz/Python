# ask the user for the year
#Spencer Goldwin
year = int(input("Enter a year to determine if it is a leap year. "))

#calculate whether this is a leap year
if (year % 4) == 0:
    print("In", year, "February has 29 days.")
else:
    print("In", year, "Feburary has 28 days.")
