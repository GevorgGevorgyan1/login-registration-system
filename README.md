# Login and Registration System (Tkinter)

This is a login and registration system built with **Python** and **Tkinter**. It allows users to register with a username and password and then log in with the credentials. The system stores the usernames and passwords in a text file (`username_and_password.txt`).

## Features

- **Login**: Users can log in by entering their username and password.
- **Registration**: Users can create a new account by entering a username and password.
- **Password Visibility Toggle**: Click on the eye icon to toggle the visibility of the password.
- **Text File Storage**: User credentials are stored in a plain text file (`username_and_password.txt`).
- **GUI**: A simple and intuitive graphical user interface built using Tkinter.

## Requirements

- Python 3.x
- Tkinter library (comes pre-installed with Python)

## Files

- `login_registration_system.py`: The main Python file with the logic for login, registration, and password management.
- `username_and_password.txt`: The text file where user credentials are stored.
- `eye-open.png` & `eye-closed.png`: Images for toggling the visibility of the password.
- `login.png`, `sign_up.png`: Background images used in the login and registration screens.

## How to Run

1. Clone the repository:

    ```bash
    git clone https://github.com/GevorgGevorgyan1/login-registration-system.git
    ```

2. Navigate to the project directory:

    ```bash
    cd login-registration-system
    ```

3. Make sure you have the required image files in your directory (e.g., `login.png`, `sign_up.png`, `eye-open.png`, and `eye-closed.png`).

4. Run the Python script:

    ```bash
    python login_registration_system.py
    ```

5. The GUI window will appear, allowing you to either log in or sign up.

## How to Use

- **Login**: Enter your username and password and click "Sign in."
- **Sign Up**: If you don't have an account, click "Sign up" and enter a username and password. The credentials will be stored in the `username_and_password.txt` file.
