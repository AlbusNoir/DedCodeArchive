'''
Quine:
a program which takes no input and produces a copy of its own source code as its only output

Quine's paradox:
"Yields falsehood when preceded by its quotation" yields falsehood when preceded by its quotation.
'''

exec(s:='print("exec(s:=%r)"%s)')