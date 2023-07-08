# Weather Data Analysis and Squirrel Census

This repository contains Python code for analyzing weather data and performing analysis on squirrel census data. The code is organized as follows:

## Files

- `main.py`: The main Python script that performs data analysis on weather data and squirrel census data.
- `weather_data.csv`: A CSV file containing weather data.
- `2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv`: A CSV file containing squirrel census data.
- `new_data.csv`: A CSV file generated from the analysis.

## Weather Data Analysis

The code in `main.py` demonstrates the analysis of weather data using the `csv` and `pandas` libraries. It performs the following tasks:

1. Reads weather data from `weather_data.csv` using the `csv` library and prints the temperatures.
2. Reads weather data from `weather_data.csv` using the `pandas` library and prints the temperatures.
3. Converts the weather data to JSON format using the `to_json()` method.
4. Converts the temperature data to a list using the `to_list()` method.
5. Calculates the mean temperature using the `mean()` method.
6. Finds the maximum temperature using the `max()` method.
7. Retrieves rows with specific conditions, such as filtering data for a specific day or finding the row with the maximum temperature.
8. Converts temperature from Celsius to Fahrenheit for a specific day.
9. Creates a new data frame from scratch using a dictionary.
10. Saves the new data frame to a CSV file named `new_data.csv`.

## Squirrel Census Analysis

The code in `main.py` also includes an analysis of squirrel census data. It performs the following tasks:

1.Reads squirrel census data from `2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv` using the `pandas` library. 2. Counts the number of grey, red, and black squirrels in the census data. 3. Stores the squirrel count data in a dictionary. 4. Creates a data frame from the squirrel count data. 5. Saves the squirrel count data to a CSV file named `squirrel_count.csv`.

Feel free to explore the code and adapt it to your needs!
