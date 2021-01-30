num = int(input("Enter the year you would like to check: "))

if ((num % 4 == 0 and num % 100 == 0 and num % 400 == 0) or (num % 4 == 0 and num % 100 != 0)):
    print(str(num) + " is a leap year.")
else:
    print(str(num) + " is not a leap year.")
