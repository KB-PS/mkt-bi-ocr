import streamlit as st
from random import choice
from utilities import load_css

st.set_page_config(page_title="Apples")

#st.header("Results of invoice processing")

load_css()



files = st.session_state.get("files", [])

processing_results = []

if files:
    title = '<p style="font-family:sans-serif; color:#121212; font-size: 42px;">Results of invoice processing</p>'
    st.markdown(title, unsafe_allow_html=True)


    for k,v in files.items():
        for item in v:
            ch = choice([True, False])
            if ch:
                st.success(item)
                processing_results.append({"id":item.id, "name":item.name, "processed":ch, "error":''})
            else:
                st.error(item)
               # processing_results[item.id]={"processed":ch, "error":f'OCR could not read the file {item.name}'}
                processing_results.append({"id":item.id, "name":item.name,"processed":ch, "error":f'OCR could not read the file {item.name}'})


#st.write(processing_results)
st.session_state["processing_results"]=processing_results