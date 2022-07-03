#api_key = "API FROM:- https://newsapi.org/"
# notification-icon-path = "ICON PATH OF ICO FILE" #.ico file

from plyer import notification as nf  # plyer module
import requests  # request module
import json

# API Link Here From newsapi.org
url = "https://newsapi.org/v2/top-headlines?country=us&category=business&apiKey=4137bd043df24ee5b1768da4ba594597"
gnews = requests.get(url).json()
article = gnews["articles"]

for news in article:
    nt = news['title']  # Fetching Title From API Data.


def notifyMe():
    nf.notify(
        title='News Update',  # Notification Title
        message=nt,  # Message/News
        # .ico Icon File Path
        app_icon=None,
        timeout=8  # Time Out Of Notification
    )



# Running Our Function
if __name__ == "__main__":
    notifyMe()
