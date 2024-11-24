#Exercise 10: Is it even?

# Function to determine if a number is even or odd
def check_even_odd(number):
    # Check if the number is divisible by 2
    if number % 2 == 0:
        return f"{number} is even."
    else:
        return f"{number} is odd."

def main():
    try:
        # Ask the user to input a number
        user_input = int(input("Enter a number: "))  # Convert the input to an integer
        # Call the check_even_odd function and store the result
        result = check_even_odd(user_input)
        # Print the result returned by the function
        print(result)
    except ValueError:
        # Handle invalid input if the user doesn't enter a valid integer
        print("Invalid input. Please enter a valid integer.")

# Ensure the main function is executed only when the script is run directly
if __name__ == "__main__":
    main()
