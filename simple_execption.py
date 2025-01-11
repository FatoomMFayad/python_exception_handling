from traceback import print_tb

try:
    x = int(input("Enter a number: "))
    y = int(input("Enter another number: "))
    print(x / y)
except ValueError as e:
    print(f"You should input a number: {e}")
except ZeroDivisionError as e:
    print(f"You cannot divide by zero: {e}")
except Exception as e:
    print(f"Something went wrong: {e}")
print("Thank you!")