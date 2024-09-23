import streamlit as st
import streamlit.components.v1 as stc

from ml_text_appp import run_ml_text_app

def main():
    menu = ['Home', 'Machine Learning']
    choice = st.sidebar.selectbox('Menu', menu)

    if choice == 'Home':
        st.subheader('Welcome to Rexus Final Project')
    elif choice == 'Machine Learning':
        #st.subheader('Welcome to Our Machine Learning')
        run_ml_text_app()

        
if __name__ == '__main__':
    main()