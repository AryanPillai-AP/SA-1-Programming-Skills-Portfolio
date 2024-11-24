#Exercise 5: Days of the Month

# Dictionary to store days in each month.
month_days = {
    1: 31,  # January
    2: 28,  # February (non-leap year)
    3: 31,  # March
    4: 30,  # April
    5: 31,  # May
    6: 30,  # June
    7: 31,  # July
    8: 31,  # August
    9: 30,  # September
    10: 31,  # October
    11: 30,  # November
    12: 31   # December
}
# Asks the user to input the month number.

try:
    month = int(input("Enter the month number (1-12): "))
    if month < 1 or month > 12:
        print("Invalid month number. Please enter a number between 1 and 12.")
    else:
        # Check for February and leap year adjustment
        if month == 2:
            leap_year = input("Is it a leap year? (yes/no): ").strip().lower()
            if leap_year == "yes":
                print("February has 29 days in a leap year.")
            else:
                print(f"February has {month_days[month]} days.")
        else:
            print(f"The month has {month_days[month]} days.")
except ValueError:
    print("Invalid input. Please enter a numeric value for the month.")
