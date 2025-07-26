def add_numbers(a: float, b: float) -> float:
    """Returns the sum of two numbers."""
    return a + b

def main():
    print("Addition of Two Numbers")
    
    try:
        # Take input from the user
        num1 = float(input("Enter the first number: "))
        num2 = float(input("Enter the second number: "))

        # Perform addition
        result = add_numbers(num1, num2)

        # Display result
        print(f"\nResult: {num1} + {num2} = {result}")
        
    except ValueError:
        print("Error: Please enter valid numeric values.")

if __name__ == "__main__":
    main()
