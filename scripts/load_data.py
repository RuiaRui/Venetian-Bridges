import pandas as pd
from string import digits
import re

#filename = 'Ponte_San_polo.txt'
filename='PONTE_SC'
with open(filename) as f:
    lines = f.readlines()

i = 0
list_whole = []
list_one = []
for l in lines:
    list_one.append(l)
    i += 1
    if i % 5 == 0:
        list_whole.append(list_one)
        list_one = []

print(list_whole)
df = pd.DataFrame(list_whole)
print(df)
df.columns = ['name', 'river', 'street', 'district', 'id']
df = df.replace('\n', '', regex=True)
df['name']=df.name.apply(lambda x : re.sub(r'[0-9]+', '', x))

df=df.sort_values('name')
df.to_csv('Ponte_San_Croce.csv')