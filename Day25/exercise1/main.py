

## Reading file line by line
#with open("weather_data.csv", "r") as weather_data_file:
#    data = weather_data_file.readlines()
#    print(data)

## Reading csv file using csv library
#import csv
#with open("weather_data.csv", "r") as csvfile:
#    data = csv.reader(csvfile)
#    print(data)
#    temperatures =[]
#    for row in data:
#        if row[1] != "temp":
#            temperatures.append(int(row[1])) # saves only temperatures as integers
#        # print(row) # example of row output ['Monday', '12', 'Sunny']
#
#    print(temperatures)

## Reading csv file using Pandas library
import pandas
import math


data = pandas.read_csv("./weather_data.csv")
# If we want to print out all data
print(data)
# Output:
#         day  temp condition
#0     Monday    12     Sunny
#1    Tuesday    14      Rain
#2  Wednesday    15      Rain
#3   Thursday    14    Cloudy
#4     Friday    21     Sunny
#5   Saturday    22     Sunny
#6     Sunday    24     Sunny

# If we want to print only one row named temp
print(data['temp'])
# Output:
#0    12
#1    14
#2    15
#3    14
#4    21
#5    22
#6    24
#Name: temp, dtype: int64

# Get average temperature
# The old way
#avg = sum(data['temp'].to_list()) / len(data['temp'].to_list())
#print(avg) # result: 17.428571428571427
# using pandas Series.mean
print(data["temp"].mean()) # result: 17.428571428571427
# Get max temperature
print(data["temp"].max()) # result: 24
# Get data in row where day is Monday
print(data[data.day == "Monday"])
# result
#      day  temp condition
#0  Monday    12     Sunny

# get data in row where temperature is max
print(data[data.temp == data.temp.max()])
#result
#      day  temp condition
#6  Sunday    24     Sunny

# insert data
data_dict = {"students" : ["Amy", "James", "Angela"], "scores" : [79, 56, 65]}
data = pandas.DataFrame(data_dict)
print(data)
#result
#  students  scores
#0      Amy      79
#1    James      56
#2   Angela      65