# from datetime import datetime, timedelta
#
# user_input = input("When would you like to travel (YYYY-MM-DD format): ")
#
# travel_date = datetime.strptime(user_input, '%Y-%m-%d')
# date_list = [travel_date.strftime('%Y-%m-%d')]
#
# print(date_list)


from datetime import datetime, timedelta

user_input = input("When would you like to travel (YYYY-MM-DD format): ")

travel_date = datetime.strptime(user_input, '%Y-%m-%d')
date_list = [travel_date.strftime('%Y-%m-%d')]
print(date_list)

# Extract individual components (year, month, day) from travel_date and print them
year = travel_date.year
month = travel_date.month
day = travel_date.day
print(year, month, day)









