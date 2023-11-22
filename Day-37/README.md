# Pixela Tracker

A simple Python script using the [Pixela API](https://docs.pixe.la/) to track and visualize your daily activities. In this example, it's set up to track cycling distance.

## Prerequisites

- Python 3.x
- Requests library (`pip install requests`)

## Getting Started

1. Clone the repository:

   ```bash
   git clone https://github.com/Olusegun-Light/Python-100-Days-Of-Code.git
   ```

2. Navigate to the project directory:

   ```bash
   cd Day-37
   ```

3. Update the `USERNAME`, `TOKEN`, and `GRAPH` variables in `main.py` with your Pixela account details.

4. Run the script:

   ```bash
   python main.py
   ```

## Functionality

1. **Create User Account:**

   - Makes a POST request to Pixela to create a new user account.

2. **Create Graph:**

   - Makes a POST request to Pixela to create a graph for tracking the specified activity.

3. **Add Pixel to the Tracker:**

   - Asks the user to input the distance they cycled today and makes a POST request to update the graph.

4. **Update Pixel:**

   - Updates the pixel value for the current date.

5. **Delete Pixel:**
   - Deletes the pixel for the current date.

## Acknowledgments

This project utilizes the [Pixela API](https://docs.pixe.la/) for creating and managing pixel-based graphs. Feel free to explore and modify the script for your tracking needs.

If you encounter any issues or have suggestions, please open an issue or contribute to the project.

Happy tracking!
