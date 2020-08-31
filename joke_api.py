import urllib
import json
from urllib.request import urlopen
#import numpy
from tkinter import *

joke = 'https://official-joke-api.appspot.com/random_joke'
morejokes = 'https://official-joke-api.appspot.com/random_ten'


user_agent = 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.9.0.7) Gecko/2009021910 Firefox/3.0.7'

headers={'User-Agent':user_agent,}

class one_joke:
    request=urllib.request.Request(joke,None,headers) #The assembled request
    response = urllib.request.urlopen(request)
    data = json.load(response)
    a = data['setup']
    b = data['punchline']

    def load_joke(self):
        request=urllib.request.Request(joke,None,headers) #The assembled request
        response = urllib.request.urlopen(request)
        data = json.load(response)
        self.a = data['setup']
        self.b = data['punchline']
    def question(self):
        return self.a
    def answer_get(self):
        return self.b


def more_jokes():
    global set_ups
    global punch_lines

    request=urllib.request.Request(morejokes,None,headers) #The assembled request
    response_2 = urllib.request.urlopen(request)
    jokes = json.load(response_2)
    for jokess in jokes:
        pass
        #set_ups.append(jokess['setup'])
        #punch_lines.append(jokess['punchline'])
        #print(jokess['type'],':', jokess['setup'],'\n' ,jokess['punchline'],'\n')


#print("Question: ", set_ups[1], '\n', "Answer: ", punch_lines[1])

somejoke = one_joke()

def new_joke():
    somejoke.load_joke()
    display_joke.config(text=somejoke.question())
    #answer.config(text=answers())

def answers_display():
    answer_display.config(text=somejoke.answer_get())

#widgets


window = Tk()
window.geometry('400x300+230+230')

display_joke = Label(window, text="Joke")
display_joke.pack()
answer = Button(window, bd = 3, text = "Answer!", command = answers_display)
answer.pack()
answer_display = Label(window, text = 'Answer')
answer_display.pack()

new_joke_btn = Button(window, text = "New Joke!", command = new_joke)
new_joke_btn.pack(side= BOTTOM)


window.mainloop()
