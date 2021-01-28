import random


quotes = []

f = open('quoteslist.txt', 'r')

for line in f:
    quotes.append(line)

quote = random.choice(quotes)

print(quote)
