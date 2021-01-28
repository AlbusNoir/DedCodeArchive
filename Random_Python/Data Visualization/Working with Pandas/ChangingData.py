'''
Editing data with Pandas
'''
import pandas as pd

# dataframe
df = pd.read_csv('pokemon_data.csv')

# new col totaling the hp+atk+def+spatk+spdef+speed
df['Total'] = df['HP'] + df['Attack'] + df['Defense'] + df['Sp. Atk'] + df['Sp. Def'] + df['Speed']

# drop columns
df = df.drop(columns=['Total'])  # reset df to be whatever edit you want

print(df.head(5))


# more succint way of adding col
# new column, use iloc specify ALL cols (:) then the cols you want to add, axis=1 means horizontally, 0 is vertically
df['Total'] = df.iloc[:,4:10].sum(axis=1)


# move total column
cols = list(df.columns.values)
df = df[cols[0:4] + [cols[-1]] + cols[4:12]]  # gets 0-4 then last then rest

'''
NOTE: the above doesn't actually modify any data. Refer to SavingChanges.py for saving edits
