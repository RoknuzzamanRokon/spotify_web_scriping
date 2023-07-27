from datetime import datetime, timedelta

user_input = input("When would you like to travel (YYYY-MM-DD format): ")

try:
    travel_date = datetime.strptime(user_input, '%Y-%m-%d')
    date_list = [travel_date.strftime('%Y-%m-%d')]

except ValueError:
    print("Invalid date format. Please use the YYYY-MM-DD format.")
