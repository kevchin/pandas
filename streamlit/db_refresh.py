# https://discuss.streamlit.io/t/how-to-use-session-state-to-update-dataframe/30502/3
import pandas as pd
import streamlit as st
import numpy as np


# Make dummy function
def read_sql_query(sql_query, con):
    return (pd.DataFrame(np.random.randint(0,6,size=(5, 3)),
		columns=list('abc')))

con = None

def main():
    df = read_sql_query(
        """
    select * from testdb
     """,
        con,
    )
    text = "out session" + ' FIRST TIME'
    if "click" not in st.session_state:
        # First time dataset
        st.session_state.click = False
        df = pd.DataFrame({"a": [1, 2, 3], "b": [4, 5, 6]})
        st.write(df)
        st.bar_chart(df)
    else:
        if st.session_state.click == False:
            # alternate dataset request
            st.session_state.click = True

            df["c"] = df["a"] + df["b"]
            text = "IN session: " + str(df.to_numpy().sum())

            # here it suppose to display the updated data 
            # after the user update values.
            st.write(df)
            st.bar_chart(df)
        else:
            # alternate dataset request

            text = "OUT session: " + str(df.to_numpy().sum())
            st.session_state.click = False
            st.write(df)
            st.bar_chart(df)
    st.button(text)

if __name__ == "__main__":
    main()
