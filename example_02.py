from datetime import datetime, timedelta

user_input = input("When would you like to travel (YYYY-MM-DD format): ")

try:
    # Convert user input to a datetime object
    travel_date = datetime.strptime(user_input, '%Y-%m-%d')

    # Create a list to store the dates
    date_list = []

    # Add the first date to the list
    date_list.append(travel_date.strftime('%Y-%m-%d'))

    # Generate the next 9 dates and add them to the list
    for i in range(9):
        travel_date += timedelta(days=1)
        date_list.append(travel_date.strftime('%Y-%m-%d'))

    print(date_list)

except ValueError:
    print("Invalid date format. Please use the YYYY-MM-DD format.")
