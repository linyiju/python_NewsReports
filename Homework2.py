#抓取udn新聞稿後，並存取成mp3檔唸出來
#from __future__ import print_function
import os,requests,webbrowser,sys# Import the OS Module
from bs4 import BeautifulSoup as bs
from gtts import gTTS as gs

def get_draft(url): #收集新聞稿
    resp = requests.get(url)

    if resp.status_code is 200:
        resp.encoding = "UTF-8"
        soup = bs(resp.text,"html.parser")
        scope1 = soup.select("#tab1")
        scope2 = scope1[0].select(".taba")

        hot_lines=[]

        for line in scope2: #集成一個list
             hot_lines.append(line.text)

        return hot_lines#顯示出來的list回傳到hot_lines

def reports(draft): #顯示念出來的東西
     print("大家好! 歡迎來到超蝦新聞")
     i=0
     while i < len(draft):
         print(str("第")+str(i+1)+str("則")+" "+draft[i])
         i+=1

def speech(report): #把草稿轉變成字串
    text ="大家好"+" "+"歡迎來到超蝦新聞"+" "
    i=0
    for news in report:
        text = text+"第"+str(i+1)+"則"+"時間"+news[:2]+"點"+news[3:5]+"分"+news[5:]
        i+=1
    return text

def sound(speak): #轉變成語音檔
    tts=gs(text=speak,lang="zh")
    os.chdir(CheckDir) #更改路徑
    tts.save("MyFirstHomework.mp3")
    webbrowser.open("MyFirstHomework.mp3")

#執行
if __name__ == '__main__':

    CheckDir = input("Enter the name of the directory to check : ")
    print()

    if os.path.exists(CheckDir):  # Checks if the dir exists
        print("The directory exists")
    else:
        print("No directory found for " + CheckDir)  # Output if no directory
        print()
        os.makedirs(CheckDir)  # Creates a new dir for the given name
        print("Directory created for " + CheckDir)

    draft= get_draft("https://udn.com/news/index")
    reports(draft)
    speak = speech(draft)
    sound(speak)
