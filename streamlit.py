import streamlit as st
import random
import smtplib
from email.message import EmailMessage
import sqlite3

st.markdown(
    """
    <style>
    .stApp{
        background-image:url("https://imgs.search.brave.com/EwTWXx7W4QwXThlal6eV-E0DqiQm-x1_b7Lq1IRniTw/rs:fit:860:0:0:0/g:ce/aHR0cHM6Ly9jb250/ZW50LmpkbWFnaWNi/b3guY29tL3YyL2Nv/bXAvcHVuZS92Mi8w/MjBweHgyMC54eDIw/LjI1MDIwODEyMzA1/MS5jNXYyL2NhdGFs/b2d1ZS9pbm5vbWF0/aWNzLXJlc2VhcmNo/LWxhYnMta290aHJ1/ZC1wdW5lLWRhdGEt/c2NpZW5jZS10cmFp/bmluZy1pbnN0aXR1/dGVzLXFkOGEybTFu/ZmEuanBnP3c9Mzg0/MCZxPTc1");
        background-size:cover;
        background-repeat:no-repeat;
    }
    </style>
    """,
    unsafe_allow_html=True
)

conn = sqlite3.connect("bank_users.db")
c = conn.cursor()
c.execute("""
CREATE TABLE IF NOT EXISTS users (
    account_number TEXT PRIMARY KEY,
    name TEXT NOT NULL,
    email TEXT NOT NULL UNIQUE,
    password TEXT NOT NULL
)
""")
conn.commit()

if "page" not in st.session_state:
    st.session_state.page = "login"

def go_to_login():
    st.session_state.page = "login"
    st.rerun()

def go_to_register():
    st.session_state.page = "register"
    st.rerun()

def send_otp(to_email):
    otp = ''.join([str(random.randint(0, 9)) for _ in range(6)])
    st.session_state.otp = otp
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    from_email = 'indianh4cker123@gmail.com'
    password = 'abry sasx tuqp bodm'
    server.login(from_email, password)
    msg = EmailMessage()
    msg['Subject'] = "OTP Verification"
    msg['From'] = from_email
    msg['To'] = to_email
    msg.set_content(f'Your OTP is: {otp}')
    server.send_message(msg)
    server.quit()
    st.success("OTP successfully sent!")

def generate_account_number():
    return ''.join([str(random.randint(0, 9)) for _ in range(10)])

if st.session_state.page == "login":
    st.title("INNOMATICS BANK")
    with st.form("Login"):
        account_number = st.text_input("Enter your account number")
        Pin = st.text_input("Enter your pin", type="password")
        submitted = st.form_submit_button("Login")
        if submitted:
            c.execute("SELECT * FROM users WHERE account_number=? AND password=?", (account_number, Pin))
            user = c.fetchone()
            if user:
                st.success(f"Welcome {user[1]}!")
            else:
                st.error("Invalid account number or pin")
    st.write("New to bank? Please register")
    if st.button("Register"):
        go_to_register()

elif st.session_state.page == "register":
    st.title("Register Page")
    name = st.text_input("Full Name")
    email = st.text_input("Email")
    password = st.text_input("Password", type="password")
    if st.button("Send OTP"):
        if email.endswith("@gmail.com"):
            send_otp(email)
        else:
            st.error("Please enter a valid Gmail address")
    if "otp" in st.session_state:
        verify_otp = st.text_input("Enter OTP sent to your email")
        if st.button("Verify OTP"):
            if verify_otp == st.session_state.otp:
                account_number = generate_account_number()
                try:
                    c.execute("INSERT INTO users (account_number, name, email, password) VALUES (?, ?, ?, ?)",
                              (account_number, name, email, password))
                    conn.commit()
                    st.success(f"Registration successful! Your account number is: {account_number}")
                    
                except sqlite3.IntegrityError:
                    st.error("Email already registered!")
                if st.button("Go Back to login"):
                        go_to_login()
            else:
                st.error("Incorrect OTP, try again.")


