# Fitness Tracker

Track your daily exercises and update your workout log using the Nutritionix API and Google Sheets.

## Prerequisites

- Python 3.x
- `requests` library (`pip install requests`)

## Getting Started

1. Clone the repository:

   ```bash
   git clone https://github.com/Olusegun-Light/Python-100-Days-Of-Code
   ```

2. Navigate to the project directory:

   ```bash
   cd Day-38
   ```

3. Set up your environment variables:

   - `YOUR_APP_ID`: Obtain this from [Nutritionix API](https://developer.nutritionix.com/).
   - `YOUR_API_KEY`: Obtain this from [Nutritionix API](https://developer.nutritionix.com/).
   - `YOUR_SHEET_ENDPOINT`: Your Google Sheets API endpoint.
   - `USERNAME` and `PASSWORD` or `TOKEN` based on your authentication method.

4. Run the script:

   ```bash
   python main.py
   ```

## Usage

1. Input the exercises you did when prompted.

2. The script will make a request to the Nutritionix API to get information about the exercises.

3. The results will be printed, and the script will update your workout log on Google Sheets.

## Authentication Methods

The script supports multiple authentication methods:

- No Auth: For public sheets.
- Basic Auth: For private sheets.
- Bearer Token: For token-based authentication.

## Acknowledgments

This project uses the Nutritionix API to fetch exercise information and updates a Google Sheets document with workout details. Feel free to customize the script to fit your fitness tracking needs.

If you encounter any issues or have suggestions, please open an issue or contribute to the project.

Happy tracking!
