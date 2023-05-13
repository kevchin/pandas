import pandas as pd
import streamlit as st

# Create a dictionary of data
data = {'Name': ['A', 'A', 'B', 'B', 'C', 'C', 'C', 'D', 'D', 'D'],
       'Color': ['red', 'blue', 'black', 'blue', 'green', 'black', 'blue', 'green', 'yellow', 'white']}

# Create a DataFrame from the data
df = pd.DataFrame(data)

# Create an empty DataFrame to store filtered data
df_filtered = pd.DataFrame()

# Initialize the name_select variable
name_select = None

# Get a list of unique color options from the original DataFrame
color_options = df['Color'].unique()

# Create a multi-select widget to select colors
color_select = st.multiselect("Select Color", color_options, key="color")

# Create a flag to track if the color select has been changed
color_select_changed = False

# If the user selects one or more colors:
if color_select:
    # Set the flag to indicate the color select has been changed
    color_select_changed = True
    
    # Filter the original DataFrame to only include rows with the selected colors
    df_filtered = df[df['Color'].isin(color_select)]
    
    # Get a list of unique name options from the filtered DataFrame
    name_options = df_filtered['Name'].unique()
    
    # Create a multi-select widget to select names
    name_select = st.multiselect("Select Name", name_options, key="name")

# If the user selects one or more names, but the color select has not been changed:
if name_select and not color_select_changed:
    # Filter the original DataFrame to only include rows with the selected names
    df_filtered = df[df['Name'].isin(name_select)]
    
    # Get a list of unique color options from the filtered DataFrame
    color_options = df_filtered['Color'].unique()
    
    # Create a multi-select widget to select colors
    color_select = st.multiselect("Select Color", color_options, key="color")

# If the filtered DataFrame is not empty, display it
if not df_filtered.empty:
    st.write(df_filtered)
