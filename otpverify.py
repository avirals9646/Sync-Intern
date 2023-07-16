import random
import smtplib
import tkinter as tk
from tkinter import messagebox

# Generating a random 6 digit number as OTP
OTP = random.randint(100000, 999999)

# Setting up server
server = smtplib.SMTP("smtp.gmail.com", 587)  # server code of gmail is 587
server.starttls()  # for security

# Create a tkinter window
window = tk.Tk()
window.title("OTP Verification")


# Function to send OTP
def send_otp():
    receiver_email = receiver_email_entry.get()

    email_check1 = ["gmail", "hotmail", "yahoo", "outlook"]
    email_check2 = [".com", ".in", ".org", ".edu", ".co.in"]

    count = 0

    for domain in email_check1:
        if domain in receiver_email:
            count += 1
    for site in email_check2:
        if site in receiver_email:
            count += 1

    if "@" not in receiver_email or count != 2:
        messagebox.showerror("Invalid Email ID", "Please enter a valid Email ID.")
        return

    # Generate a new OTP
    global OTP
    OTP = random.randint(100000, 999999)

    password = "lvbvlcwdzzfijnwy"  # password to get into the sender's gmail account
    server.login("aviralunited@gmail.com", password)  # logging into the sender's gmail account

    body = "Your One Time Password (OTP) is " + str(OTP) + "."  # generating a message
    subject = "One Time Password (OTP) for verification"
    message = f'Subject:{subject}\n\n{body}'

    server.sendmail("aviralunited@gmail.com", receiver_email, message)
    messagebox.showinfo("OTP Sent", "OTP has been sent to " + receiver_email)

# Function to verify OTP
def verify_otp():
    entered_otp = otp_entry.get()

    if entered_otp == str(OTP):  # verifying the entered OTP
        messagebox.showinfo("OTP Verified", "OTP Verified!")
    else:
        messagebox.showerror("Invalid OTP", "Invalid OTP! Please try again.")

# Create a frame
frame = tk.Frame(window)
frame.pack(pady=20)

# Create email label and entry
receiver_email_label = tk.Label(frame, text="Email ID:")
receiver_email_label.pack(side="left")
receiver_email_entry = tk.Entry(frame)
receiver_email_entry.pack(side="left")

# Create send OTP button
send_otp_btn = tk.Button(window, text="Send OTP", command=send_otp)
send_otp_btn.pack(pady=10)

# Create OTP label, entry, and verify OTP button (hidden initially)
otp_label = tk.Label(window, text="Enter OTP:")
otp_entry = tk.Entry(window)
verify_otp_btn = tk.Button(window, text="Verify OTP", command=verify_otp)

# Function to show OTP entry and verify OTP button
def show_otp_entry():
    send_otp_btn.pack_forget()
    otp_label.pack()
    otp_entry.pack()
    verify_otp_btn.pack()

# Function to reset the UI
def reset_ui():
    receiver_email_entry.delete(0, tk.END)
    otp_entry.delete(0, tk.END)
    send_otp_btn.pack()
    otp_label.pack_forget()
    otp_entry.pack_forget()
    verify_otp_btn.pack_forget()

# Create reset button
reset_btn = tk.Button(window, text="Reset", command=reset_ui)
reset_btn.pack()

# Start the tkinter event loop
window.mainloop()

# Close the server connection
server.quit()
