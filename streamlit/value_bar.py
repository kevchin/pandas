import pandas as pd
import seaborn as sns
import streamlit as st
import numpy as np
import matplotlib.pyplot as plt


df = pd.DataFrame(
    np.random.randint(1, 6, size=(100, 2)), columns=["Item_Name", "Rating_Score"]
)

val_count  = pd.DataFrame(df['Rating_Score'].value_counts())
#print (val_count.columns)

fig, ax = plt.subplots(figsize=(10,5))

ax = df['Rating_Score'].value_counts()[:20][::-1].plot(kind='barh')

ax.set_title('Some title')
ax.set_ylabel('y label', fontsize=12)
ax.set_xlabel('x label', fontsize=12)


# Add figure in streamlit app
#st.pyplot(fig)

df1 = df['Rating_Score'].value_counts().rename_axis('unique_values').reset_index(name='counts')

#st.bar_chart(df1)
st.bar_chart(df.Rating_Score.value_counts())
#st.bar_chart(df.Rating_Score.value_counts().sort_values())
