import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from babel.numbers import format_currency

data_bikesharing = pd.read_csv('main_data.csv')

# Sidebar
with st.sidebar:
    
    st.image("https://seeklogo.com/images/T/The_Bike_Man-logo-207AE33D5F-seeklogo.com.png")
    st.sidebar.title('BIKE SHARING')
    st.subheader('Please choose visualization first!')
    visualization_option = st.sidebar.selectbox('Choose Visualization', ['Daily Bike Sharing Count by Hour', 'Difference in Bike Sharing Counts Weekdays vs Weekends', 'The Effect of Weather on Daily Bike Sharing'])

# Main content
st.title('Bike Sharing Dashboard :sparkles:')

# Visualization
if visualization_option == 'Daily Bike Sharing Count by Hour':
    st.subheader('Daily Bike Sharing Count by Hour')
    fig, ax = plt.subplots(2, figsize=(12, 12))

    sns.lineplot(data=data_bikesharing, x='hr', y='cnt_hourly', estimator='mean', ax=ax[0])
    ax[0].set_title('Hourly Count of Bike Sharings')
    ax[0].set_xlabel('Hour')
    ax[0].set_ylabel('Count')

    sns.barplot(data=data_bikesharing, x='hr', y='cnt_hourly', estimator=sum, ax=ax[1])
    ax[1].set_title('Total Hourly Count of Bike Sharings')
    ax[1].set_xlabel('Hour')
    ax[1].set_ylabel('Total Count')

    st.pyplot(fig)

    st.subheader('Result')
    st.write('From both visualizations above, daily bike rentals are higher at 8 AM and also from 5 PM to 6 PM. Meanwhile, rentals are lower from 4 AM to 5 AM.')

elif visualization_option == 'Difference in Bike Sharing Counts Weekdays vs Weekends':
    st.subheader('Difference in Bike Sharing Counts Weekdays vs Weekends')
    fig, ax = plt.subplots(1, 2, figsize=(15, 6))
    
    data_sewa = data_bikesharing.groupby('workingday_daily')['cnt_daily'].mean()
    labels = ['Weekend', 'Weekday']
    ax[0].bar(labels, data_sewa, color=['blue', 'orange'])
    ax[0].set_title('Average Bike Sharing Counts by Day Type')
    ax[0].set_xlabel('Day Type')
    ax[0].set_ylabel('Average Bike Sharing Counts')
    
    total = data_bikesharing.groupby('workingday_daily')['cnt_daily'].sum()
    labels = ['Weekend', 'Weekday']
    ax[1].pie(total, labels=labels, autopct='%1.1f%%', startangle=140)
    ax[1].set_title('Total Bike Sharing Counts by Day Type')

    st.pyplot(fig)

    st.subheader('Result:')
    st.write('From both visualizations above, the bike rental counts are higher on weekdays compared to weekends.')

else:
    st.subheader('The Effect of Weather on Daily Bike Sharing')
    fig, ax = plt.subplots(figsize=(10, 6))
    sns.boxplot(data=data_bikesharing, x='weathersit_daily', y='cnt_daily', hue='weathersit_daily', legend=False, ax=ax)
    plt.title('Daily Bike Sharing Count by Weather')
    plt.xlabel('Weather Situation')
    plt.ylabel('Count')
    st.pyplot(fig)

    weather_data = data_bikesharing.groupby('weathersit_daily')['cnt_daily'].mean()
    weather_names = ['Clear', 'Mist+Cloudy', 'Light Snow']
    fig_weather, ax_weather = plt.subplots()
    ax_weather.bar(weather_names, weather_data)
    ax_weather.set_title('Effect of Weather on Daily Bike Sharing Counts')
    ax_weather.set_xlabel('Weather Condition')
    ax_weather.set_ylabel('Average Daily Bike Sharing Count')
    st.pyplot(fig_weather)

    st.subheader('Result')
    st.write('From both visualizations above, during clear weather, partly cloudy, and mostly cloudy, the daily bike rental counts are higher compared to other weather conditions.')
    
# Footer
st.caption('Copyright (c) Bike Sharing 2024')
