from datetime import datetime, timedelta
from bs4 import BeautifulSoup
import requests

user_input = input("When would you like to travel (YYYY-MM-DD format): ")

try:
    travel_date = datetime.strptime(user_input, '%Y-%m-%d')
    date_list = [travel_date.strftime('%Y-%m-%d')]

except ValueError:
    print("Invalid date format. Please use the YYYY-MM-DD format.")


url = "https://www.billboard.com/charts/hot-100/2000-08-12/"

url_request = requests.get(url)
url_request.raise_for_status()

url_request_text = url_request.text


soup = BeautifulSoup(url_request_text, "html.parser")

articel_song_list = soup.select("li ul li h3")

for tag in articel_song_list:
    article_song_list_text = tag.getText()

    print(article_song_list_text.strip())
# print(soup.text)








