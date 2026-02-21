# data downloaded from https://data.cityofnewyork.us/Environment/2018-Central-Park-Squirrel-Census-Squirrel-Data/vfnx-vebw/data_preview
import pandas
data = pandas.read_csv("./2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")
grey_squirrels_count = len(data[data["Primary Fur Color"]== "Gray"])
cinnamon_squirrels_count = len(data[data["Primary Fur Color"]== "Cinnamon"])
black_squirrels_count = len(data[data["Primary Fur Color"]== "Black"])
print(cinnamon_squirrels_count)
print(grey_squirrels_count)
print(black_squirrels_count)

data_dict = {
    "Fur color":["Gray","Cinnamon","Black"],
    "Count": [grey_squirrels_count, cinnamon_squirrels_count, black_squirrels_count]
}

df = pandas.DataFrame(data_dict)
df.to_csv("squirrel_count.csv")