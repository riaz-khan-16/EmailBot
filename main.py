import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import os
from dotenv import  load_dotenv

def send_email(sender_email, app_password, receiver_email, subject, body_html):
    try:
        # Set up the MIME
        msg = MIMEMultipart()
        msg['From'] = sender_email
        msg['To'] = receiver_email
        msg['Subject'] = subject

        # Add body
        msg.attach(MIMEText(body_html, 'html'))

        # Create server
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()

        # Login
        server.login(sender_email, app_password)

        # Send email
        server.send_message(msg)
        server.quit()
        print("Email sent successfully!")

    except Exception as e:
        print(f"Error: {e}")

# Example usage
if __name__ == "__main__":
    sender = "riaz222666@gmail.com"
    load_dotenv()
    app_pass = os.getenv("app_pass")  # Not your Gmail password
    receiver = "riaz.khan.ruet@gmail.com"

    #
    
    # email_body = "Hi Riaz Khan!"
    # Professional email content
    email_body = """
    <html>
        <body>
            <p>Dear Professor,</p>
            
            <p>I hope this email finds you well.</p>
            
            <p>
                I am writing to express my interest in your research on 
                <b>Control Systems and AI</b>. I have a background in 
                <i>Machine Learning</i> and would love to collaborate 
                or learn more about your work.
            </p>
            
            <p>
                Looking forward to your response.<br>
                Best regards,<br>
                <b>Riaz Khan</b><br>
                Mechatronics Engineer
            </p>
        </body>
    </html>
    """

    send_email(sender, app_pass, receiver, "Prospective ", email_body)
