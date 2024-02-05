import streamlit as st

def customer_feedback():

    # Header
    st.title("Contact Us & Customer Service")

    # Contact Information
    st.header("Contact Information")
    st.markdown(
        "If you have any questions or need assistance, please feel free to reach out to us."
    )

    # Email
    st.subheader("Email")
    st.write("📧 support@ridergate.com")

    # Phone
    st.subheader("Phone")
    st.write("📞 +91 82873 63535 | 📞 +91 97675 23123 ")

    # Address
    st.subheader("Address")
    st.write("🏢 Train road, Vasant Kunj, Sector-7")

    # Social Media
    st.subheader("Social Media")
    st.write("Follow us on social media for updates:")
    st.write("📱 [Facebook](https://www.facebook.com/ridergate)")
    st.write("📱 [Twitter](https://www.twitter.com/ridergate)")
    st.write("📱 [Instagram](https://www.instagram.com/ridergate)")

    # Customer Service Hours
    st.header("Customer Service Hours")
    st.write("Our customer service team is available during the following hours:")
    st.write("🕒 Monday to Friday: 9:00 AM - 5:00 PM")
    st.write("🕒 Saturday: 10:00 AM - 2:00 PM")
    st.write("🕒 Sunday: Closed")

    # Feedback Form
    st.header("Send us your feedback!")
    st.write("We value your feedback. Please use the form below to send us your comments, suggestions, or concerns.")
    feedback = st.text_area("Enter your feedback here:")
    if st.button("Submit Feedback"):
        # You can add code here to handle feedback submission, e.g., store it in a database
        st.success("Thank you for your feedback! We will get back to you soon.")

    # Footer
    st.write("RiderGate - Contactless Ticketing and Boarding Web App for Buses")

customer_feedback()