# read pdf contents outloud
import pyttsx3
import PyPDF2

# Ref: https://pypi.org/project/pyttsx3/ & https://pyttsx3.readthedocs.io/en/latest/
speaker = pyttsx3.init()

# adjust read speed
speaker.setProperty('rate', 140)  # sets rate to x words per minute (default is 200)

# set up pdf reader
book = open('{put your pdf title here}', 'rb')  # open book as binary book
print(f'Book: {book.name}')
pdfReader = PyPDF2.PdfFileReader(book)
pages = pdfReader.getNumPages()
print(f'Total pages: {pages}')
st = int(input('Enter page to start on: '))  # this gives you the option to skip the index and stuff

# audio
for pg in range(st, pages):
    page = pdfReader.getPage(pg)
    text = page.extractText()
    speaker.say(text)
    speaker.runAndWait()
