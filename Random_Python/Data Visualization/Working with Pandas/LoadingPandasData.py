'''
Working with Pandas - loading data
'''
import pandas as pd

# dataframe
df = pd.read_csv('pokemon_data.csv')

# testing load
# print(df.head(3))
# print(df.tail(3))

'''
 Can also use:
 pd.read_excel for excel
 pd.read_csv('pokemon_data.txt', delimeter='\t') for txt
 '''
