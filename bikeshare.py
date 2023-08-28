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
    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    while True:
        city = input('Please enter the name of city you\'d like to explore: ').lower()
        if city not in list(CITY_DATA.keys()):
            print('Sorry, try again')
            continue
        else:
            break

 

 

    # TO DO: get user input for month (all, january, february, ... , june)
    while True:
        months = ['january', 'february', 'march', 'april', 'may', 'june', 'all']
        month = input('Please enter the month you\'d like to filter by or enter "all" if to apply no month filter: ').lower()
        if month not in months:
            print('Sorry, try again')
            continue
        else:
            break

 

    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    while True:
        weekday = ['monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday', 'all']
        day = input('Please enter the name of weekday you\'d like to filter by or enter "all" if to apply no weekday filter: ').lower()
        if day not in weekday:
            print('Sorry, try again')
            continue
        else:
            break

 

              

 

 

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
    # load data file into a dataframe
    df = pd.read_csv(CITY_DATA[city])

 

    # convert the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])

 

    # extract month and day of week from Start Time to create new columns
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.weekday_name

 

    # filter by month if applicable
    if month != 'all':
        # use the index of the months list to get the corresponding int
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) + 1

        # filter by month to create the new dataframe
        df = df[df['month'] == month]

 

    # filter by day of week if applicable
    if day != 'all':
        # filter by day of week to create the new dataframe
        df = df[df['day_of_week'] == day.title()]

 

    return df

def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

 

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

 

    # TO DO: display the most common month
    popular_month = df['month'].mode()[0]
    print('The mosy common month is: ', popular_month)

    # TO DO: display the most common day of week
    popular_day = df['day_of_week'].mode()[0]
    print('The mosy common day is: ', popular_day)

    # TO DO: display the most common start hour
    df['hour'] = df['Start Time'].dt.hour
    popular_hour = df['hour'].mode()[0]
    print('The mosy common hour is: ', popular_hour)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

 

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    popular_start_station = df['Start Station'].value_counts().idxmax()
    print('The most commonly used start station is: ', popular_start_station)

 

    # TO DO: display most commonly used end station
    popular_end_station = df['End Station'].value_counts().idxmax()
    print('The most commonly used end station is: ', popular_end_station)

    # TO DO: display most frequent combination of start station and end station trip
    popular_start_end_station = df.groupby(['Start Station', 'End Station']).size().idxmax()
    print('The most commonly used start_end station is: ', popular_start_end_station)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

 

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    total_travel_time = df['Trip Duration'].sum()
    print('Total travel time is: ', total_travel_time)

    # TO DO: display mean travel time
    mean_travel_time = df['Trip Duration'].mean()
    print('The mean travel time is: ', mean_travel_time)

 

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

 

 

def user_stats(df):
    """Displays statistics on bikeshare users."""

 

    print('\nCalculating User Stats...\n')
    start_time = time.time()

 

    # TO DO: Display counts of user types

    user_type_count = df['User Type'].value_counts()
    print('Counts of user type: ', user_type_count)
    # TO DO: Display counts of gender

    try:
        gender_count = df['Gender'].value_counts()
        print('Counts of gender: ', gender_count)
    except KeyError:
        print('No data available')

 

 

    # TO DO: Display earliest, most recent, and most common year of birth
    # the most earliest birth year
    try:
        earliest_year = df['Birth Year'].min()
        print("The most earliest birth year:", earliest_year)
    except KeyError:
        print('No data available')

    # the most recent birth year
    try:
        most_recent = df['Birth Year'].max()
        print("The most recent birth year:", most_recent)
    except KeyError:
        print('No data available')

     # the most common birth year
    try:
        most_common_year = df['Birth Year'].value_counts().idxmax()
        print("The most common birth year:", most_common_year)
    except KeyError:
        print('No data available')

 

 

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def display_raw_data(df):
    """Displays raw data on user request. """

    view_data = input('\nWould you like to view 5 rows of individual trip data? Enter "yes" or "no"\n').lower()
    start_loc = 0
    while view_data == 'yes':
        print(df.head())
        while True:
            start_loc += 5
            view_data = input("Do you wish to see more 5 rows : ").lower()
            if view_data == 'yes':
                print(df[start_loc:start_loc+5])
                continue
            else:
                break
    print('-'*40)

def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)



 

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        display_raw_data(df)          

 

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
    main()