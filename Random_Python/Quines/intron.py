'''
Quine:
a program which takes no input and produces a copy of its own source code as its only output

Quine's paradox:
"Yields falsehood when preceded by its quotation" yields falsehood when preceded by its quotation.

Intron:
code you can inject within a quine that will replicate as part of the replication
but does not actually contribute directly to the function of the quine.
IT'S A FREE LOADER

------------------------------------------------------------------------------------

intron that takes input from user and adds it as input into the quine
neat thing here is that is you don't enter anything, it just prints itself
if you do enter something, it will inject and then print itself, thus, intron quine
so really, if you copy what you get after input back into term and run, it will produce itself
'''

t='';s='t=input() or t;\
print(f"t={repr(t)};s={repr(s)};\
exec(s)#{t}")';exec(s)#