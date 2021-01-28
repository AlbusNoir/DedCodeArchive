'''
Save edits made to csvs
'''
import pandas as pd

# dataframe
df = pd.read_csv('pokemon_data.csv')

# make totals
df['Total'] = df.iloc[:,4:10].sum(axis=1)

# move totals
cols = list(df.columns.values)
df = df[cols[0:4] + [cols[-1]] + cols[4:12]]

# save
df.to_csv('modified.csv', index=False)  # index=False gets rid of the numbers on the side

# save to excel
df.to_excel('modified.xlsx', index=False)

# to txt. sep = dilimidator
df.to_csv('modified.txt', index=False, sep='t')
