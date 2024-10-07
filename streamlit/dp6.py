import pandas as pd
import numpy as np
import streamlit as st
from datetime import date, timedelta, datetime

#jan_1, dec_31  = (date(2023, 1, 1), date(2023, 12, 31))
#jan_rg = (date(2023, 1, 13), date(2023, 1, 17))

    
def print_func(words, n):
    now = n
    print(f'{now.minute}m{now.second}s - {words} changed', n)
    #st.write(f'{now.minute}m{now.second}s - {words} changed', n)
    #st.session_state['end_range'] = datetime.now() + timedelta(days=st.session_state['deltaDate'])
    #st.session_state['start_range'] = datetime.now() - timedelta(days=st.session_state['deltaDate'])

option = st.selectbox(
	'Set Default Timeframe (relative to today)',
	('+/- 3 months', '+/- 6 months', '+/- 12 months', '+/- 2 yr' , '+/- 5 yr'), index=2,
    on_change=print_func,
    args=('selectbox',datetime.now()) 
 )

st.write('You selected:', option)

# Create a checkbox
agree = st.checkbox("Include Blank Date Entries", value=True)

# Check if the checkbox is checked
if agree:
    st.write("Great! We will include blank dates")
else:
    st.write("Only search filled in dates")

if option == '+/- 3 months':
    st.session_state['deltaDate'] = 90
elif option == '+/- 6 months':
    st.session_state['deltaDate'] = 180
elif option == '+/- 12 months':
    st.session_state['deltaDate'] = 365
elif option == '+/- 2 yr':
    st.session_state['deltaDate'] = 365 * 2
elif option == '+/- 5 Yr':
    st.session_state['deltaDate'] = 365 * 5
    
#st.write( 'deltaDate:',  st.session_state['deltaDate'] )
st.session_state['end_range'] = datetime.now() + timedelta(days=st.session_state['deltaDate'])
st.session_state['start_range'] = datetime.now() - timedelta(days=st.session_state['deltaDate'])

#deltaDate = 365

today = datetime.now()
next_year = today.year - 6 # max default is 5 year back, so 6 is larger window
future_year = today.year + 6 # max default is 5 year ahead, so 6 is larger window
jan_1 = date(next_year, 1, 1)
dec_31 = date(future_year, 12, 31)
#start_range = today - timedelta(days=st.session_state['deltaDate'])
#end_range = today + timedelta(days=st.session_state['deltaDate'])


    
#jan_1, dec_31  = (date(2023, 1, 1), date(2023, 12, 31)) # allowable range
#jan_rg = (date(2023, 1, 13), date(2023, 1, 17)) # Default values


if st.session_state:
    #d = st.session_state.d
    d = None
else:
    st.session_state['end_range'] = datetime.now() + timedelta(days=st.session_state['deltaDate'])
    st.session_state['start_range'] = datetime.now() - timedelta(days=st.session_state['deltaDate'])
    #jan_rg = (st.session_state['start_range'], st.session_state['end_range']) # preset range
    #d = jan_rg
    d = (st.session_state['start_range'], st.session_state['end_range']) # preset range

#d = st.date_input("Select a range", value=d, min_value=jan_1, max_value=dec_31)

if 'deltaDate' not in st.session_state:
    st.session_state['deltaDate'] = 365
    
if 'start_range' not in st.session_state:
    st.session_state['start_range'] = datetime.now() - timedelta(days=st.session_state['deltaDate'])
    

if 'end_range' not in st.session_state:
    st.session_state['end_range'] = datetime.now() + timedelta(days=st.session_state['deltaDate'])
    

d = st.date_input("Finetune a date range (Optional)", value=(st.session_state['start_range'],
                                                             st.session_state['end_range'])
                  , min_value=jan_1, max_value=dec_31)

if len(d)==2:
    st.session_state.d = d
    
d
st.write('Selection:', agree, d)


# Set the number of rows
num_rows = 20

# Generate random dates
#end_date = pd.to_datetime('2024-01-01')

yrs_ago = today - timedelta(days=365*3)
yrs_ahead = today + timedelta(days=365*3)
start_date = pd.to_datetime(yrs_ago)
end_date = pd.to_datetime(yrs_ahead)

np.random.seed(42)
random_dates = pd.to_datetime(np.random.randint(start_date.value, end_date.value, num_rows), unit='ns')


# Create the DataFrame
df = pd.DataFrame({'date': random_dates})

# Randomly replace some dates with None values
df['date'] = df['date'].sample(frac=0.7, random_state=42).reset_index(drop=True)

#print(df)
st.write('total:', len(df.index))
st.dataframe(df.sort_values('date', ascending=True))


#l = ((df['date'] >= st.session_state['start_range']) & (df['date'] <= st.session_state['end_range'])) 

l = ((df['date'].dt.date >= d[0]) & (df['date'].dt.date <= d[1])) 

if agree:
    l =  ( l  | df['date'].isnull())

st.write('filter:', len(df.loc[l,].index), 
         st.session_state['start_range'],
         st.session_state['end_range'], d,
         d[0], d[1])
st.dataframe(df.loc[l,].sort_values('date', ascending=True))

