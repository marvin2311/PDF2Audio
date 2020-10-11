import pyttsx3
import PyPDF2


# open the book file and initialize the pdf reader
book = open('the_monk_who_sold_his_ferrari.pdf','rb')

pdfReader = PyPDF2.PdfFileReader(book)


# initialize the speaker to convert text to speech, set properties for voice and reading pace
speaker = pyttsx3.init()

speaker.setProperty('voice', "com.apple.speech.synthesis.voice.Alex")
speaker.setProperty('rate',145)


# loop through each page, extract the text and read it (content of the example starts at page 10)
pages = pdfReader.numPages

for num in range(9, pages):

    page = pdfReader.getPage(num)
    text = page.extractText()

    speaker.say(text)
    speaker.runAndWait()


# close the book file
book.close()
