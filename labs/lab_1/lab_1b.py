"""
lab_1b.py

This is a script that implements a simple calculator. It takes two numbers and an operation,
then performs the operation and returns the result. 

The script asks the user to input the numbers and the operation to be performed,
and prints the result to the terminal window.

"""

def simple_calculator(operation: str, num1: float, num2: float) -> float:
    """
    Function that takes in two numbers and an operation (add, subtract, multiply, divide),
    then performs the operation on the two numbers and returns the result.

    Args:
        operation (str): The operation to perform ("add", "subtract", "multiply", "divide").
        num1 (float): The first number.
        num2 (float): The second number.

    Returns:
        float: The result of the operation.
    """

    if operation == "add":
        return num1 + num2
    elif operation == "subtract":
        return num1 - num2
    elif operation == "multiply":
        return num1 * num2
    else:
        if num2 != 0:
            return num1 / num2
        else:
            raise ValueError("Cannot divide by zero.")
    
def prompt_valid_number(message: str) -> float:
    """
    Continues to prompt the user with a provided message until the user provides a valid number

    Args:
        message (str) message to prompt the user with

    Returns:
        float: The number the user provides
    """
    while True:
        try:
            num = float(input(message))
            break
        except ValueError:
            print("Please input a number")
    return num

def prompt_valid_operation(message: str) -> str:
    """
    Continues to prompt the user with a provided message until the user provides a valid operation
    
    Args:
        message (str): message to prompt the user with
        
    Returns:
        str: the operation the user provides
    """
    
    while True:
        operation = input(message).strip().lower()
        
        if (operation == "add" or operation == "subtract" or operation == "multiply" or operation == "divide"):
            return operation
        
        print("Invalid operation. Please choose from 'add', 'subtract', 'multiply', or 'divide'.")
        

def main():
    
    print(f"===== Simple Calculator =====")

    # Ask the user for sample input    
    num1 = prompt_valid_number("Enter the first number: ")
    num2 = prompt_valid_number("Enter the second number: ")
    operation = prompt_valid_operation("Enter the operation (add, subtract, multiply, divide): ")

    # Perform the calculation and display the result
    result = simple_calculator(operation, num1, num2)
    print(f"The result of {operation}ing {num1} and {num2} is: {result}")


if __name__ == "__main__":
    main()
