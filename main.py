# This program will Dictate your Daily's Breaking News
from win32com.client import Dispatch
import requests
import json
def speak(str):
    speak = Dispatch("SAPI.SpVoice")
    speak.Speak(str)
if __name__ == '__main__':
    speak("Today's main headlines....Let's begin")
    with open("config.json", 'r') as f:
        params = json.load(f)
    url = params["MyAPI"]
    news = requests.get(url).text
    # print(news)
    parsed_news = json.loads(news)
    articles = parsed_news["articles"]
    i = 1
    for lines in articles:
        # print(lines['description'])
        headlines = lines['title']
        print(f"News {i} : {headlines}")
        print(f"visit this to know more about News {i} :{lines['url']}")
        print("\n")
        speak(f"News {i} is {headlines}")
        i += 1
    speak("Thanks..for listening...we will meet you in the next episode")