import streamlit as st
import qrcode

# Setting page configuration for a better visual appeal
st.set_page_config(page_title="RiderGate", page_icon=":bus:", layout="wide")

def show_discover_more_page():
    # Inject custom CSS for horizontal scrolling in testimonials section
    st.markdown("""
    <style>
    .horizontal-scroll {
    display: flex;
    overflow-x: auto;
    white-space: nowrap;
    }
    .horizontal-scroll > div {
    flex: none;
    }
    </style>
    """, unsafe_allow_html=True)

    # Main title for the "About Us" page
    st.title("About RiderGate 🚍")

    # Introduction and mission statement of RiderGate
    st.markdown("""
    Welcome to **RiderGate**, the future of bus travel, where convenience meets technology to offer you a seamless, contactless ticketing experience. Our mission is to revolutionize the way you travel by bus, making it more efficient, eco-friendly, and effortless than ever before. With RiderGate, your journey is just a tap away. Say goodbye to long lines and complicated booking processes, and hello to a smarter way of traveling.
    """)

    # Explanation of how the service works
    st.header("How It Works 🛠️")
    st.markdown("""
    - **Choose Your Destination 🌐**: Start by selecting where you want to go. Our system immediately calculates the best routes and fares for you, ensuring you always get the best deal.
    - **Book & Pay 💳**: Book your ticket using our secure payment system. Whether you prefer credit/debit cards, e-wallets, or even crypto, we've got you covered.
    - **Travel 🚌**: Use the QR code sent to your device to board the bus. Enjoy your ride with no further check-ins required. It's that simple!
    """)

    # Section highlighting the reasons to choose RiderGate
    st.header("Why Choose RiderGate? 🤔")
    st.markdown("""
    - **Efficiency**: With RiderGate, skip the lines and the waiting. Your ticket is just a few clicks away.
    - **Flexibility**: Change of plans? No problem. Easily modify or cancel your booking with a few taps.
    - **Sustainability**: Our paperless ticketing system means every ride with us is a step towards a greener planet. 🌍
    - **Affordability**: Enjoy competitive pricing with no hidden fees. We believe in transparency and value for every mile.
    """)

    # Testimonials section with horizontal scrolling
    st.header("Hear From Our Users 🗣️")
    testimonials = [
        ("John Doe", "“RiderGate has transformed my daily commute. It's fast, reliable, and so easy to use. I can't imagine going back to the old way of traveling.”"),
        ("Jane Smith", "“I love the flexibility RiderGate offers. Last-minute changes are no longer a headache. Plus, it feels good to support a service that's environmentally friendly.”"),
        ("Emma Brown", "“The customer service is top-notch! Had an issue with my booking and it was resolved in minutes. Definitely using RiderGate for all my city travels.”"),
    ]

    # Creating a container and columns for each testimonial for horizontal scroll
    container = st.container()
    all_columns = container.columns(len(testimonials))

    for i, (name, testimonial) in enumerate(testimonials):
        with all_columns[i]:
            st.markdown(f"**{name}** says:")
            st.markdown(f"> {testimonial}")

    # Section about the founders of RiderGate
    st.header("About the Founders 👨‍💻👩‍💻")
    st.markdown("""
    ### Vedant Saini
    A grade 11 student at Vasant Valley School, Vedant is deeply passionate about digital solutions and coding. With a keen interest in the environment, Vedant believes in leveraging technology to create sustainable solutions for everyday challenges. His curiosity and commitment to ethics drive him to innovate and push the boundaries of what's possible.
    """)
    st.markdown("""
    ### Savya Meattle
    Also in grade 11 at Vasant Valley School, Savya shares a similar enthusiasm for digital innovation and the environment. Her love for learning and a strong ethical foundation inspire her to explore new horizons in technology and sustainability. Together, Vedant and Savya aim to make a significant impact through RiderGate, combining their skills and passions to transform the public transportation landscape.
    """)

    # Footer section
    st.markdown("---")
    st.write("© 2024 RiderGate. Simplifying Your Journey.")

show_discover_more_page()