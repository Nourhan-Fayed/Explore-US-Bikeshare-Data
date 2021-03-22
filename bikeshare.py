import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york': 'new_york_city.csv',
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
    # user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    city_input = ''
    cities  = {'a' :'chicago' ,'b' : 'new york' , 'c' :'washington' }
    while city_input.lower() not in cities.keys():
        city_input = input('\n choose Which city you want to see? Please type \n The letter (a) for Chicago\n The letter (b) for New York City\n The letter (c) for Washington\n')
        if city_input.lower() not in cities.keys():
            print('Sorry, I do not understand your input. ')
    city = cities[city_input.lower()]
    
    #  user input for month (all, january, february, ... , june)
    #convert month name to month number to help in load data function

    month_input = ''
    months_dict = {'january': 1, 'february': 2, 'march': 3, 'april': 4,
                   'may': 5, 'june': 6,'all': 'all' }
    while month_input.lower() not in months_dict.keys():
        month_input = input('\nWhich month you want to filter with? January, February, March, April,'
                            ' May, June or choose  all for not filtering by months ?\n')
        if month_input.lower() not in months_dict.keys():
            print('Sorry, I do not understand your input. Please type in a '
                  'month between January and June')
    month = months_dict[month_input.lower()]
    


    #  user input for day of week (all, monday, tuesday, ... sunday)

    day_input = ''
    days_dict = {'saturday': 1, 'sunday': 2, 'monday': 3, 'tuesday': 4,
                   'wednesday': 5, 'thursday': 6, 'friday':7,'all':8 }
    while day_input.lower() not in days_dict.keys():
        day_input = input('\n choose Which day you want to filter by? Saturday, Sunday, Monday, Tuesday, Wednesday, Thursday, Friday or all for not filtering by day\n')
        if day_input.lower() not in days_dict.keys():
            print('Sorry, I do not understand your input. Please type a week day or  or all for not filtering by day')
    day = day_input.lower()
    
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

    # extract month , hour and day of week from Start Time to create new columns
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.weekday_name
    df['hour'] = df['Start Time'].dt.hour
    # filter by month if applicable
    if month != 'all':

        # filter by month to create the new dataframe
        df = df[df['month'] == month]

    # filter by day of week if applicable
    if day != 'all':
        # filter by day of week to create the new dataframe
        df = df[df['day_of_week'] == day.title()]


    return df


def time_stats(df):
    """
    Displays statistics on the most frequent times of travel.
    
    Args:
    
     (df) - Pandas DataFrame containing city data filtered by month and day
    
    
    """

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # display the most common month

    most_common_month=  df['month'].mode()[0]  
    print('The most common month is:', most_common_month)
    
    # display the most common day of week
    
    most_common_day=df['day_of_week'].mode()[0]
    print('The most common day of the week is: ' , most_common_day )

    # display the most common start hour
    
    most_common_hour= df['hour'].mode()[0]    
    print('The most common hour is: {}' , most_common_hour)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """
    Displays statistics on the most popular stations and trip.
    
    Args:
    
     (df) - Pandas DataFrame containing city data filtered by month and day if you want to filter with them 
    
    
    """

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # display most commonly used start station

    most_common__start_station = df['Start Station'].mode()[0]

    print('Most Start Station:', most_common__start_station)
    
    # display most commonly used end station

    most_common__end_station = df['End Station'].mode()[0]

    print('Most End Station:',  most_common__end_station)
    
    # display most frequent combination of start station and end station trip
    
    df['station combination']= df['Start Station']+" | "+ df['End Station']
    
    most_frequent_combination = df['station combination'].mode()[0]
     
    print('Most station combination:', most_frequent_combination )
    

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """
    Displays statistics on the total and average trip duration.
    
    Args:
    
     (df) - Pandas DataFrame containing city data filtered by month and day if you want to filter with them 
    
    """

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # display total travel time

    total_travel_t = df['Trip Duration'].sum()

    print('Total Travel Time:', total_travel_t)

    # display mean travel time
    
    mean_travel_t = df['Trip Duration'].mean()

    print('Mean Travel Time:', mean_travel_t)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """
    
    Displays statistics on bikeshare users.
    
    Args:
    
     (df) - Pandas DataFrame containing city data filtered by month and day if you want to filter with them 
    
    """

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # Display counts of user types
    
    counts_user_types = df['User Type'].value_counts()
    
    print("Count of user types:" , counts_user_types)
    
    # Display counts of gender

    if 'Gender' in df:
        counts_user_gender = df['Gender'].value_counts()
        print("Count of gender:" , counts_user_gender )
    else:
       print("There is no Gender data to display for the city you choose")     
       
    # Display earliest, most recent, and most common year of birth
    if 'Birth Year'  in df:
        earliest_year =df['Birth Year'].min()
        most_recent_year =df['Birth Year'].max()
        most_common_year =df['Birth Year'].mode()[0]
     
        print('Earliest Year:',earliest_year)
        print('Most Recent Year:',most_recent_year)
        print('Most Common Year:',most_common_year)
    else:
        print("There is no Birth Year data to display for the city you choose") 
        
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def display_raw_data(df):
    
    """
    Displays raw data in batch of 5 upon user request.
    
    Args:
    
     (df) - Pandas DataFrame containing city data filtered by month and day if you want to filter with them 
      
    
    """
    
    
    row = 0
        
    review = input('\nWould you like to see sample raw data ? (y)es or anything else for no.\n')
    while review.lower() == 'yes' :
        dfslice=df.iloc[row:row+5]
        # check if end of data is reached, if so,  exit the loop 
        if dfslice.empty:
            print('no more data to display!')
            break
        else:            
            print(dfslice)
            m_review = input('\nType (y)es if you would you like to see more sample raw data or type anything else for no \n')                
            if m_review.lower() !='yes':
                break
            else:
                row+= 5
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
