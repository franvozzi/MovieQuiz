import requests
import json

def get_movie_quiz_questions(amount=5, category=11, difficulty="easy", type="multiple"):
    # Open Trivia Database API endpoint for movie-related questions
    api_url = "https://opentdb.com/api.php"

    # Parameters for the API request
    params = {
        "amount": amount,
        "category": category,  # 11 corresponds to Entertainment: Film category
        "difficulty": difficulty,
        "type": type
    }

    # Make the API request
    response = requests.get(api_url, params=params)

    # Check if the request was successful (status code 200)
    if response.status_code == 200:
        # Parse the JSON response
        data = json.loads(response.text)
        
        # Extract and return the list of questions
        return data.get("results", [])
    else:
        print("Failed to fetch questions. Status code:", response.status_code)
        return []

def print_question(question, choices):
    print(question)
    for i, choice in enumerate(choices, start=1):
        print(f"{i}. {choice}")
    user_answer = input("Your answer (enter the corresponding number): ")
    return int(user_answer) - 1  # Convert user input to index

def main():
    print("Welcome to the Movie Quiz!")

    # Get movie-related quiz questions
    questions = get_movie_quiz_questions()

    # Iterate through the questions and ask the user
    for i, question_data in enumerate(questions, start=1):
        question = question_data["question"]
        choices = question_data["incorrect_answers"] + [question_data["correct_answer"]]
        choices = [choice.replace("&quot;", "\"").replace("&#039;", "'") for choice in choices]  # Clean HTML entities
        choices = [bytes(choice, "utf-8").decode("utf-8", "ignore") for choice in choices]  # Remove invalid characters
        choices.sort()  # Sort choices alphabetically

        user_answer = print_question(f"\nQuestion {i}: {question}", choices)

        # Check the user's answer
        correct_answer = question_data["correct_answer"]
        if choices[user_answer] == correct_answer:
            print("Correct!\n")
        else:
            print(f"Sorry, the correct answer is: {correct_answer}\n")

    print("Quiz completed! Thanks for playing.")

if __name__ == "__main__":
    main()
