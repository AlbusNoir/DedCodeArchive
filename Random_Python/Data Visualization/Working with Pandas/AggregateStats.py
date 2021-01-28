'''
Using pandas for aggregate stats
'''
import pandas as pd

df = pd.read_csv('modified.csv')

# look for averages by Type 1 sorted by Defense stat
df.groupby(['Type 1']).mean().sort_values('Defense', ascending=False)

# three main agstats you can do with groupby is mean, sum, count

# summize all stats of Type 1
df.groupby(['Type 1']).sum()

# clean up counts. Fills a col and adds to df and sets to 1
df['count'] = 1

# count how many per Type 1
df.groupby(['Type 1']).count()['count']

# this will pull the count col and the Type 1 to show something like Bug 69, Dark 31, etc

# pull subsets with Type 1 and Type 2
df.groupby(['Type 1', 'Type 2']).count()['count']

# of type 1 bug, 2 have type 2 or electric etc

# limit chunksize. Only 5 rows passed in at a time
for df in pd.read_csv('modified.csv', chunksize=5):
    print('CHUNK DF')
    print(df)

# putting that into practice
new_df = pd.DataFrame(columns=df.columns)

for df in pd.read_csv('modified.csv', chunksize=5):
    results = df.groupby(['Type 1']).count()

    new_df = pd.concat([new_df, results]) # takes new df, appends results, stores

# final new df is a smaller, sorted df by Type 1 counted
