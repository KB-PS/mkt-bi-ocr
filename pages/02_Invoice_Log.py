import streamlit as st
from utilities import load_css
import pandas as pd

st.set_page_config(page_title="Oranges")

load_css()
#st.header("Detailed log")

load_css()

processing_results = st.session_state.get("processing_results", [])

if processing_results:
    title = '<p style="font-family:sans-serif; color:#121212; font-size: 42px;">Detailed log</p>'
    st.markdown(title, unsafe_allow_html=True)

    #st.write(processing_results)
    df = pd.DataFrame.from_dict(processing_results)
    df.set_index("id", inplace=True)
    st.dataframe(df)