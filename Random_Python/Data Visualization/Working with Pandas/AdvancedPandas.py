'''
More advanced pandas concepts
'''
import pandas as pd

df = pd.read_csv('pokemon_data.csv')

# display only grass type & Grass|X
df.loc[df['Type 1'] == 'Grass']

# display Grass & Poison
df.loc[(df['Type 1'] == 'Grass') & (df['Type 2'] == 'Poison')]

# display type 1 Grass OR Type 2 Poison
df.loc[(df['Type 1'] == 'Grass') | (df['Type 2'] == 'Poison')]

# type1 grass type 2 poison hp more than 70
new_df = df.loc[(df['Type 1'] == 'Grass') & (df['Type 2'] == 'Poison') & (df['HP'] > 70)]

# can set each of the above to a new df with var = statement (i.e. new_df = df.loc[...])
# can also save the new df's same way as the reg df

# new_df.to_csv('filtered.csv')

# reset index so it's 0, 1, 2, ...
new_df = new_df.reset_index()

# by default, old index saved in new col. To get rid of this do
new_df = new_df.reset_index(drop=True)

# if you want to conserve memory, the above can be done in place
new_df.reset_index(drop=True, inplace=True)

# filter out 'Mega'
df.loc[df['Name'].str.contains('Mega')]

# everything except 'Mega', use ~ not
df.loc[~df['Name'].str.contains('Mega')]

# using regex to filter
import re

# filter type1 is fire or grass without worrying about case (re.I -> ignore case)
df.loc[df['Type 1'].str.contains('fire|grass', flags=re.I, regex=True)]

# only pokemon starting with 'Pi'
df.loc[df['Name'].str.contains('^pi[a-z]*', flags=re.I, regex=True)]

# reading above regex: start of line is 'pi' followed by nothing or a-z


# change Type 1 Fire to Type 1 Flamer
df.loc[df['Type 1'] == 'Fire', 'Type 1'] = 'Flamer'

# do reverse to change back

# set all fire types to legendary
df.loc[df['Type 1'] == 'Fire', 'Legendary'] = True

# changing multiple parameters
df.loc[df['Total'] > 500, ['Generation', 'Legendary']] = 'TEST'
