import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
    # get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs

while True:
        city = input("Enter city (chicago, new york city, washington): ").strip().lower()
        if city in CITY_DATA:
            break
        print("Invalid city. Please try again.")




    # get user input for month (all, january, february, ... , june)
valid_months = ['all', 'january', 'february', 'march', 'april', 'may', 'june']
    while True:
        month = input("Enter month (all, january, february, march, april, may, june): ").strip().lower()
        if month in valid_months:
            break
        print("Invalid month. Please try again.")

    # get user input for day of week (all, monday, tuesday, ... sunday)

valid_days = ['all', 'monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday']
    while True:
        day = input("Enter day (all, monday, tuesday, wednesday, thursday, friday, saturday, sunday): ").strip().lower()
        if day in valid_days:
            break
        print("Invalid day. Please try again.")


    print('-'*40)
    return city, month, day


def load_data(city, month, day):
    """
    Loads data for the specified city and filters by month and day if applicable.

    Args:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    Returns:
        df - Pandas DataFrame containing city data filtered by month and day
    """

# Load city CSV
    df = pd.read_csv(CITY_DATA[city])

    # Convert Start Time to datetime and drop invalid rows (minimal safety)
    df['Start Time'] = pd.to_datetime(df['Start Time'], errors='coerce')
    df = df.dropna(subset=['Start Time'])

    # Derive time-based columns used later
    df['month'] = df['Start Time'].dt.month                  # 1-12
    df['day_of_week'] = df['Start Time'].dt.day_name().str.lower()  # 'monday'...'sunday'
    df['hour'] = df['Start Time'].dt.hour                    # 0-23

    # Filter by month if requested
    if month != 'all':
        month_map = {
            'january': 1, 'february': 2, 'march': 3,
            'april': 4, 'may': 5, 'june': 6
        }
        df = df[df['month'] == month_map[month]]

    # Filter by day of week if requested
    if day != 'all':
        df = df[df['day_of_week'] == day]


    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # display the most common month


    # display the most common day of week


    # display the most common start hour


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # display most commonly used start station


    # display most commonly used end station


    # display most frequent combination of start station and end station trip


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # display total travel time


    # display mean travel time


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # Display counts of user types


    # Display counts of gender


    # Display earliest, most recent, and most common year of birth


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
