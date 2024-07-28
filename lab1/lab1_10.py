months = ("January", "February", "March", "April", "May", "June",
          "July", "August", "September", "October", "November", "December")

# Number of days in each month (non-leap year)
days_in_months = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

month_name = input("Enter the month name: ")
year = int(input("Enter the year: "))

#  if it's a leap year
is_leap_year = (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)

# Find the number of days in the given month
if month_name in months:
    month_index = months.index(month_name)
    if month_name == "February" and is_leap_year:
        days = 29
    else:
        days = days_in_months[month_index]
    print(f"the number of days in {month_name}is :{days} ")
else:
    print("Invalid month name.")
