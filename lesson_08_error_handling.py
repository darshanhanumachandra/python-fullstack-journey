"""
Error Handling - try/except/finally

**WHEN TO USE**:
- File operations (file might not exist)
- User input (user might enter wrong type)
- Division (avoid divide by zero)
- Type conversions (can't convert string to int)
- Network calls (connection might fail)
"""

print("Example 1: Division")
try:
    num1 = int(input("Enter num1 : "))
    num2 = int(input("Enter num2 : "))
    result = num1/num2
    print(f"Result : {result}")
except ZeroDivisionError:
    print("ERROR: Cannot divide by zero!")
except ValueError:
    print("ERROR: Please enter valid numbers!")

print("Example 2: Type Conversion")
try:
    user_input = int(input("Enter a number : "))
    print(f"User input = {user_input}")
except ValueError:
    print("ERROR: Input is not a valid number!")

print("Example 3: File Operations")
try:
    """
    with open("file.txt", "r") as file:
        content = file.read()
        print(content)
    """
    file = open("file.txt", "r")
    content = file.read()
    print(content)
    file.close()
except FileNotFoundError:
    print("ERROR: File not found!")

print("Example 4: Index Error")
try:
    numbers = [1,2,3,4]
    print(numbers[10])
except:
    print("ERROR: Index out of range!")

print("Example 5: Finally Block")
try:
    x = 5/0
    print(x)
except:
    print("ERROR: Math error!")
finally:
    print("This always runs, whether error happened or not")
