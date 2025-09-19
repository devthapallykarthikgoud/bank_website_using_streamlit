💳 Bank Website Using Streamlit
<p align="center"> <i>An interactive banking web application built with Python and Streamlit.</i> </p> <p align="center"> <a href="https://innomaticsbank.streamlit.app/" target="_blank">🔗 Live Demo</a> </p>
📌 Table of Contents

About

Features

Tech Stack

Installation

Usage

Contributing

🧾 About

Bank Website Using Streamlit is a simple yet interactive web application that simulates a bank system. It allows users to:

Register new accounts.

Log in securely.

View account details, balance, and transaction history.

Deposit or withdraw funds (simulation).

This project is designed for learning purposes, to demonstrate Python web development and interactive UI creation using Streamlit.

✨ Features

✅ User Registration & Login: Secure account creation and authentication.

✅ Dashboard: View account information and transaction history.

✅ Transaction Simulation: Deposit and withdraw funds.

✅ Responsive Design: User-friendly UI with background images and styled components.

✅ Email OTP Verification: Validates user email during registration.

⚙️ Tech Stack
Component	Technology
Frontend	Streamlit
Backend	Python
Database	SQLite
Email	SMTP (Gmail)
📥 Installation
Prerequisites

Python 3.7+

Pip (Python package manager)

Steps

Clone the repository

git clone https://github.com/devthapallykarthikgoud/bank_website_using_streamlit.git
cd bank_website_using_streamlit


Create a virtual environment

python -m venv venv


Activate the environment

Windows

.\venv\Scripts\activate


macOS/Linux

source venv/bin/activate


Install dependencies

pip install -r requirements.txt


Run the application

streamlit run streamlit.py

🚀 Usage

After running the application, open your browser at http://localhost:8501 or visit the Live App
. Users can:

Register a new account with email and password.

Verify OTP sent to their email.

Log in using account number and password.

Access dashboard to view profile, balance, and perform simulated transactions.

Logout to end the session.

🤝 Contributing

We welcome contributions! Here's how to contribute:

Fork the repository

Create a feature branch

git checkout -b feature-branch


Make your changes and commit

git commit -m "Add new feature"


Push to your branch

git push origin feature-branch


Open a Pull Request and describe your changes.

Please follow the existing code style and include appropriate documentation.
