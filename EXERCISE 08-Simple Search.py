#Exercise 8: Simple Search

# List of names
names = ["Jake", "Zac", "Ian", "Ron", "Sam", "Dave"]

#Allow the user to input the search term
search_term = input("Enter the name you want to search for: ").strip()

# Search for the name in the list
if search_term in names:
    print(f"{search_term} is in the list")
else:
    print(f"{search_term} is not in the list.")


