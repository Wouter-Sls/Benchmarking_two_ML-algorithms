import numpy as np
import pandas as pd
import sklearn
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
import calendar
import streamlit as st

st.title("Task ML. Benchmarking two ML algorithms") #Show the title of the app on Streamlit
st.subheader(':blue[_Created by Wouter Selis_] :male-technologist:', divider='rainbow') #Show a subheader on Streamlit with text in blue, an emoji and a rainbow line under the text

filecsv='forestfires.csv'
#Import of the forestfires csv file
df = pd.read_csv(filecsv)

# Create a dictionary to map month abbreviations to numbers
month_to_num = {month.lower(): index for index, month in enumerate(calendar.month_abbr) if month}
# Use the map function to transform the values
df['month'] = df['month'].map(month_to_num)


# Create a dictionary to map day abbreviations to numbers
day_to_num = {day.lower(): index+1 for index, day in enumerate(calendar.day_abbr) if day}
# Use the map function to transform the values
df['day'] = df['day'].map(day_to_num)


# Create train and test set
x=df[['month','day', 'X', 'Y','FFMC', 'DMC', 'DC', 'ISI', 'temp', 'RH', 'wind', 'rain']]
y=df['area']

X_train, X_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=0)

#Train the model
model = LinearRegression()
model.fit(X_train, y_train)

month=''
day=''
x=''
y=''
ffmc=''
dmc=''
dc=''
isi=''
temp=''
rh=''
wind=''
rain=''


#User input
try:
    month = float(st.text_input("Enter a month as a number (Jan=1, Feb=2, ...): "))
except ValueError:
    st.error("Value can't be empty.")
try:
    day = float(st.text_input("Enter a day as a number (Monday=1, Tuesday=2, ...): "))
except ValueError:
    st.error("Value can't be empty.")
try:
    x = float(st.text_input("Enter an X coördinate (1 to 9): "))
except ValueError:
    st.error("Value can't be empty.")
try:
    y = float(st.text_input("Enter an Y coördinate (1 to 9): "))
except ValueError:
    st.error("Value can't be empty.")
try:
    ffmc = float(st.text_input("Enter a FFMC index from the FWI system (0.0 to 101.0): "))
except ValueError:
    st.error("Value can't be empty.")
try:
    dmc = float(st.text_input("Enter a DMC index from the FWI system (0.0 to 200.0): "))
except ValueError:
    st.error("Value can't be empty.")
try:
    dc = float(st.text_input("Enter a DC index from the FWI system (0.0 to 800.0): "))
except ValueError:
    st.error("Value can't be empty.")
try:
    isi = float(st.text_input("Enter a ISI index from the FWI system (0.0 to 60.0): "))
except ValueError:
    st.error("Value can't be empty.")
try:
    temp = float(st.text_input("Enter a temperature in Celsius degrees: 0.0 to 45.0"))
except ValueError:
    st.error("Value can't be empty.")
try:
    rh = float(st.text_input("Enter a RH index from the FWI system (0.0 to 100.0): "))
except ValueError:
    st.error("Value can't be empty.")
try:
    wind = float(st.text_input("Enter the wind speed in km/h: "))
except ValueError:
    st.error("Value can't be empty.")
try:
    rain = float(st.text_input("Enter the outside rain in mm/m2: "))
except ValueError:
    st.error("Value can't be empty.")

if month != '' or day !='' or x!=''or y !=''or ffmc !=''or dmc !=''or dc !=''or isi !=''or temp !=''or rh !=''or wind !=''or rain!='':
    user_inputs={'month': month,'day':day , 'X': x, 'Y': y,'FFMC': ffmc, 'DMC': dmc, 'DC': dc, 'ISI': isi, 'temp': temp, 'RH': rh, 'wind': wind, 'rain': rain}
    df_user=pd.DataFrame([user_inputs])
    y_pred = model.predict(df_user)
    st.write("Predicted burned forest area: ", round(y_pred[0],2))