from youtube_search import YoutubeSearch
from googlesearch import search
import webbrowser
import talk as t
import json

def play(text):
    try:
        results = YoutubeSearch(text, max_results=1).to_json()
        if results is None:
            t.talk("Sory, I can't find video named " + text)
            return
        results = json.loads(results)
        video_id = results['videos'][0]['id']
        url = 'https://www.youtube.com/watch?v=' + str(video_id)
        webbrowser.open(url, new=0, autoraise=True)
        t.talk("Okey, now playing " + text)
        print("Now playing " + text)
    except:
        t.talk("Sory, I can't find video named " + text)

def srch(text):
    result = search(text)
    webbrowser.open(result[0], new=0, autoraise=True)
    t.talk('Searching for ' + text)
    print('Searching for ' + text)
