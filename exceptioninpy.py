# How exceptions are handled in Python?. Illustrate with the help of an example.

def divide(x, y):
    try:
        result = x / y
    except ZeroDivisionError:
        print("Error: division by zero")
    else:
        print("Result:", result)
    finally:
        print("Done")

# Example usage
divide(10, 2)
divide(10, 0)

'''
Result: 5.0
Done
Error: division by zero
Done
'''