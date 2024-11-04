import streamlit as st
from logics.customer_query_handler import process_user_message
from helper_functions.utility import check_password

# region <--------- Streamlit App Configuration --------->
st.set_page_config(
    layout="centered",
    page_title="My Streamlit App"
)

# endregion <--------- Streamlit App Configuration --------->

st.title("Health Buddy") 

if not check_password():  
    st.stop()

st.image("./images/health_icon.png", caption="Onwards to a healthier lifestyle!")
with st.expander("IMPORTANT NOTICE (DISCLAIMER)"):
    st.write("""
    This web application is a prototype developed for educational purposes only. The information provided here is NOT intended for real-world usage and should not be relied upon for making any decisions, especially those related to financial, legal, or healthcare matters.

    Furthermore, please be aware that the LLM may generate inaccurate or incorrect information. You assume full responsibility for how you use any generated output.

    Always consult with qualified professionals for accurate and personalized advice.
    """)

form = st.form(key="form")
form.subheader("Kindly indicate your preferred type of exercise, and we will recommend the most suitable options provided by the Health Promotion Board.")

user_prompt = form.text_area("Enter your prompt here", height=200)

if form.form_submit_button("Submit"):
    st.toast(f"User Input Submitted - {user_prompt}")
    response = process_user_message(user_prompt) #<--- This calls the `process_user_message` function that we have created 🆕
    st.write(response)
    print(f"User Input is {user_prompt}")

    