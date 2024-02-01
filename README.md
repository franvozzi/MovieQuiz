# Movie Quiz

## Overview

Movie Quiz is a simple Python script that serves as an interactive quiz game. The script fetches movie-related questions from the Open Trivia Database API, allowing users to test their knowledge of movies in a fun and engaging way.

## Features

- **Python Version:** 3.9.6
- **Requests Version:** 2.28.2

## Getting Started

1. Install the required libraries:

   ```bash
   pip install requests
   ```
Run the script:
python movie_quiz.py
Follow the on-screen instructions to answer the quiz questions.

Customization
You can modify the script to change the difficulty level by adjusting the parameters in the get_movie_quiz_questions function.

## Example: Set difficulty to "medium"
```python
questions = get_movie_quiz_questions(amount=5, difficulty="medium") 
```

Feel free to explore and adapt the code to suit your preferences.

## Concepts Demonstrated
- Importing Libraries
- API Interactions
- JSON Parsing
- Error Handling
- User Input
- Looping
- String Manipulation
- Conditional Statements

## Contributing
Contributions are welcome! Feel free to open issues or submit pull requests to enhance the functionality or improve the code.

## License
This project is licensed under the MIT License - see the LICENSE file for details.

## Acknowledgments
The Movie Quiz script uses the Open Trivia Database API for fetching quiz questions.
Happy quizzing!

Make sure to adjust the details in the README file as needed, including the license information, acknowledgments, and any additional sections you might want to include.
