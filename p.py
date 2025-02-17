try:

    x = 10 /0

except ZeroDivisionError:

    print("Can't divide by zero!")

else:

    print("No error occurred!")

finally:

    print("This will always execute.")