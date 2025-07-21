import tkinter as tk
from tkinter import messagebox
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

def send_email():
    sender = sender_entry.get()
    app_pass = app_pass_entry.get()
    receiver = receiver_entry.get()
    subject = subject_entry.get()
    body = body_text.get("1.0", tk.END)

    try:
        # MIME setup
        msg = MIMEMultipart()
        msg['From'] = sender
        msg['To'] = receiver
        msg['Subject'] = subject
        msg.attach(MIMEText(body, 'html'))  # Use 'html' for formatting

        # Gmail server
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login(sender, app_pass)
        server.send_message(msg)
        server.quit()

        messagebox.showinfo("Success", "Email sent successfully!")
    except Exception as e:
        messagebox.showerror("Error", str(e))

# GUI
root = tk.Tk()
root.title("Email Sender")
root.geometry("500x500")

tk.Label(root, text="Sender Email:").pack()
sender_entry = tk.Entry(root, width=50)
sender_entry.pack()

tk.Label(root, text="App Password:").pack()
app_pass_entry = tk.Entry(root, width=50, show="*")
app_pass_entry.pack()

tk.Label(root, text="Receiver Email:").pack()
receiver_entry = tk.Entry(root, width=50)
receiver_entry.pack()

tk.Label(root, text="Subject:").pack()
subject_entry = tk.Entry(root, width=50)
subject_entry.pack()

tk.Label(root, text="Email Body:").pack()
body_text = tk.Text(root, height=10, width=50)
body_text.pack()

send_button = tk.Button(root, text="Send Email", command=send_email)
send_button.pack(pady=10)

root.mainloop()
