# Flight Deals Notifier

This Python script checks for IATA codes in a Google Sheet, it utilizes the Flight Search API to fetch IATA codes for cities and updates the Google Sheet. Additionally, it sends notifications for flight deals.

## Prerequisites

- Python 3.x
- Requests library (`pip install requests`)

## Setup

1. Clone the repository:

   ```bash
   git clone https://github.com/your-username/flight-deals-notifier.git
   ```

2. Navigate to the project directory:

   ```bash
   cd flight-deals-notifier
   ```

3. Set up your environment variables:

   - `YOUR_API_KEY_HERE`: Obtain this from [Tequila API](https://tequila.kiwi.com/)
   - `YOUR ENDPOINT HERE`: Your Sheety Prices endpoint.

4. Run the main script:

   ```bash
   python main.py
   ```

## How It Works

1. The script retrieves destination data from the Sheety API using the `DataManager` class.
2. If the IATA codes are missing, it uses the `FlightSearch` class to fetch them and updates the Google Sheet.
3. Notifications for flight deals are handled by the `NotificationManager` class.

## Directory Structure

- **main.py**: The main script orchestrating data retrieval and updates.
- **notification_manager.py**: Manages notifications for flight deals.
- **flight_search.py**: Utilizes the Tequila API to get IATA codes for cities.
- **flight_data.py**: Structures the flight data.
- **data_manager.py**: Handles the retrieval and update of data from the Sheety API.

## Acknowledgments

- [Tequila API](https://tequila.kiwi.com/) for providing flight-related data.
- [Sheety](https://sheety.co/) for the API allowing access to Google Sheets as a database.

Feel free to customize and extend this script to suit your flight tracking and notification needs.
