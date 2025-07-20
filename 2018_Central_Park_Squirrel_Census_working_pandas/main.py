import pandas
data = pandas.read_csv(r'./2018_Central_Park_Squirrel_Census_working_pandas/2018_Central_Park_Squirrel_Census_-_Squirrel_Data_20250721.csv')
gray_fur_color=len(data[data['Primary Fur Color']=='Gray'])
cinnamon_fur_color=len(data[data['Primary Fur Color']=='Cinnamon'])
black_fur_color=len(data[data['Primary Fur Color']=='Black'])
data_dict = { 'Fur Color': ['Gray','Cinnamon','Black'],
    'Count':[gray_fur_color,cinnamon_fur_color,black_fur_color]}

df = pandas.DataFrame(data_dict)
df.to_csv('./2018_Central_Park_Squirrel_Census_working_pandas/count_of_squirrel.csv')