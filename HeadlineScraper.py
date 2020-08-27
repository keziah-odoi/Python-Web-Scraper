import tkinter as tk
from PIL import ImageTk, Image
from bs4 import BeautifulSoup
import requests

#**************Scraping Site**************************#
newsHeadline = ""
newsTemp = ""

def getGoogle(url):
    newURL = 'https://'+url
    source = requests.get(newURL).text
    soup = BeautifulSoup(source, 'html.parser')
    headline = ""
    for article in soup.select('item'):
        headline += (str(article.title.text)+"\n")
    label['text'] = headline
    print(headline)
    global newsTemp
    newsTemp = headline
    return newsTemp

def getAljazeera(url):
    newURL = 'https://'+url
    source = requests.get(newURL).text
    soup = BeautifulSoup(source, 'html.parser')
    headline = ""
    for article in soup.find_all('div', attrs={'class': 'col-sm-4 queen-btm-story story-default-sec'}):
        headline += (str(article.h2.text)+"\n")
    label['text'] = headline
    print(headline)
    global newsTemp
    newsTemp = headline
    return newsTemp


def parentSearch(url):
    if str(url) == "news.google.com/news/rss":
        getGoogle(url)
    elif str(url) == "aljazeera.com":
        getAljazeera(url)
    else:
        print("URL not included!")
        label['text'] = "Sorry, headlines cannot be retrieved"


def exportTXT():
    global newsTemp
    textFile = open("Headlines.txt", "w")
    textFile.write("HEADLINES\n")
    textFile.write(newsTemp)
    textFile.close()

#***********************************TKINTER CODE*******************************************
HEIGHT = 500
WIDTH = 600
root = tk.Tk()
canvas = tk.Canvas(root, height=HEIGHT, width = WIDTH)
canvas.pack()

root.title("Headline Grabber")
root.tk.call('wm', 'iconphoto', root._w, ImageTk.PhotoImage(Image.open(r"newspaper-icon.png")))

backgroundImage = ImageTk.PhotoImage(Image.open(r"newspaper.jpg"))
backgroundLabel = tk.Label(root, image=backgroundImage)
backgroundLabel.place(relwidth=1, relheight=1)

frame = tk.Frame(root, bg= '#faaf3e', bd=5)
frame.place(relx = 0.5, rely= 0.1, relwidth = 0.75, relheight=0.1, anchor='n')
inputURl = tk.Entry(frame)
inputURl.place(relwidth = 0.65, relheight=1)

button =  tk.Button(frame, text="Get Headlines", command=lambda:parentSearch(inputURl.get()))
button.place(relx=0.7, relheight=1, relwidth=0.3)

lower_frame = tk.Frame(root, bg="#faaf3e", bd=10)
lower_frame.place(relx=0.5, rely=0.21, relwidth=0.74, relheight=0.6, anchor='n')

label = tk.Label(lower_frame)
label.place(relwidth=1, relheight=1)

exportTXTbutton = tk.Button(root, text="Export to notepad ", command=lambda:exportTXT())
exportTXTbutton.place(relx = 0.57, rely=0.9, relwidth = 0.3, relheight =0.07)

root.mainloop()