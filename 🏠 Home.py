import streamlit as st
import qrcode
from io import BytesIO
from PIL import Image



# Custom function for spacing
def add_spacing(lines=1):
    for _ in range(lines):
        st.write("")

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
    return img

def pil_to_bytes(img):
    buffered = BytesIO()
    img.save(buffered, format="PNG")
    return buffered.getvalue()

def main():
    st.set_page_config(page_title="RiderGate | Secure & Contactless Booking", layout="wide", page_icon='🚌')

    # Apply custom styles to the entire app
    st.markdown("""
        <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.3.1/css/bootstrap.min.css">
        <link href="https://fonts.googleapis.com/css2?family=Montserrat:wght@400&family=Raleway:wght@300&family=Roboto:wght@400&display=swap" rel="stylesheet">
        <style>
            .title {
                font-family: 'Raleway', sans-serif;
                font-size: 2.5em;
                font-weight: bold;
                color: #333;
            }
            .subheader {
                font-family: 'Raleway', sans-serif;
                font-size: 1.5em;
                font-weight: bold;
                color: #555;
            }
            .text {
                color: #333;
            }
            .button {
                background-color: #333;
                color: #fff;
                padding: 10px 20px;
                font-family: 'Raleway', sans-serif;
                font-size: 1.2em;
                border: none;
                border-radius: 5px;
                cursor: pointer;
            }
            .button:hover {
                background-color: #555;
            }
                .ridergate{
                font-family: 'Raleway',sans-serif;
                font-size:3.5rem;
                }
        </style>
    """, unsafe_allow_html=True)


def show_home_page():
    # Header Section with App Name, Slogan, and Description
    st.markdown("<h1 style='text-align: center;' class='ridergate'>RiderGate</h1>", unsafe_allow_html=True)
    st.markdown("<h2 style='text-align: center;'>Efficient. Fast. Easy.<br>Your Gateway to Effortless Travel</h2>", unsafe_allow_html=True)
    add_spacing(2)
    st.markdown("""
    Welcome to **RiderGate**, the future of bus travel. With our innovative contactless ticketing and boarding system, you can skip the lines, manage your trips more efficiently, and enjoy a seamless travel experience. Whether you're commuting to work, exploring the city, or traveling to a new destination, RiderGate makes it easier than ever.
    """, unsafe_allow_html=True)

    # Features Section
    st.markdown("<h1 style='text-align: center;'>Why RiderGate?</h2>", unsafe_allow_html=True)
    col1, col2, col3 = st.columns(3)
    with col1:
        st.markdown("#### **🚀 Fast Boarding**")
        st.markdown("Scan your QR code ticket and board the bus in seconds.")
    with col2:
        st.markdown("#### **💳 Easy Payments**")
        st.markdown("Pay securely with your preferred digital wallet or credit card.")
    with col3:
        st.markdown("#### **🌍 Smart Destinations**")
        st.markdown("Select your destination and get fare information instantly.")
    add_spacing(3)

    st.markdown("<h1 style='text-align: center;'>How It Works</h2>", unsafe_allow_html=True)
    st.markdown("""
    ##### Follow these simple steps to get started with RiderGate:
    ###### 1. **Select Your Destination**: Choose where you're headed and see the fare.
    ###### 2. **Make a Payment**: Use our secure payment system to pay for your ticket.
    ###### 3. **Generate Your Ticket**: Receive a QR code as your digital ticket.
    ###### 4. **Scan and Board**: Just scan your QR code when boarding. Enjoy your trip!
    """)

    # Expanding How It Works with Interactive Elements
    with st.expander("See More on How RiderGate Enhances Your Travel Experience"):
        st.markdown("""
        - **Contactless and Cashless**: Say goodbye to cash handling and paper tickets. With RiderGate, your phone is your ticket.
        - **Eco-Friendly**: By choosing RiderGate, you're also making an eco-friendly choice. Less paper means a happier planet.
        - **User-Friendly**: Our app is designed for everyone. Easy navigation, clear instructions, and a clean interface make your experience stress-free.
        """)

    # Example QR Code Generation (for demonstration, replace with actual functionality)
    with st.expander("Try Generating a Sample Ticket"):
        if st.button("Generate Sample Ticket", key='Generate'):
            qr_data = 'Sample Ticket Data for RiderGate'
            qr_code_img = generate_qr_code(qr_data)
            qr_code_bytes = pil_to_bytes(qr_code_img)

            # Display the QR Code Image
            st.image(qr_code_bytes, caption="Your Sample RiderGate Ticket")


    # Adding a footer for aesthetics
    st.markdown("""
    ---
    <p style='text-align: center;'>Ⓒ 2024 RiderGate. Travel Simplified.</p>
    """, unsafe_allow_html=True)



if __name__ == "__main__":
    main()
    show_home_page()
