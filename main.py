from datetime import datetime, timedelta

user_input = input("When would you like to travel (YYYY-MM-DD format): ")

travel_date = datetime.strptime(user_input, '%Y-%m-%d')
date_list = [travel_date.strftime('%Y-%m-%d')]

print(date_list)