# Flashy - Vocabulary Flashcard App

Flashy is a vocabulary flashcard application built using Python and tkinter. It helps users learn and memorize new words in a foreign language through a simple and interactive interface.

## Features

- **Flashcard Interface:** Intuitive flashcards with a French word on one side and its English translation on the other.
- **Interactive Learning:** Mark words as known or unknown for efficient learning.
- **Data Persistence:** Save progress and words to learn even after closing the application.

## Getting Started

1. **Clone the repository:**

   ```bash
    https://github.com/Olusegun-Light/Python-100-Days-Of-Code.git
   ```

2. **Navigate to the project directory:**

   ```bash
   cd Day-31
   ```

3. **Install the required dependencies:**

   ```bash
   pip install pandas
   ```

4. **Run the application:**

   ```bash
   py main.py
   ```

## Usage

1. On startup, the application displays a French word.
2. Click on the card to reveal its English translation.
3. Click the checkmark if you know the word or the 'X' button if you don't.
4. The next flashcard will automatically appear, and your progress is saved.

## Vocabulary Data

Vocabulary data is stored in a CSV file (`data/words_to_learn.csv`). Initially, it uses a set of French words, but you can customize the dataset as needed.

## Note

- The app uses images for the flashcards. Ensure the 'images' folder contains 'card_front.png' and 'card_back.png'.

Feel free to customize and extend this flashcard app according to your language learning needs. Happy learning!
