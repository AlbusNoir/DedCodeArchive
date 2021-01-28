'''
Reading data in Pandas
'''
import pandas as pd

df = pd.read_csv('pokemon_data.csv')

# Read headers
print(df.columns)

# Read each column
print(df['Name'][0:5])  # gives top 5 names
print(df[['Name','Type 1', 'HP']])  # gives three columns

# Read each row
print(df.iloc[1])  # integer location of 1 = row 1
print(df.iloc[0:4])  # int location of first 4

for index, row in df.iterrows():
    print(index, row)


print(df.loc[df['Type 1'] == "Fire"])  # locates certain stuff

# Read a specified location(R,C)
print(df.iloc[2,1])  # specific row,column


# other stuff
df.describe() # gives info about mean, median, etc

df.sort_values('Name', ascending=False) # sort in reverse alpha order
 df.sort_values(['Type 1', 'HP'], ascending=[1,0])  # sorts by type 1 ascending, hp descending
