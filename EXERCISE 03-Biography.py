#Exercise 3: Biography

# Taking input from the user
name = input("Enter your name: ")  # Handles multiple words
hometown = input("Enter your hometown: ")

# Handle invalid age input
while True:
    try:
        age = int(input("Enter your age (numeric value only): "))  # Converts age to integer
        break  # Exit loop if input is valid
    except ValueError:
        print("Invalid input. Please enter a numeric value for age.")

# Storing information in a dictionary
person_info = {
    "name": name,
    "hometown": hometown,
    "age": age
}

# Printing the values on separate lines
print(person_info["name"], person_info["hometown"], person_info["age"], sep="\n")

