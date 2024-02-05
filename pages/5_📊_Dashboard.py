import streamlit as st
import pandas as pd

# Sample data for rides and payments
rides_data = {
    'Date': ['2024-01-01', '2024-01-05', '2024-01-10'],
    'Start': ['Home', 'Office','Delhi'],
    'Destination': ['Work', 'Gym', 'Kolkata'],
    'Distance (km)': [10, 5, 800],
}

payments_data = {
    'Date': ['2024-01-01', '2024-01-05', '2024-01-10'],
    'Amount (₹)': [1500, 700, 2000],
}

# User details
user_name = "John Doe"
user_email = "john.doe@example.com"


def display_dashboard(user_name, user_email, rides_data, payments_data):
    parameters = st.query_params
    print(parameters.get_all(key='email'))
    rides_df = pd.DataFrame(rides_data)
    payments_df = pd.DataFrame(payments_data)

    # Streamlit app
    st.title("User Dashboard 📊")

    # Display user information
    st.sidebar.subheader("👤 User Information")
    st.sidebar.write(f"👤 Name: {user_name}")
    st.sidebar.write(f"✉️ Email: {user_email}")

    # Rides section
    st.header("🚗 Rides History")

    # Apply styling to the rides table
    st.table(rides_df)

    # Payments section
    st.header("💰 Payments History")

    # Apply styling to the payments table
    st.table(payments_df)

display_dashboard(user_name,user_email,rides_data,payments_data)