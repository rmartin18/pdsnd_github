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
        city = input('Enter the city (chicago, new york city, washington): ').lower()
        if city in CITY_DATA:
            print('OK, ', city)
            break
        else:
            print('Invalid. Please enter a valid city.')

    # TO DO: get user input for month (all, january, february, ... , june)
    while True:
        month = input('Enter the city (all, january, february, ... , june): ').lower()
        if month in ['all', 'january', 'february', 'march', 'april', 'may', 'june']:
            print('OK, ', month)
            break
        else:
            print('Invalid. Please enter a valid month.')

    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    while True:
        day = input('Enter the city (all, monday, tuesday, ... sunday): ').lower()
        if day in ['all', 'monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday']:
            print('OK, ', day)
            break
        else:
            print('Invalid. Please enter a valid day of the week.')

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
    #Info practice 3.
    
    df = pd.read_csv(CITY_DATA[city])

    df['Start Time'] = pd.to_datetime(df['Start Time'])
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.dayofweek

    if month != 'all':
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) + 1
        df = df[df['month'] == month]

    if day != 'all':
        days = ['monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday']
        day = days.index(day)
        df = df[df['day_of_week'] == day]
        
    return df

def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    month = df['month'].mode()[0]
    print(f'The most common month: {month}')

    # TO DO: display the most common day of week
    day = df['day_of_week'].mode()[0]
    print(f'The most common day of the week: {day}')

    # TO DO: display the most common start hour
    df['hour'] = df['Start Time'].dt.hour
    start_hour = df['hour'].mode()[0]
    print(f'The most common start hour: {start_hour}')

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)
    
def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    start_station = df['Start Station'].mode()[0]
    print(f'The most commonly used start station: {start_station}')

    # TO DO: display most commonly used end station
    end_station = df['End Station'].mode()[0]
    print(f'The most commonly used end station: {end_station}')

    # TO DO: display most frequent combination of start station and end station trip
    df['start_end_combination'] = df['Start Station'] + ' to ' + df['End Station']
    trip_combination = df['start_end_combination'].mode()[0]
    print(f'The most frequent combination of start station and end station trip: {trip_combination}')

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    total = df['Trip Duration'].sum()
    print(f'Total travel time: {total} seconds')

    # TO DO: display mean travel time
    mean = df['Trip Duration'].mean()
    print(f'Mean travel time: {mean} seconds')

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    user = df['User Type'].value_counts()
    print(f'Counts of user types:\n{user}')

    # TO DO: Display counts of gender
    if 'Gender' in df.columns:
        gender = df['Gender'].value_counts()
        print(f'Counts of gender:\n{gender}')

    # TO DO: Display earliest, most recent, and most common year of birth
    if 'Birth Year' in df.columns:
        earliest_birth_year = df['Birth Year'].min()
        most_recent_birth_year = df['Birth Year'].max()
        most_common_birth_year = df['Birth Year'].mode()[0]

        print(f'Earliest birth year: {earliest_birth_year}')
        print(f'Most recent birth year: {most_recent_birth_year}')
        print(f'Most common birth year: {most_common_birth_year}')

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)
    
def display_data(df):
    view_data = input('\nWould you like to view 5 rows of individual trip data? Enter yes or no\n').lower()
    start_loc = 0
    while view_data == 'yes':
        print(df.iloc[start_loc:start_loc+5])
        start_loc += 5
        view_data = input("Do you wish to continue?: ").lower()    
    
def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        display_data(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break

if __name__ == "__main__":
	main()

#Informarion

def calculate_distance(a, b):
    return abs(a - b)
