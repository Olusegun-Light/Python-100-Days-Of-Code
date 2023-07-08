# Using the csv library
import csv

with open("weather_data.csv") as data_file:
    datas = csv.reader(data_file)
    temperatures = []
    for row in datas:
        if row[1] != "temp":
            temperatures.append(int(row[1]))
        print(temperatures)


# Using the Panda library
import pandas

data_1 = pandas.read_csv("weather_data.csv")
print(data_1["temp"])

# Convert data to json with pandas
data_json = data_1.to_json()
print(data_json)

# Convert data to list
temp_list = data_1["temp"].to_list()
print(temp_list)

# Mean
temp_mean = data_1["temp"].mean()
print(temp_mean)

# Max Number
temp_max = data_1["temp"].max()
print(temp_max)

# Get Row
print(data_1[data_1.day == "Monday"])
print(data_1[data_1.temp == data_1.temp.max()])

# Get temp and convert to Fahrenheit
monday = data_1[data_1.day == "Monday"]
monday_temp = int(monday.temp)
monday_temp_F = monday_temp * 9/5 + 35
print(monday_temp_F)

# #  Create a data frame from scratch
data_dict = {
    "students": ["Amy", "James", "Angel"],
    "grades": [78, 54, 88]
}
data1 = pandas.DataFrame(data_dict)

# # Convert and save data to csv
data1.to_csv("new_data.csv")

data = pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")
grey_squirrels_count = len(data[data["Primary Fur Color"] == "Gray"])
red_squirrels_count = len(data[data["Primary Fur Color"] == "Cinnamon"])
black_squirrels_count = len(data[data["Primary Fur Color"] == "Black"])
print(grey_squirrels_count)
print(red_squirrels_count)
print(black_squirrels_count)

data_dict = {
    "Fur Color": ("Gray", "Cinnamon", "Black"),
    "Count": (grey_squirrels_count, red_squirrels_count, black_squirrels_count)
}

df = pandas.DataFrame(data_dict)
df.to_csv("squirrel_count.csv ")
