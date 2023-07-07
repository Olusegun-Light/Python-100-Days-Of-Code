# Letter Generation

This Python script generates personalized letters by replacing placeholders with names from a file. It reads a list of names from "invited_names.txt" and creates a letter for each name by replacing the "[name]" placeholder in the "starting_letter.txt" template. The generated letters are saved in the "ReadyToSend" folder.

## Usage

1. Ensure that you have the following files and directories in the project folder:

- `main.py`
- `Input/`
  - `Names/`
    - `invited_names.txt`
  - `Letters/`
    - `starting_letter.txt`
- `Output/`
  - `ReadyToSend/`

2. Update the "invited_names.txt" file with the desired names. Each name should be on a separate line.

3. Customize the "starting_letter.txt" template by replacing the "[name]" placeholder with the desired text.

4. Run the script by executing the following command:

```bash
python main.py
```

1. The script will generate a personalized letter for each name in the `"invited_names.txt"` file. The letters will be saved as separate text files in the "ReadyToSend" folder with the format `"letter_for_[name].txt"`.
