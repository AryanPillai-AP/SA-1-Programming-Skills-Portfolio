def check_answer(user_answer, correct_answer):
    """Check if the user's answer is correct, ignoring case."""
    return user_answer.lower() == correct_answer.lower()

def run_quiz():
    # Dictionary of European countries and their capitals
    capitals = {
        "France": "Paris",
        "Germany": "Berlin",
        "Italy": "Rome",
        "Spain": "Madrid",
        "United Kingdom": "London",
        "Netherlands": "Amsterdam",
        "Greece": "Athens",
        "Portugal": "Lisbon",
        "Sweden": "Stockholm",
        "Denmark": "Copenhagen"
    }
    
    score = 0
    total_questions = len(capitals)
    
    print("Welcome to the European Capitals Quiz!")
    print(f"You will be given questions about the capitals of {total_questions} European countries.")
    print("Capitalisation does not matter.\n")
    
    # Ask each question
    for country, capital in capitals.items():
        user_answer = input(f"What is the capital of {country}? ")
        
        if check_answer(user_answer, capital):
            print("Correct! Well done!")
            score += 1
        else:
            print(f"Sorry, that's incorrect. The capital of {country} is {capital}.")
        print()  # Empty line for better readability
    
    # Show final results
    print("Quiz completed!")
    print(f"Your final score: {score}/{total_questions}")
    
    # Provide feedback based on score
    if score == 10:
        print("Perfect score! You're a geography expert!")
    elif score >= 8:
        print("Great job! You really know your European capitals!")
    elif score >= 6:
        print("Good effort! Keep studying to improve your score.")
    else:
        print("You might want to review European capitals some more.")

if __name__ == "__main__":
    run_quiz()