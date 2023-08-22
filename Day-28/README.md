# Pomodoro Timer

A simple Pomodoro Timer GUI application built using the Tkinter library in Python. The Pomodoro Technique is a time management method developed by Francesco Cirillo in the late 1980s. It uses a timer to break work into intervals, traditionally 25 minutes in length, separated by short breaks.

## Features

- Timer mechanism for work and breaks.
- Countdown mechanism to display the time remaining.
- Start and reset buttons for control.
- Marks to track completed work sessions.
- User-friendly UI with a tomato image.

## Prerequisites

To run this application, you need to have Python installed on your system. The Tkinter library is included with most standard Python distributions.

## How to Use

1. Clone this repository to your local machine.
2. Make sure you have a `tomato.png` image file in the same directory as the `main.py` script.
3. Open a terminal/command prompt and navigate to the repository folder.
4. Run the following command to start the Pomodoro Timer:

   ```shell
   python main.py
   ```

5. The GUI application will open, displaying the timer and control buttons.

## Functionality

- Click the "Start" button to initiate the Pomodoro timer. The timer will follow the traditional Pomodoro cycle of work sessions and breaks.
- The timer text will display the time remaining in the current session.
- The "Reset" button can be used to reset the timer and marks.
- Upon completing work sessions, checkmarks ("✅") will appear below the timer to indicate completed sessions.

## Customization

Feel free to modify the constants in the `main.py` script, such as work, short break, and long break durations, to match your preferred timing intervals.

## Acknowledgements

This project was inspired by the Pomodoro Technique and developed for educational purposes using the Tkinter library in Python.
