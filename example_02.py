# from datetime import datetime, timedelta
#
# user_input = input("When would you like to travel (YYYY-MM-DD format): ")
#
# try:
#     # Convert user input to a datetime object
#     travel_date = datetime.strptime(user_input, '%Y-%m-%d')
#
#     # Create a list to store the dates
#     date_list = []
#
#     # Add the first date to the list
#     date_list.append(travel_date.strftime('%Y-%m-%d'))
#
#     # Generate the next 9 dates and add them to the list
#     for i in range(9):
#         travel_date += timedelta(days=1)
#         date_list.append(travel_date.strftime('%Y-%m-%d'))
#
#     print(date_list)
#
# except ValueError:
#     print("Invalid date format. Please use the YYYY-MM-DD format.")


from bs4 import BeautifulSoup
import requests

date = input("Which year do you want to travel to? Type the date in this format YYYY-MM-DD: ")

response = requests.get("https://www.billboard.com/charts/hot-100/" + date)

soup = BeautifulSoup(response.text, 'html.parser')
song_names_spans = soup.select("li ul li h3")

song_names = [song.getText().strip() for song in song_names_spans]
print(song_names)