import streamlit as st
from streamlit_option_menu import option_menu

# 1. as sidebar menu
with st.sidebar:
    # selected = option_menu("Main Menu", ["Home", 'Settings'],
    #                        icons=['dashboard', 'gear'], menu_icon="cast", default_index=1)
    # selected
    # 1. as sidebar menu
    # 1. as sidebar menu
    selected = option_menu(
        menu_title= None,
        options = ["Home", "Upload", "Tasks", 'Settings'],
        icons=['house', 'cloud-upload', "list-task", 'gear'],
        menu_icon="cast", default_index=0, orientation="vertical",
        styles={
            "container": {"padding": "0!important", },
            "icon": {"color": "orange", "font-size": "25px"},
            "nav-link": {"font-size": "25px", "text-align": "left", "margin": "0px",
                         "--hover-color": "#eee"},
            "nav-link-selected": {"background-color": "green"},
        }
    )

if selected == 'Home':
    st.title(f'You have selected {selected}')
if selected == 'Upload':
    st.title(f'You have selected {selected}')
if selected == 'Tasks':
    st.title(f'You have selected {selected}')
if selected == 'Settings':
    st.title(f'You have selected {selected}')