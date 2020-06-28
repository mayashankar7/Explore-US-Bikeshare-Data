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
        city = input("enter the desired name of city")
        if city in ["chicago","new york city","washington"]:
            break
        else:
            city = input("try again please").lower()

    # TO DO: get user input for month (all, january, february, ... , june)
    while True:
        month = input("enter the  months's name you want")
        if  month in ["all","january", "february", "march", "april", "may", "june"]:
            break
        else:
            month = input("enter a valid month please").lower()
            
            
        


    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    while True:
        day = input("enter the name of day you want")
        if day in ["all","monday", "tuesday", "wednesday", "thursday", "friday", "saturday","sunday"]:
            break
        else:
            day = input("enter the day name again ").lower()
            
        


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
    start_time = time.time()
    
    df = pd.read_csv(CITY_DATA[city])
    
    df["Start Time] = pd.to_datetime(df["Start Time"])
    
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.weekday_name   
       
    if month !="all":
       df["month"] = df['Start Time'].dt.month
       months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) + 1

        # filter by month to create the new dataframe
        df = df.loc[df['month'] == month]

    # filter by day of week if applicable
    if day != 'all':
        df['day_of_week'] = df['Start Time'].dt.weekday_name

        # filter by day of week to create the new dataframe
        df = df.loc[df['day_of_week'] == day.title()]
   



    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    common_month = df["month"].mode()[0]
    print(common_month , "is the most common month")

    # TO DO: display the most common day of week
    common_day = df["day"].mode()[0]
    print(common_day , "is the most common day") 

    # TO DO: display the most common start hour
    df["hour"] = df["Start Time"].dt.hour
    common_hour = df["hour"].mode()[0]
    print(common_hour , "is the most common hour")
       

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    print(df["Start Station"].value_counts().idxmax() , "is the most commonly used start station")

    # TO DO: display most commonly used end station
    print(df["End Station"].value_counts().idxmax() , "is the most commonly used end station") 

    # TO DO: display most frequent combination of start station and end station trip
    combine_stations = df.groupby(["Start Station" , "End Station"]).count()
    print(Start_Station , "and" , End_station , "are the most commonly used start and end stations")   


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    total_travel_time = df['Trip Duration'].sum()
    total_travel_time_update = total_travel_time/(86400)
    print("the total travel time is" , total_travel_time_update , "days")                       
                            

    # TO DO: display mean travel time
    mean_trvel_time = df['Trip Duration'].mean()
    print('The Mean travel time is:', Mean_Travel_Time/60, " Minutes")
    

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    types_of_user =df['User Type'].value_counts()
    print(types_of_user)

    # TO DO: Display counts of gender
    if ('Gender' in df):
        count_of_male=df['Gender'].str.count('Male').sum()
        count_of_female=df['Gender'].str.count('Female').sum()
        print(f'total male users are {count_of_male}')
        print(f'total female users are {count_of_female}'
        
       

    # TO DO: Display earliest, most recent, and most common year of birth
    if('Birth Year' in df):
        earliest_year = df['Birth Year'].min()
        recent_year = df['Birth Year'].max()
        common_birth_year = df['Birth Year'].mode()[0]
        print("\nEarliest year of birth: " + str(earliest_year))
        print("\nMost recent year of birth: " + str(recent_year))
        print("\nMost common year of birth: " + str(common_birth_year))
              

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
