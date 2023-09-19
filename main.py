import streamlit as st
import pandas as pd
data = {
    'A': [10, 15, 13, 17, 20],
    'B': [5, 8, 7, 10, 12],
    'C': [12, 10, 11, 9, 14]
}

df = pd.DataFrame(data)

st.title('👋🏻 Esto es un ejemplo.')
st.line_chart(df)

