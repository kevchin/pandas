# https://discuss.streamlit.io/t/how-to-use-session-state-to-update-dataframe/30502/3
import pandas as pd
import streamlit as st
import numpy as np
import random
from numpy.random import seed
from numpy.random import randint


# Make dummy function
def read_sql_query(sql_query, con):

    data = {'a': ['A', 'A', 'B', 'B', 'C', 'C', 'C', 'D', 'D', 'D'],
            'b': ['red', 'blue', 'black', 'blue', 'green', 'black', 'blue', 'green', 'yellow', 'white']}
    colors = True
    colors = False
    if (colors):
       df = pd.DataFrame(data)
       return (df)
    else:
       cl  = randint(0, 10, 10)
       data = {'a': ['A', 'A', 'B', 'B', 'C', 'C', 'C', 'D', 'D', 'D'],
            'b': ['red', 'blue', 'black', 'blue', 'green', 'black', 'blue', 'green', 'yellow', 'white'], 'c': cl}
       df = pd.DataFrame(data)
       return (df)
       #return (pd.DataFrame(np.random.randint(0,6,size=(5, 3)),
#		columns=list('abc')))

con = None

def main():
    df = read_sql_query(
        """
    select * from testdb
     """,
        con,
    )
    text = "out session" + ' FIRST TIME'
    options = df['a'].unique().tolist()
    selected_options = st.sidebar.multiselect('Which a do you want?',
		options, options)

    if "click" not in st.session_state:
        # First time dataset
        st.session_state.click = False
        cl  = randint(0, 10, 10)
        data = {'a': ['A', 'A', 'B', 'B', 'C', 'C', 'C', 'D', 'D', 'D'],
            'b': ['red', 'blue', 'black', 'blue', 'green', 'black', 'blue', 'green', 'yellow', 'white'], 'c': cl}
        df = pd.DataFrame(data)
        st.write(df)
        #st.bar_chart(df)
    else:

        if st.session_state.click == False:
            # alternate dataset request
            st.session_state.click = True

#            df["c"] = df["a"] + df["b"]
            text = "IN session: " + str( random.randint(0, 9))

            # here it suppose to display the updated data 
            # after the user update values.
            filtered_df = df[df["a"].isin(selected_options)]
#            st.dataframe(df)
            st.write(filtered_df)
            #st.write(df)
            #st.bar_chart(filtered_df)
        else:
            # alternate dataset request

            text = "OUT session: " + str( random.randint(0, 9))
            st.session_state.click = False
            filtered_df = df[df["a"].isin(selected_options)]
#            st.dataframe(df)
            st.write(filtered_df)
            #st.bar_chart(df)
            #st.bar_chart(filtered_df)
    st.button(text)

if __name__ == "__main__":
    main()

