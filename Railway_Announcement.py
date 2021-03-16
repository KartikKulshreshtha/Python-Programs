import os
import pandas as pd

# Python provides a module called pydub to work with audio files.
from pydub import AudioSegment

# Python provides a module called pydub to work with audio files.
from gtts import gTTS

# This Function converts our text to audio

from playsound import playsound


def TextToSpeech(text, filename):
    myText = str(text)
    language = 'en-in'
    myObj = gTTS(text=myText, lang=language, slow=True)
    myObj.save(filename)

# This Function returns pydub audio segment


def mergeAudios(audios):
    combined = AudioSegment.empty()
    for audio in audios:
        combined += AudioSegment.from_mp3(audio)
    return combined



# This function Generates skeleton of whole project
def generateskeleton():
    # 1 - Generate Kripya dhayn de
    audio = AudioSegment.from_mp3('Railway.mp3')
    start = 1000
    finish = 3100
    audioProcessed = audio[start:finish]
    audioProcessed.export('1_hindi.mp3', format="mp3")

    # 2 Generating Gadi sankhya
   # audio = AudioSegment.from_mp3('Railway.mp3')
    #start = 2800
    #finish = 7000
    #audioProcessed = audio[start:finish]
    #audioProcessed.export('2_hindi.mp3', format="mp3")

    # 3 - from-city
    #audio = AudioSegment.from_mp3('Railway.mp3')
    #start = 7000
    #finish = 7600
    #audioProcessed = audio[start:finish]
    #audioProcessed.export('3_hindi.mp3', format="mp3")

    # 4 Via
    #audio = AudioSegment.from_mp3('Railway.mp3')
    #start = 7700
    #finish = 8300
    #audioProcessed = audio[start:finish]
    #audioProcessed.export('4_hindi.mp3', format="mp3")

    # 5 - Generate se chal kr
    audio = AudioSegment.from_mp3('Railway.mp3')
    start = 8200
    finish = 9300
    audioProcessed = audio[start:finish]
    audioProcessed.export('5_hindi.mp3', format="mp3")

    # 6 Generate To-city
    #audio = AudioSegment.from_mp3('Railway.mp3')
    #start = 8900
    #finish = 10250
    #audioProcessed = audio[start:finish]
    #audioProcessed.export('6_hindi.mp3', format="mp3")

    # 7 Ko jane wali
    audio = AudioSegment.from_mp3('Railway.mp3')
    start = 10150
    finish = 11100
    audioProcessed = audio[start:finish]
    audioProcessed.export('7_hindi.mp3', format="mp3")

    # 8 Apne nirdharit samay
    audio = AudioSegment.from_mp3('Railway.mp3')
    start = 11200
    finish = 12500
    audioProcessed = audio[start:finish]
    audioProcessed.export('8_hindi.mp3', format="mp3")

    # 9 Time
    #audio = AudioSegment.from_mp3('Railway.mp3')
    #start = 12700
    #finish = 15500
    #audioProcessed = audio[start:finish]
    #audioProcessed.export('9_hindi.mp3', format="mp3")

    # 10 Par
    audio = AudioSegment.from_mp3('Railway.mp3')
    start = 15700
    finish = 16200
    audioProcessed = audio[start:finish]
    audioProcessed.export('10_hindi.mp3', format="mp3")

    # 11 Only Platform
    audio = AudioSegment.from_mp3('Railway.mp3')
    start = 16300
    finish = 17400
    audioProcessed = audio[start:finish]
    audioProcessed.export('11_hindi.mp3', format="mp3")

    # 12 Platform Number
    #audio = AudioSegment.from_mp3('Railway.mp3')
    #start = 17500
    #finish = 18100
    #audioProcessed = audio[start:finish]
    #audioProcessed.export('12_hindi.mp3', format="mp3")

    # 13 Generating aa rhi h
    audio = AudioSegment.from_mp3('Railway.mp3')
    start = 18200
    finish = 21000
    audioProcessed = audio[start:finish]
    audioProcessed.export('13_hindi.mp3', format="mp3")


def generateAnnouncement(filename):
    FILE = []
    # It reads the data from the database(Excel file)
    df = pd.read_excel(filename)
    # It reads the data one by one using iterrows function in pandas
    for index, item in df.iterrows():
        # 2 Generating Gadi sankhya
        TextToSpeech(item['train_no'] +" " + item['train_name'],'2_hindi.mp3')
        # 3 Generating from-ci(item
        TextToSpeech(item['from'],'3_hindi.mp3')
        # 4 Generating Via
        TextToSpeech(item['via'],'4_hindi.mp3')
        # 6 Generating To-city
        TextToSpeech(item['to'],'6_hindi.mp3')
        # 9 Generating Time
        TextToSpeech(item['time'],'9_hindi.mp3')
        # 12 Platform Number
        TextToSpeech(item['platform'],'12_hindi.mp3')

        audios = [f"{i}_hindi.mp3" for i in range(1,14)]
        announcement = mergeAudios(audios)
        FILE.append(announcement.export(f"anouncement_{item['train_no']}_{index+1}.mp3", format="mp3"))
    return str(FILE)

def PlaySound(func):
    for audio in func:
        playsound(audio)


if __name__ == '__main__':
    print("Generating skeleton....")
    generateskeleton()
    print("Now Generating Announcement...")
    func = generateAnnouncement("announcement.xlsx")
    print(func)
    PlaySound(func)