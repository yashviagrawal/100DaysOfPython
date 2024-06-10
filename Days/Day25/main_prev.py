import pandas
import pandas as pd
# import csv
#
# with open("wd.csv") as data_file:
#     data = csv.reader(data_file)
#     for row in data:
#         print(row)
#
# data = pd.read_csv("wd.csv")
#
# #aveage tmep normal
# temp_list = data['temp'].to_list()
# temp_avg = sum(temp_list)/len(temp_list)
# print(temp_avg)
# #using pandas
# temp_avg = data['temp'].mean()
# print(temp_avg)
#
# print(data[data.condition=="Sunny"])
#
# #CREATE  A DATAFRAME
#
# data_dict = {
#     "students": ["Amy", "James", "Angela"],
#     "scores": [76, 56, 65]
# }
#
# data = pandas.DataFrame(data_dict)
# print(data)
# data.to_csv("student.csv")

data = pd.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")
grey = len(data[data["Primary Fur Color"] == "Gray"])
red = len(data[data["Primary Fur Color"] == "Cinnamon"])
black = len(data[data["Primary Fur Color"] == "Black"])

data_dict = {
    "Fur Color": ["Gray", "Cinnamon", "Black"],
    "Count": [grey, red, black]
}

new = pd.DataFrame(data_dict)
new.to_csv("new.csv")
print(new)