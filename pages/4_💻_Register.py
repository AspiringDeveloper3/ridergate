import streamlit as st
import pandas as pd

# Load user data from CSV
df = pd.read_csv('pages/users.csv')

def login():
    st.header("Login")

    email = st.text_input("📧 Email:", key='login_email')
    password = st.text_input("🔒 Password", type="password")

    login_button = st.button("Login 👉", key='login_button', type='primary')
    if login_button and email != '' and password != '':
        df = pd.read_csv('pages/users.csv')

        is_valid_user = False
        # Add your authentication logic here
        for index,value in df.iterrows():
            if [email, password] == [value[2], value[3]]:
                is_valid_user=True
        if is_valid_user:
            st.success("🎉 Login successful!")
            # Provide a link to the Dashboard
            st.link_button(label="Go to Dashboard ➡️", url=f"/Dashboard?email={email}", type='primary')

        else:
            st.error("❌ Invalid username or password")
    elif login_button:
        st.warning("⚠️ Please fill in all required fields before logging in.")

def register():
    st.header("Register")

    first_name = st.text_input("First Name:")
    last_name = st.text_input("Last Name:")
    email = st.text_input("📧 Email:", key='register_email')
    new_password = st.text_input("🔒 New Password", type="password")
    confirm_password = st.text_input("🔒 Confirm Password", type="password")

    registration_button = st.button("Register 👉", key='registration_button', type='primary')
    if registration_button and all([first_name, last_name, email, new_password, confirm_password]):
        if first_name == '':
            st.error("❌ Please fill the **First name** field.")
        elif last_name == '':
            st.error("❌ Please fill the **Last name** field.")
        elif email == '':
            st.error("❌ Please fill the **Email** field.")
        elif new_password == '':
            st.error("❌ Please create a new password.")
        # Add your registration logic here
        if new_password == confirm_password:
            st.success("🎉 Registration successful!")
            # Provide a link to the Dashboard
            st.link_button(label="Go to Dashboard ➡️", url=f"/Dashboard?email={email}", type='primary')
            with open("pages/users.csv", 'a') as file:
                file.write(f'\n{first_name},{last_name},{email},{new_password}')
            # Reload user data after registration
            global df
            df = pd.read_csv('pages/users.csv')
        else:
            st.error("❌ Passwords do not match")
    elif registration_button:
        st.warning("⚠️ Please fill in all the required fields before attempting registration.")


def main():

    st.set_page_config(page_title="RiderGate | Register", layout="wide", page_icon='💻')
    st.markdown("""
<style>
                #register, #login{
                text-align:center;
            }
                </style>
""", unsafe_allow_html=True)

    # Custom function for spacing
    def add_spacing(lines=1):
        for _ in range(lines):
            st.write("")
    st.markdown("<h1 style='text-align:center;'>User Authentication 🚀</h1>", unsafe_allow_html=True)
    col1, col2, col3 = st.columns(3)
    with col1:
        register()

    with col2:
        # Vertical Separation
        st.markdown("<hr style='width:1px; height:80vh; background-color:white; margin:auto;'>", unsafe_allow_html=True)
    with col3:
        login()


if __name__ == "__main__":
    main()
