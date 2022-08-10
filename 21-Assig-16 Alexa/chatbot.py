###############################################################################
#                             CHATBOT                                         #
###############################################################################

## for speech-to-text
import speech_recognition as sr

## for text-to-speech
from gtts import gTTS

## for data
import os
import time


# Build the AI
class ChatBot():
    def __init__(self, name):
        print("--- starting up", name, "---")
        self.name = name

    def speech_to_text(self):
        recognizer = sr.Recognizer()
        with sr.Microphone() as mic:
            print("listening...")
            audio = recognizer.listen(mic)
        try:
            self.text = recognizer.recognize_google(audio)
            print("me --> ", self.text)
            return self.text
        except:
            print("me -->  ERROR")

    
   
       
        
        
  

       
    
ai = ChatBot(name="chatbot")
while True:
        text=ai.speech_to_text()
        print("ai --> ", text)

        details={'one':'Details of roll number one  Academic percentage is 94 and attencedence percentage is 80',
        'two':'Details of roll number two  Academic percentage is 85 and attencedence percentage is 90',
        'three':'Details of roll number three  Academic percentage is 94 and attencedence percentage is 80',
        'four':'Details of roll number four  Academic percentage is 75 and attencedence percentage is 76',
        'five':'Details of roll number four  Academic percentage is 65 and attencedence percentage is 96'
        }
     

        if 'number 1' in text :
            text=details['one']
        elif 'number 2' in text:
            text=details['two']
        elif 'number 3' in text:
            text=details['three']
        elif 'number 4' in text:
            text=details['four']
        elif 'number 5' in text:
            text=details['five']
      
        
        else:
            text=text

        language = 'en'
  

        myobj = gTTS(text=text, lang=language, slow=True) 
  
        myobj.save("output.mp3") 
        # Play the converted file  
        os.system("start output.mp3") 
        time.sleep(8)
        print("----Ready----")

