import streamlit as st
import numpy as np
import pandas as pd

if 'key' not in st.session_state:
    st.session_state['rerun_counter'] = 0

@st.cache_data
def dbfunction(conn, sql, rerun_counter):
    df = pd.DataFrame(np.random.randint(0,100,size=(100, 4)), 
		columns=list('ABCD'))
    return (df)

conn = 1
sql = ""

df = dbfunction(conn, sql, st.session_state['rerun_counter'])

if st.button("re-run database"):
    st.session_state['rerun_counter'] += 1

st.table(data=df.head(5))
