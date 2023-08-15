# NATO Phonetic Alphabet Converter

This Python script converts a word into its corresponding NATO phonetic alphabet representation using a provided CSV dataset.

## Description

The NATO phonetic alphabet is a spelling alphabet used by international aviation and maritime communication. Each letter of the alphabet is represented by a specific word to ensure clear and accurate communication, especially in situations where letters might be misunderstood.

This script takes a user input word and converts it into its NATO phonetic alphabet representation. It utilizes a CSV dataset containing the mapping between letters and their corresponding words.

## How to Use

1. Make sure you have the required `nato_phonetic_alphabet.csv` file in the same directory as your script.

2. Run the Python script `main.py` using your preferred Python interpreter.

3. Enter a word when prompted. The script will convert the word into its NATO phonetic alphabet representation and display the result.

## Example

Suppose you run the script and input the word "hello", the output will be:

    ```
    ['Hotel', 'Echo', 'Lima', 'Lima', 'Oscar']
    ```

## CSV Dataset

The `nato_phonetic_alphabet.csv` dataset contains the mapping between letters and their NATO phonetic alphabet representations.

The dataset is structured as follows:

| letter | code    |
| ------ | ------- |
| A      | Alpha   |
| B      | Bravo   |
| C      | Charlie |
| ...    | ...     |

## Requirements

- Python 3.x
- pandas library (`pip install pandas`)

---

Feel free to modify and use this script to convert words into NATO phonetic alphabet representations. It can be particularly useful in scenarios where precise communication is crucial, such as spelling out important information over voice channels.
