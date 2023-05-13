import streamlit as st
import pandas as pd
import plotly.express as px
import numpy as np

df = pd.DataFrame(
    np.random.randint(1, 6, size=(100, 2)), columns=["Item_Name", "Rating_Score"]
)

df = (
    df.groupby("Rating_Score")
    .count()
    .reset_index()
    .rename(columns={"Item_Name": "Count"})
)
df["Item_Name"] = "Samsung Galaxy S20 FE 5G"
st.dataframe(df)

fig = px.bar(
    df,
    x="Rating_Score",
    y="Count",
    color="Rating_Score",
    text="Count",
)

st.plotly_chart(fig)
