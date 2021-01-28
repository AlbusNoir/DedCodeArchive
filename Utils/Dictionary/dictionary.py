# app that will accept a word from user, return the definition of the word
# error handling with word similarities and non-words using difflib

import json
from difflib import get_close_matches

data = json.load(open("data.json"))


# if word entered is word in data.json -> define
# if word is similar but spelled wrong -> look for close match, return first match
# if not word -> error
def translate(w):
    w = w.lower()
    if w in data:
        return data[w]
    elif w.title() in data:  # if "texas" also checks for "Texas"
        return data[w.title()]
    elif w.upper() in data:  # NATO NASA USA -> acronyms
        return data[w.upper()]
    elif len(get_close_matches(w, data.keys())) > 0:
        yn = input("Did you mean %s instead? Enter Y if yes, N if no: " % get_close_matches(w, data.keys())[0])
        if yn == "Y" or yn == "y":
            return data[get_close_matches(w, data.keys())[0]]
        elif yn =="N" or yn == "n":
            return "Unknown word. Please try again"
        else:
            return "Please use Y or N"
    else:
        return "Unknown word. Please try again"


# global variable for word input
word = input("Enter word: ")


output = (translate(word))


# test if more than one definition
# if yes -> put each on own line
#if no -> output
if type(output) == list:
    for item in output:
        print(item)
else:
    print(output)