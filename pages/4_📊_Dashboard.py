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

ride_df = pd.read_csv("pages/rides.csv")
user_df = pd.read_csv("pages/users.csv")
payment_df = pd.read_csv("pages/payment.csv")


def display_dashboard():
    parameters = st.query_params
    email = parameters.get_all(key='email')[0]
    rides_df = ride_df[ride_df['email'] == email][['date','bookingid', 'start', 'end' ,'distance']]
    rides_df = rides_df.rename(columns={'bookingid': 'Booking ID','date': 'Date', 'start': 'Start Location', 'end': 'Destination', 'distance': 'Distance (km)'})
    firstname = user_df[user_df['email'] == email]['firstname']
    lastname = user_df[user_df['email'] == email]['lastname']
    payments_df = payment_df[payment_df['email'] == email][['date', 'bookingid', 'bustype','amount']]
    payments_df = payments_df.rename(columns=({'date': 'Date', 'bookingid': 'Booking ID', 'amount': 'Amount (₹)', 'bustype': 'Bus'}))

    # Streamlit app
    st.title("User Dashboard 📊")

    # Display user information
    st.sidebar.subheader("👤 User Information")
    st.sidebar.write(f"👤 Name: {firstname[0]} {lastname[0]}")
    st.sidebar.write(f"✉️ Email: {email}")

    # Rides section
    st.header("🚗 Rides History")

    # Apply styling to the rides table
    st.table(rides_df)
    st.link_button(label="Book a new ride", url=f'/Booking?email={email}', type='primary')

    # Payments section
    st.header("💰 Payments History")

    # Apply styling to the payments table
    st.table(payments_df)

display_dashboard()