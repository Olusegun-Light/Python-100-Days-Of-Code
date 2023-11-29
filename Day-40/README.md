# Flight Deals Notifier

This Python script monitors flight prices, sends notifications for low-price alerts, and updates IATA codes in a Google Sheet.

## Prerequisites

- Python 3.x
- Requests library (`pip install requests`)
- Twilio library (`pip install twilio`)

## Setup

1. Clone the repository:

   ```bash
   git clone https://github.com/Olusegun-Light/Python-100-Days-Of-Code
   ```

2. Navigate to the project directory:

   ```bash
   cd Day-40
   ```

3. Set up your environment variables:

   - `YOUR_FLIGHT_SEARCH_API_KEY`: Obtain this from [Tequila API](https://tequila.kiwi.com/)
   - `YOUR_TWILIO_ACCOUNT_SID`: Your Twilio account SID.
   - `YOUR_TWILIO_AUTH_TOKEN`: Your Twilio auth token.
   - `YOUR_TWILIO_VIRTUAL_NUMBER`: Your Twilio virtual number.
   - `YOUR_TWILIO_VERIFIED_NUMBER`: Your Twilio verified number.
   - `YOUR_SHEETY_PRICES_ENDPOINT`: Your Sheety Prices endpoint.

4. Run the main script:

   ```bash
   python main.py
   ```

## How It Works

1. Retrieves destination data from the Sheety API using the `DataManager` class.
2. If IATA codes are missing, uses the `FlightSearch` class to fetch them and updates the Google Sheet.
3. Checks for flight deals using the `FlightSearch` class and sends SMS notifications using the `NotificationManager` class.

## Directory Structure

- **main.py**: Orchestrates data retrieval, updates, and sends notifications.
- **notification_manager.py**: Manages Twilio SMS notifications.
- **flight_search.py**: Utilizes the Tequila API to get IATA codes and check for flight deals.
- **flight_data.py**: Structures the flight data.
- **data_manager.py**: Handles the retrieval and update of data from the Sheety API.

## Acknowledgments

- [Tequila API](https://tequila.kiwi.com/) for providing flight-related data.
- [Twilio](https://www.twilio.com/) for SMS notification services.
- [Sheety](https://sheety.co/) for the API allowing access to Google Sheets as a database.

Feel free to customize and extend this script to suit your flight tracking and notification needs.
