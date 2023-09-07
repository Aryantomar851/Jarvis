import pyttsx3
import datetime
import speech_recognition as sr #pip install speech recognition == speech to mic to text
import smtplib
from secrets import senderemail, epwd, to
from email.message import EmailMessage
import pyautogui
import webbrowser as wb
from time import sleep
import wikipedia
import pywhatkit
import requests
from newsapi import NewsApiClient
import clipboard
import os
import pyjokes
import time as tt
import string
import random
import psutil
from nltk.tokenize import word_tokenize


engine = pyttsx3.init()
def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def getvoices(voice):
    voices  = engine.getProperty('voices')
    if voice == 1:
        engine.setProperty('voice',voices[0].id)
        speak("hello this is Jarvis")

    if voice == 2:
        engine.setProperty('voice',voices[1].id)
        speak("hello this is Friday")
    
   

def time():
    Time = datetime.datetime.now().strftime("%I:%M:%S")# hour = I minutes = M minutes = S seconds
    speak("the current time is:")
    speak(Time)

def date():
    year = int(datetime.datetime.now().year)
    month = int(datetime.datetime.now().month)
    date = int(datetime.datetime.now().day)
    speak("the current date is:")
    speak(date)
    speak(month)
    speak(year)

def greeting():
    hour = datetime.datetime.now().hour
    if(hour >= 6 and hour < 12):
        speak("good morning sir!")
    elif hour >= 12 and hour <18 :
        speak("Good afternoon sir!")
    elif hour >= 18 and hour< 24:
        speak("Good evening sir!") 
    else:
        speak("Good Night sir!")

def wishme():
    speak("Welcome back sir!")
    time()
    date()
    greeting()
    speak("jarvis at your service , please tell me how can i help you?")
# while True:
#     voice = int(input("Press 1 for male\nPress 2 for female\n"))
#         #     speak(audio)
#     getvoices(voice)
# time()
# date()
#wishme()
def takeCommandMIC():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)
    try:
        print("Recognizning...")
        query = r.recognize_google(audio , language="en-IN")
        print(query)
    except Exception as e:
        print(e)
        speak("Say that again Please...")
        return "None"
    return query


def takeCommandCMD():
    query = input("please tell me how can i help you?\n ")
    return query

def sendEmail(receiver, subject, content):
    server = smtplib.SMTP('smtp.gmail.com',587)
    server.starttls()
    server.login(senderemail, epwd)
    email = EmailMessage()
    email['From'] = senderemail
    email['To'] = receiver
    email['Subject'] = subject
    email.set_content(content)
    server.send_message(email)
    server.close()

def sendwhatsmsg(phone_no, message):
    Message = message;
    wb.open('https://web.whatsapp.com/send?phone='+8516827035+'&text='+Message)
    sleep(10)
    pyautogui.press('enter')

def searchgoogle():
    speak('what should i search?')
    search = takeCommandMIC()
    wb.open = ('https://www.google.com/search?q='+search)

def news():
    newsapi = NewsApiClient(api_key='0b63ee0fa998475b89b65576704962cb')
    speak('what topic you need the new about?')
    topic = takeCommandMIC()
    data = newsapi.get_top_headlines(q=topic,
                                     language ='en',
                                     page_size = 5)
    newsdata = data['articles']
    for x,y in enumerate(newsdata):
        print(f'{x}{y["description"]}')
        speak((f'{x}{y["description"]}'))

    speak("that's it for now i'll update you in some time")

def text2speech():
    text = clipboard.paste()
    print(text)
    speak(text)

def screenshot():
    name_img = tt.time()
    name_img = f'C:\\New folder\\mw\\Jarvis\\screenshot\\{name_img}.png'
    img = pyautogui.screenshot(name_img)
    img.show()

def passwordgen():
    s1 = string.ascii_uppercase
    s2 = string.ascii_lowercase
    s3 = string.digits
    s4 = string.punctuation

    passlen = 8
    s = []
    s.extend(list(s1))
    s.extend(list(s2))
    s.extend(list(s3))
    s.extend(list(s4))

    random.shuffle(s)
    newpass = ("".join(s[0:passlen]))
    print(newpass)
    speak(newpass)

def flip():
    speak("okay, sir flipping a coin ")
    coin = ['head', 'tails']
    toss = []
    toss.extend(coin )
    random.shuffle(toss)
    toss = ("".join(toss[0]))
    speak("i flipped he coin and you get"+ toss)

def roll():
    speak("okay sir, rolling a die for you")
    die = ['1','2','3','4','5','6']
    roll = []
    roll.extend(die)
    random.shuffle(roll)
    roll = ("".join(roll[0]))
    speak("i rolled a die and you get"+roll)

def cpu():
    usage = str(psutil.cpu_percent())
    speak('CPU is at' + usage)
    battery = psutil.sensors_battery()
    speak("Battery is at ")
    speak(battery.percent)







#http://api.openweathermap.org/data/2.5/weather?q=bhopal&units=imoerial&appid=eb7db6ffc5736668e125e103bf80c725

if __name__ == "__main__":
        getvoices(1)
        # wishme()
        while True:
            query = takeCommandMIC().lower()
            query = word_tokenize(query)
            print(query)
            wakeword = "jarvis"
            if wakeword in query:
                if 'time' in query:
                    time()
                elif 'date' in query:
                    date()
                elif 'email' in query:
                    email_list = {
                        'test mail': 'qwrlbyouuudujmmiuq@bbitj.com'
                    }
                    try:
                        speak("To whom want to send mail?")
                        name = takeCommandMIC()
                        receiver = email_list[name]
                        speak("what is the subject of the mail?")
                        subject = takeCommandMIC()
                    
                        speak('what should i say?')
                        content = takeCommandMIC()
                        sendEmail(receiver,subject,content)
                        speak("email has been send")
                    except Exception as e:
                        print(e)
                        speak("unable to send email")
                elif 'message' in query:
                    user_name = {
                        'Jarvis': '8516827035'
                    }
                    try:
                        speak("To whom want to send whatsApp Message?")
                        name = takeCommandMIC()
                        phone_no = user_name[name]
                        speak("what is the message?")
                        message = takeCommandMIC()
                        sendwhatsmsg(phone_no,message)
                        speak("message has been send")
                    except Exception as e:
                        print(e)
                        speak("unable to send WhatsApp Message")

                elif 'wikipedia' in query:
                    speak('searching on wikipedia...')
                    query = query.replace("wikipedia","")
                    result = wikipedia.summary(query,sentences = 2)
                    print(result)
                    speak(result)
                
                elif 'search' in query:
                    searchgoogle()

                elif 'youtube' in query:
                    speak("What should i search for on youtube")
                    topic = takeCommandMIC()
                    pywhatkit.playonyt(topic)

                elif 'weather' in query:
                    city = 'bhopal'
                    url = f'http://api.openweathermap.org/data/2.5/weather?q={city}&units=imoerial&appid=eb7db6ffc5736668e125e103bf80c725'
                    res = requests.get(url)
                    data = res.json()

                    weather = data['weather'] [0] ['main']  
                    temp = data['main']['temp']
                    desp = data['weather'] [0] ['description']
                    temp = round((temp - 32) * 5/9)
                
                    print(weather)
                    print(temp)
                    print(desp)
                    print(f'weather in {city} city is like' )
                    speak('Temperature : {} degree celcius'.format(temp))
                    speak('weather is {}'.format(desp))

                elif 'news' in query :
                    news()

                elif 'read' in query :
                    text2speech()
                
                elif 'open code' in query:
                    codepath = 'C:\\New folder\\mw\\java.exe'
                    os.startfile(codepath)
                
                elif 'open ' in query:
                    os.system('explorer C://{}'.format(query.replace('Open','')))
                elif 'joke' in query:
                    speak(pyjokes.get_joke())
                elif 'screenshot' in query:
                    screenshot()
                elif 'remember that' in query:
                    speak("what should i remember?")
                    data = takeCommandMIC()
                    speak("you said to me remember that"+data)
                    remember = open('data.txt','w')
                    remember.write(data)
                    remember.close()
                
                elif'do you know anything' in query:
                    remember = open('data.txt','r')
                    speak("you told me to remember that"+ remember.read())
                
                elif 'password' in query:
                    passwordgen()

                elif 'flip' in query :
                    flip()
                elif 'roll' in query:
                    roll()

                elif 'cpu' in query:
                    cpu()

                    
                    
                elif 'offline' in query:
                    quit()

