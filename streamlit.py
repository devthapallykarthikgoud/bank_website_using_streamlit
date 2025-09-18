import streamlit as st
import random
import smtplib
from email.message import EmailMessage
import sqlite3

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

def go_to_register():
    st.session_state.page = "register"

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
                    go_to_login()
                except sqlite3.IntegrityError:
                    st.error("Email already registered!")
            else:
                st.error("Incorrect OTP, try again.")
