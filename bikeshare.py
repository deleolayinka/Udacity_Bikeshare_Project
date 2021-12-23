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
        (str) month - name of the month to filter by, or "None" to apply no month filter
        (str) day - name of the day of week to filter by, or "None" to apply no day filter
    """
    print('Hello! My name is Moses Olayinka Oyedele, I will be your information guide on this tour. Let\'s explore some interesting data!')
    
    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    while True:
        cities= ['chicago','new york city','washington']
    # Accepting user input and converting to lower case, repeated at every user input stage of this program
    # Handling invalid User inputs
        city= input("\nYou are welcome to the US bikeshare analytics dashboard, please specify the city you would love to analyze: \n\n1. Chicago \n2. New York City \n3. Washington \n\nAccepted input: Full city name (case insensitive), (e.g. chicago, Chicago, CHICAGO, cHiGAgo).\n").lower()
        if city in cities:
            break
        else:
            print("\n Invalid input! Please enter a valid city name")    

    # TO DO: get user input for month (all, january, february, ... , june)
    while True:
        months= ['January','February','March','April','June','May','None']
        month= input("\nPlease specify the month you would love to analyze (January, February, March, April, May, June). \nType 'None' to filter for all months.\n").title()
        if month in months:
            break
        else:
            print("\nInvalid input! Please enter a valid month name")    


    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    while True:
        days= ['Monday','Tuesday','Wednesday','Thursday','Friday','Saturday','Sunday','None']
        day = input("\nPlease specify the day of the week you would love to analyze (Monday, Tuesday, Wednesday, Thursday, Friday, Saturday, Sunday)? \nType 'None' to filter for all days\n").title()         
        if day in days:
            break
        else:
            print("\nInvalid input! Please enter a valid day of the week")    

    print('-'*40)
    return city, month, day

def load_data(city, month, day):
    """
    Loads data for the specified city and filters by month and day if applicable.

    Args:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "None" to apply no month filter
        (str) day - name of the day of week to filter by, or "None" to apply no day filter
    Returns:
        df - Pandas DataFrame containing city data filtered by month and day
    """
    
    # Loading city data file into a dataframe
    df = pd.read_csv(CITY_DATA[city])

    # Converting the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    # Extracting the month and day of week from the Start Time to create new columns
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.weekday_name

    # Filtering by month (only if applicable)
    if month != 'None':
        # Using the index of the month list to get the corresponding int
        months = ['January', 'February', 'March', 'April', 'May', 'June']
        month = months.index(month)+1
    
        # Filtering by month to create the new dataframe
        df = df[df['month']==month] 

   # Filtering by day of the week (if applicable)
    if day != 'None':
        # filter by day of week to create the new dataframe
        df = df[df['day_of_week']==day]

    # Returning the selected file as a dataframe (df) with relevant columns
    return df

def time_stats(df,month,day):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    if month =='None':
        pop_month= df['month'].mode()[0]
        months= ['January','February','March','April','May','June']
        pop_month= months[pop_month-1]
        print("The most common month is",pop_month)

    # TO DO: display the most common day of week
    if day =='None':
        pop_day= df['day_of_week'].mode()[0]
        print("The most common day of the week is",pop_day)

    # Extracting hour from the Start Time column to create an hour column
    df['Start Hour'] = df['Start Time'].dt.hour
    
    # TO DO: display the most common start hour
    pop_hour=df['Start Hour'].mode()[0]
    print("The most common Start Hour is {}:00 hrs".format(pop_hour))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def station_stats(df):
    """Displays statistics on the most popular stations and trip."""
    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    pop_start_station= df['Start Station'].mode()[0]
    print("The most commonly used Start Station is {}".format(pop_start_station))

     # TO DO: display most commonly used end station
    pop_end_station= df['End Station'].mode()[0]
    print("The most commonly used End Station is {}".format(pop_end_station))

    # TO DO: display most frequent combination of start station and end station trip
    # Using str.cat to combine two columns in the df, and assigning the result to a new column 'Start To End'
    # Using mode on this new column to obtain the most frequent combination of start station and end station trip
    df['Start To End'] = df['Start Station'].str.cat(df['End Station'], sep=' to ')
    combo = df['Start To End'].mode()[0]
    print(f"\nThe most frequent combination of start station and end station trips are from {combo}.")

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    total_duration=df['Trip Duration'].sum()
    # Converting total travel time to Minutes & Seconds
    minute,second=divmod(total_duration,60)
    # Converting total travel time to Hours & Minutes
    hour,minute=divmod(minute,60)
    print("The total travel time is: {} hour(s) {} minute(s) {} second(s)".format(hour,minute,second))
    
    # TO DO: display mean travel time
    average_duration=round(df['Trip Duration'].mean())
    m,sec=divmod(average_duration,60)
    if m>60:
        h,m=divmod(m,60)
        print("The mean travel time: {} hour(s) {} minute(s) {} second(s)".format(h,m,sec))
    else:
        print("The mean travel time: {} minute(s) {} second(s)".format(m,sec))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def user_stats(df,city):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    user_counts= df['User Type'].value_counts()
    print("The user types are distributed as follows:\n",user_counts)

    # TO DO: Display counts of gender
    if city.title() == 'Chicago' or city.title() == 'New York City':
        gender_counts= df['Gender'].value_counts()
        print("\nThe gender counts are distributed as follows:\n",gender_counts)
    
    # TO DO: Display earliest, most recent, and most common year of birth
        earliest= int(df['Birth Year'].min())
        print("\nThe earliest year of birth was in",earliest)
        most_recent= int(df['Birth Year'].max())
        print("The most recent year of birth is",most_recent)
        common= int(df['Birth Year'].mode()[0])
        print("The most common year of birth is",common)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

    # Displaying the data frame itself based on request from the user
def display_data(df):
    """Displays 5 rows of data from the csv file for the selected city.
    Args:
    param1 (df): The data frame you wish to work with.
    Returns:
    None.
    """
    while True:
        response=['yes','no']
        choice= input("Would you like to view individual trip data (Only 5 entries)? \nPlease type 'yes' or 'no'\n").lower()
        if choice in response:
            if choice=='yes':
                start=0
                end=5
                data = df.iloc[start:end,:9]
                print(data)
            break     
        else:
            print("Invalid input! Please enter a valid response")
    if  choice=='yes':       
            while True:
                choice_2= input("Would you like to view more trip data? \nPlease type 'yes' or 'no'\n").lower()
                if choice_2 in response:
                    if choice_2=='yes':
                        start+=5
                        end+=5
                        data = df.iloc[start:end,:9]
                        print(data)
                    else:    
                        break  
                else:
                    print("Please enter a valid response")              

def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)
        
        time_stats(df,month,day)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df,city)
        display_data(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break

if __name__ == "__main__":
	main()