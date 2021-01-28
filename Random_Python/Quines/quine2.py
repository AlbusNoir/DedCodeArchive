'''
Quine:
a program which takes no input and produces a copy of its own source code as its only output

Quine's paradox:
"Yields falsehood when preceded by its quotation" yields falsehood when preceded by its quotation.
'''

a='a=%s%s%s;print(a%%(chr(39),a,chr(39)))';print(a%(chr(39),a,chr(39)))
b='b={}{}{};print(b.format(chr(39),b,chr(39)))';print(b.format(chr(39),b,chr(39)))
c='c=%r;print(c%%c)';print(c%c)