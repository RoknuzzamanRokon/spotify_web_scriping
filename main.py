from datetime import datetime, timedelta
from bs4 import BeautifulSoup
import requests

user_input = input("When would you like to travel (YYYY-MM-DD format): ")


url = "https://www.billboard.com/charts/hot-100/"

url_request = requests.get(url + user_input)


url_request_text = url_request.text


soup = BeautifulSoup(url_request_text, "html.parser")

articel_song_list = soup.select("li ul li h3")

for tag in articel_song_list:
    article_song_list_text = tag.getText()

    print(article_song_list_text.strip())
# print(soup.text)

client_id = "f18610a8146140bab0c9f785979949ed"


client = "0377bee00d6e4406a60474ab78cf1bf1"





