import streamlit as st
import qrcode
import random
import pandas as pd
from io import BytesIO
from datetime import datetime

st.set_page_config("RiderGate | Booking", page_icon='🎫', layout='wide')

# Function to generate a random booking ID
def generate_booking_id():
    return f"{random.randint(1000, 9999)}-{random.randint(1000, 9999)}-{random.randint(1000, 9999)}"

def generate_qr_code(data):
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    qr.add_data(data)
    qr.make(fit=True)
    img = qr.make_image(fill_color="black", back_color="white")
    buffered = BytesIO()
    img.save(buffered, format="PNG")
    return buffered.getvalue()

def calculate_price(distance):
    try:
        distance = float(distance)
        price = distance * 5  # Assuming a rate of 5 INR per kilometer
        return price
    except ValueError:
        return None

def book_a_ride():
    ride_df = pd.read_csv("pages/rides.csv")
    user_df = pd.read_csv("pages/users.csv")
    payment_df = pd.read_csv("pages/payment.csv")
    parameters = st.query_params
    email = parameters.get_all(key='email')[0]

    firstname = user_df[user_df['email'] == email]['firstname']
    lastname = user_df[user_df['email'] == email]['lastname']
    st.title("Book Your Ride 📅")

    with st.form(key='booking_form'):
        name = f'{firstname[0]} {lastname[0]}'
        date = st.date_input("Date of Ride 🗓️", min_value=datetime.today())
        time_of_day = st.selectbox("Time of Day 🕒", ["Morning ☀️", "Afternoon 🌤", "Evening 🌙"])
        start = st.text_input("Start Location 🏠", placeholder="Where are you starting?")
        stop = st.text_input("Destination 🏁", placeholder="Where are you going?")
        distance = st.number_input("Distance (in kilometers) 🛣️", min_value=0.1, format="%f")
        bus_type = st.selectbox("Bus Type 🚌", ["Regular", "Luxury", "Sleeper", "AC"])

        submit_button = st.form_submit_button(label='Calculate Fare & Generate Ride Details 🛂', type='primary')

    if submit_button and all([name, date, time_of_day, start, stop, distance, bus_type]):
        booking_id = generate_booking_id()
        price = calculate_price(distance)

        if price is not None:
            st.markdown(f"### Fare Rate: 5 INR per kilometer\n### Estimated Fare: **{price:.2f} INR**")
           
            qr_data = f"Booking ID: {booking_id}\nName: {name}\nDate: {date}\nTime: {time_of_day}\nStart: {start}\nStop: {stop}\nDistance: {distance} km\nBus Type: {bus_type}\nPrice: {price:.2f} INR"
            qr_code_img = generate_qr_code(qr_data)

            st.success("Your ride has been booked! ✅")
            st.info(f"Booking ID: **{booking_id}**")
            st.header("Your QR Code for your journey. Try scanning this 💻:")
            st.image(qr_code_img, caption="Your Ride QR Code 🚍", use_column_width=False, width=300)
            with open('pages/rides.csv', 'a') as file:
                file.write(f'\n{email},{date},{start},{stop},{distance},{booking_id}')
            with open('pages/payment.csv', 'a') as file:
                file.write(f'\n{email},{date},{price},{bus_type},{booking_id}')
            st.markdown(f"""<div style='border: 2px solid white; border-radius: 20px; padding: 1rem; max-width:70vw; margin:auto;'>
    <h1 style='text-align: center;'>Boarding Pass 🎫</h1>
    <hr style='background-color:#fff; width: 60vw; height:1px; margin:auto; margin-bottom: 1rem; margin-top:1rem;'/>
    <table style='width:100%;'>
        <!-- First Row -->
        <tr>
            <td style='text-align: center;'><b>Name:</b> {name}</td>
            <td style='text-align: center;'><b>Date:</b> {date}</td>
            <td style='text-align: center;'><b>Time:</b> {time_of_day}</td>
        </tr>
        <!-- Second Row -->
        <tr>
            <td style='text-align: center;'><b>Bus Type:</b> {bus_type}</td>
            <td style='text-align: center;'><b>Start Location:</b> {start}</td>
            <td style='text-align: center;'><b>Destination:</b> {stop}</td>
        </tr>
        <!-- Third Row -->
        <tr>
            <td style='text-align: center;'><b>Booking ID:</b> {booking_id}</td>
            <td style='text-align: center;'><b>Distance:</b> {distance} km</td>
            <td style='text-align: center;'><b>Fare:</b> 💲{price:.2f} INR</td>
        </tr>
    </table>
   <style>
        button.payment {{
            background-color: #f8f9fa;
            color: #495057;
            border: 1px solid #ced4da;
            border-radius: 5px;
            padding: 10px 20px;
            max-width: 10.5rem;
            cursor: pointer;
            transition: background-color 0.3s, transform 0.3s, box-shadow 0.3s, width 0.5s;
        }}

        button.payment:hover {{
            background-color: #e9ecef;
            transform: scale(1.05);
            box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
            width: 200px;
            transition: all 0.3s ease-in-out;
        }}

        button.payment::after {{
            content: '💵';
            margin-left: 5px;
            opacity: 0;
            transition: opacity 0.5s ease-in;
        }}

        button:hover::after {{
            opacity: 1;
        }}
    </style>
</div>
<br>
<br>
""", unsafe_allow_html=True)
            st.link_button("Back to dashboard ➡️", url=f'/Dashboard?email={email}', type='primary')
        else:
            st.error("Invalid distance input. Please enter a valid distance in kilometers.")
    elif submit_button:
        st.warning("⚠️ Please fill in all the fields.")
if __name__ == "__main__":
    book_a_ride()
