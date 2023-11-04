# Quizzler

Quizzler is a simple quiz application that fetches questions from the Open Trivia Database API and presents them to the user for answering. The application uses Tkinter for the graphical user interface and demonstrates the use of classes and APIs.

## Getting Started

Before running the application, ensure you have the required dependencies installed. You can install them using the following:

```bash
pip install requests
```

## Prerequisites

- Python 3

## Usage

Run the `main.py` script to start the quiz. The script fetches 10 boolean-type questions from the Open Trivia Database API under the "Science: Computers" category.

```bash
py main.py
```

Answer the questions presented in the Tkinter GUI by clicking the "True" or "False" buttons. After completing the quiz, the final score is displayed in the terminal.

## Project Structure

- **main.py**: The main script that initiates the quiz by creating instances of `Question`, `QuizBrain`, and `QuizInterface`.
- **data.py**: Fetches quiz questions from the Open Trivia Database API.
- **question_model.py**: Defines the `Question` class.
- **quiz_brain.py**: Implements the `QuizBrain` class, which manages the quiz logic.
- **ui.py**: Implements the graphical user interface using Tkinter.
