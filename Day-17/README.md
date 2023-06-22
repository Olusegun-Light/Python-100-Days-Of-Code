# Quiz Game

Welcome to the Quiz Game! This is a simple Python program that allows you to take a quiz by answering a series of True/False questions. Test your knowledge and see how well you do!

## How to Run the Game

To run the Quiz Game, follow these steps:

1. Ensure that you have Python installed on your machine.

2. Download or clone the project files to your local machine.

3. Open a terminal or command prompt and navigate to the project directory.

4. Run the following command to start the game:

   ```shell
   python main.py
   ```

5. The game will begin, and you will be presented with a series of questions. Enter your answer as either "True" or "False" for each question.

6. After answering all the questions, your final score will be displayed.

## Customizing the Quiz

You can customize the quiz by modifying the `question_data` list in the `data.py` file. Each question in the list is represented by a dictionary with two keys: "text" and "answer". Update the list with your own questions and answers to create a personalized quiz.

## Project Structure

The project consists of the following files:

- `main.py`: The main script to run the quiz game. It imports the necessary modules and manages the flow of the game.

- `question_model.py`: Defines the Question class, which represents a single question in the quiz. Each question has a text and an answer.

- `quiz_brain.py`: Contains the QuizBrain class, which handles the logic of the quiz game. It keeps track of the score, manages the questions, and checks the answers.

Feel free to explore and modify the code to enhance the game or add new features. Have fun challenging yourself and others with your own quiz questions!

## Happy Quizzing!

Enjoy playing the Quiz Game and have fun testing your knowledge. Feel free to share the game with your friends and family, and see who can achieve the highest score. Happy quizzing!
