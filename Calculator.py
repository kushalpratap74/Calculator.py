def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        return "Error: Division by zero is not allowed!"
    return a / b

def calculator():
    print("Simple Calculator")
    print("=================")
    print("Select an operation:")
    print("1. Addition (+)")
    print("2. Subtraction (-)")
    print("3. Multiplication (*)")
    print("4. Division (/)")
    
    try:
        choice = input("Enter the number of the operation (1/2/3/4): ")

        if choice not in ['1', '2', '3', '4']:
            print("Invalid operation choice! Please select 1, 2, 3, or 4.")
            return

        num1 = float(input("Enter the first number: "))
        num2 = float(input("Enter the second number: "))

        if choice == '1':
            result = add(num1, num2)
            operation = '+'
        elif choice == '2':
            result = subtract(num1, num2)
            operation = '-'
        elif choice == '3':
            result = multiply(num1, num2)
            operation = '*'
        elif choice == '4':
            result = divide(num1, num2)
            operation = '/'
        
        print(f"Result: {num1} {operation} {num2} = {result}")
    
    except ValueError:
        print("Error: Please enter valid numbers!")
    
if __name__ == "__main__":
    calculator()
