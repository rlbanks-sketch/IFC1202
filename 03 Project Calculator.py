def calculator():
    # Prompt for the first number (float to accept int or float)
    num1 = float(input("Enter First Number: "))

    # Prompt for the operator
    operator = input("Enter Operator (+,-,*,/): ")

    # Prompt for the second number
    num2 = float(input("Enter Second Number: "))

    # Perform calculation based on operator
    if operator == '+':
        result = num1 + num2
        print(f"{num1} + {num2} = {result}")
    elif operator == '-':
        result = num1 - num2
        print(f"{num1} - {num2} = {result}")
    elif operator == '*':
        result = num1 * num2
        print(f"{num1} * {num2} = {result}")
    elif operator == '/':
        # Handle division by zero
        if num2 == 0:
            print("Error: Division by zero")
        else:
            result = num1 / num2
            print(f"{num1} / {num2} = {result}")
    else:
        print("Invalid Operator")

if __name__ == "__main__":
    calculator()
