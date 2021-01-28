'''
Quine:
a program which takes no input and produces a copy of its own source code as its only output

Quine's paradox:
"Yields falsehood when preceded by its quotation" yields falsehood when preceded by its quotation.
'''

# abusing %r
s='s=%r;print(s%%s)';print(s%s)
