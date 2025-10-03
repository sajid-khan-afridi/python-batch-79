try:
    x = int(input("Enter a number: "))
except Exception as e:
    print(type(e))
    print(type(Exception))
    print("Error occurred:", e)


# Division by zero raises an exception
num = 10
den = 0
try:
    result = num / den  # Raises ZeroDivisionError
except ZeroDivisionError as e: # When we use as e, e is the instance of the ZeroDivisionError exception
# except Exception as e: # When we use as e, e is the instance of the ZeroDivisionError exception
    print(f"Division by zero is not allowed: {ZeroDivisionError}")
    print(f"Division by zero is not allowed: {e}")

try:
    age = int(input("Enter your age: "))  # Invalid literal for `int()`
    print("Your age is", age)
except ValueError as e:#specific
    print(f"Invalid input! Please enter a whole number. Error: {e}")