'''
Quine:
a program which takes no input and produces a copy of its own source code as its only output

Quine's paradox:
"Yields falsehood when preceded by its quotation" yields falsehood when preceded by its quotation.
'''

# this one is cheating. nothingness always results in nothingness so like meh
# this literally just puts the code in a file then reads the file back
# it's not self sustaining
print(open(__file__).read())