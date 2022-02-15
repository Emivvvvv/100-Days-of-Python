# with open("weather_data.csv", mode="r") as weather_data:
#     data = weather_data.readlines()
#     print(data)

# import csv
#
# with open("weather_data.csv", mode="r") as weather_data:
#     data = csv.reader(weather_data)
#     temperatures = []
#     for row in data:
#         if not row[1] == "temp":
#             temperatures.append(int(row[1]))
#     print(temperatures)

# import pandas
#
# data = pandas.read_csv("weather_data.csv")
# print(data["temp"])

# data_dict = data.to_dict()
# print(data_dict)

# temp_list = data["temp"].to_list()
# print(data["temp"].mean())
# print(data["temp"].max())

# print(data["condition"])
# print(data.condition)

# print(data[data.day == "Monday"])
# print(data[data.temp == data.temp.max()])

# monday = data[data.day == "Monday"]
# # print(monday.condition)
# monday_temp = int(monday.temp)
# monday_temp_F = monday_temp * 9/5 + 32
# print(monday_temp)
# print(monday_temp_F)

# data_dict = {
#     "students": ["Ali", "Veli", "Ayse", "Fatma"],
#     "scores": [76, 56, 65, 31]
# }
# data = pandas.DataFrame(data_dict)
# print(data)
# data.to_csv("new_data.csv")

import pandas

squirel_data = pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")
squirel_fur_color = squirel_data["Primary Fur Color"]
print(squirel_fur_color)
fur_colors_list = squirel_fur_color.to_list()
print(fur_colors_list)

data_dict = {
    "Fur Color": ["gray", "red", "black"],
    "Count": [0, 0, 0]
}

for color in fur_colors_list:
    if color == "Gray":
        data_dict["Count"][0] += 1
    elif color == "Cinnamon":
        data_dict["Count"][1] += 1
    elif color == "Black":
        data_dict["Count"][2] += 1

data = pandas.DataFrame(data_dict)
data.to_csv("squirrel_count.csv")

