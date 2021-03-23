

try:
    value = 10 / 0
    number = int(input("Enter a number: "))
    print(number)
except ZeroDivisionError:
    print("Devided by zero!")
except:
    print("Invalid Input!")