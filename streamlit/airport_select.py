import streamlit as st
import pandas as pd
import plotly.express as px

# Sample data in dict for dataframe.
data = {
    'country': ['aaa', 'bbb', 'cccc'],
    'airports': [12, 2, 42],
    'population': [1200, 105, 7500]
}

# Build df.
df = pd.DataFrame(data)
st.dataframe(df, use_container_width=True)

sel_country = st.selectbox('**Select country**', df.country)
fil_df = df[df.country == sel_country]  # filter

# Build a new df based from filter.
new_df = pd.melt(fil_df, id_vars=['country'], var_name="feature",
                 value_vars=['airports', 'population'])

logy = True  # to make small values visible
textauto = True  # to write plot label
title = f'country name: {sel_country}'
fig = px.bar(new_df, x='feature', y='value',
             height=300, log_y=logy, text_auto=textauto,
             title=title)

with st.expander('**Country Info**', expanded=True):
    st.plotly_chart(fig, use_container_width=True)
