import streamlit as st
import streamlit_authenticator as stauth
from collections import defaultdict
import yaml
from utilities import load_css

st.set_page_config(
    page_title="Invoice Processing",
    page_icon="✉️",
)

load_css()

with open('.config.yaml') as file:
    config = yaml.load(file, Loader=yaml.SafeLoader)

authenticator = stauth.Authenticate(
    config['credentials'],
    config['cookie']['name'],
    config['cookie']['key'],
    config['cookie']['expiry_days'],
    config['preauthorized']
)

name, authentication_status, username = authenticator.login('Login', 'main')
    
if st.session_state["authentication_status"]:
    authenticator.logout('Logout', 'main')
    st.title('Welcome to the OCR application')
    st.write(f'Welcome *{st.session_state["name"]}*')
elif st.session_state["authentication_status"] == False:
    st.error('Username/password is incorrect')
elif st.session_state["authentication_status"] == None:
    st.warning('Please enter your username and password')
    
if st.session_state["authentication_status"]:
    
    
    cont = st.container()
    st.markdown("---")
    cols = st.columns(2)
    
    files = defaultdict(list)
    #st.session_state["files"] = files
    
    with cols[0]:
        with st.container():
            st.markdown("## Škoda auto")
            key = "spare_parts_skoda"
            spare_parts_skoda = st.file_uploader("Spare parts", accept_multiple_files=True, key=key)
            if spare_parts_skoda:
                files[key] = spare_parts_skoda

            key = "new_cars_skoda"
            new_cars_skoda = st.file_uploader("New cars", accept_multiple_files=True, key=key)
            if new_cars_skoda:
                files[key] = new_cars_skoda

    with cols[1]:
        with st.container():
            st.markdown("## Porsche")
            key = "new_cars_porsche"
            uploaded_files2 = st.file_uploader("Choose a Porsche invoice", accept_multiple_files=True, key=key)
            if uploaded_files2:
                files[key] = new_cars_skoda
                
    st.session_state["files"] = files
            