go_again = True
while go_again == True:
    num = str(input("Enter the year you would like to check: "))
    if num.isnumeric() != True:
        go_again = True
        print("Please enter a number!")
    else:
        go_again = False
        num = int(num)


if ((num % 4 == 0 and num % 100 == 0 and num % 400 == 0) or (num % 4 == 0 and num % 100 != 0)):
    print(str(num) + " is a leap year.")
else:
    print(str(num) + " is not a leap year.")
