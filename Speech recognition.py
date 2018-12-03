#!/usr/bin/env python
# coding: utf-8

# In[ ]:


from easygui import *
import speech_recognition as sr
from time import ctime
import time
import os
import webbrowser
from gtts import gTTS
import pyttsx
import csv
import pandas as pd


 
def recordAudio():
    # Record Audio
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Say something!")
        audio = r.listen(source)
 
    # Speech recognition using Google Speech Recognition
    data = ""
    try:
        # Uses the default API key
        # To use another API key: `r.recognize_google(audio, key="GOOGLE_SPEECH_RECOGNITION_API_KEY")`
        data = r.recognize_google(audio)
        print("You said: " + data)
        speech('You said,' +data)
        
    except sr.UnknownValueError:
        print("Google Speech Recognition, could not understand audio")
        speech('Google Speech Recognition, could not understand, audio.')
       
    except sr.RequestError as e:
        print("Could not request results, from Google Speech Recognition service; {0}".format(e))
        speech('Could not request results, from Google Speech Recognition service.')
    return data
    

def csv_file_read(filepath):
    with open(filepath) as f:
        d = dict(filter(None, csv.reader(f)))
    return d


def name_the_key(dict, key):
    return key, dict[key]
           
#mydict = csv_file_read('voice.csv')
data1=pd.read_csv('D:/c-drive/documents/Python/Voice_Integration/voice.csv')
id_rtf=data1[['report','link']]
mydict = id_rtf.set_index('report')['link'].to_dict()



def find_key(text): 
    #mydict=csv_file_read('voice.csv')
    key_list=mydict.keys()
    data = [key.split(',') for key in mydict.keys()]
    for i in range(0,len(data)):
        x=str(data[i])[2:-2].lower()
        if x in str(text).lower():
            key_pass1=str(data[i])[2:-2]
            print(key_pass1)
            return key_pass1
            break
        else:
            key_pass1="NO"
    return key_pass1   


def AltiViz(data):
    text=data
    #print(text)
    key_pass=find_key(text)
    if key_pass!="NO":
        key_name, value = name_the_key(mydict, key_pass)
        print 'KEY NAME: %s' % key_name
        print 'KEY VALUE: %s' % value
        webbrowser.get("C:/Program Files (x86)/Mozilla Firefox/Firefox.exe %s").open(value, new=0, autoraise=True)
        
        while 1:
            filter_call=recordAudio()
            if "stop" in filter_call.lower():
                main()
            if "quit" in filter_call.lower():
                main()
            if "wait" in filter_call.lower():
                main()    
                        
            if "filter" in filter_call.lower():          
                d=filter_call.split()
                filternumber=len(d)
                if (filternumber==3):
                    v1=value+"&"+d[1]+"="+d[2]
                    webbrowser.get("C:/Program Files (x86)/Mozilla Firefox/Firefox.exe %s").open(v1, new=0, autoraise=True)
                if (filternumber==5):
                    v1=value+"&"+d[1]+"="+d[2]+"&"+d[3]+"="+d[4]
                    webbrowser.get("C:/Program Files (x86)/Mozilla Firefox/Firefox.exe %s").open(v1, new=0, autoraise=True)
            
                       
            else:
                if len(filter_call)>0:
                    if "stop" in filter_call.lower():
                        main()
                    if "quit" in filter_call.lower():
                        main()
                    if "wait" in filter_call.lower():
                        main() 
                    else:
                        AltiViz(filter_call)
        
              
    else:
        if "stop" in text.lower():
            main()
        if "quit" in text.lower():
            main()
        if "wait" in text.lower():
            main() 
            
        value="Not found"
        print("Not Found")
        speech('Report Not found.')
        
    return value
           
def speech(text):
    engine = pyttsx.init()
    engine.say(text)
    engine.setProperty('rate',100)  #120 words per minute
    engine.setProperty('volume',.9) 
    engine.runAndWait()


# initialization

time.sleep(2)

def main():
    while 1:  
        title = "VOICE UI DEMO"
        choices = ["Continue", "Quit"]
        choice = buttonbox("Welcome to Voice Integration?", title, choices)
        if choice == "Quit":
            msgbox("You missed a nice experience", title, ok_button="Back.")
            quit()
        else:
            msgbox("Cool, Have fun", title, ok_button="Start")
            print("Hi, what can I do for you?")
            speech('Hi, what can I do for you?')
            while 1:
                data = recordAudio()
                
                if len(data)>0:
                    AltiViz(data)
      
main()        

