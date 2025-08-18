
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import os
from dotenv import load_dotenv

#for attaching cv
from email.mime.base import MIMEBase
from email import encoders




class EmailSender:

    def __init__(self, sender, receiver, subject, body):
        self.sender=sender
        self.receiver=receiver
        self.subject=subject
        self.body=body

    def attachCV(self):
        filename = "Riaz_Khan_Resume.pdf"           # name of the file
        

    def sendEmail(self):
        try:
            # Set up the MIME
            msg = MIMEMultipart()
            msg['From'] = f"Riaz Khan <{self.sender}>"
            msg['To'] = self.receiver
            msg['Subject'] = self.subject
            #add body
            msg.attach(MIMEText(self.body, 'html'))

            # Attach resume
            filename = "CV__Riaz_Khan.pdf"
            with open(filename, "rb") as attachment:
                part = MIMEBase("application", "octet-stream")
                part.set_payload(attachment.read())

            encoders.encode_base64(part)
            part.add_header("Content-Disposition", f"attachment; filename={filename}")
            msg.attach(part)



            # Create server
            server = smtplib.SMTP('smtp.gmail.com', 587)
            server.starttls()

            # Login
            load_dotenv()
            app_pass = os.getenv("app_pass")
            server.login(self.sender, app_pass)




            # Send email
            server.send_message(msg)
            server.quit()
            print("Email sent successfully!")
        except Exception as e:
             print(f"Error: {e}")



        
        




# def send_email(sender_email, app_password, receiver_email, subject, body_html):
#     try:
#         # Set up the MIME
#         msg = MIMEMultipart()
#         msg['From'] = sender_email
#         msg['To'] = receiver_email
#         msg['Subject'] = subject

#         # Add body
#         msg.attach(MIMEText(body_html, 'html'))

#         # Create server
#         server = smtplib.SMTP('smtp.gmail.com', 587)
#         server.starttls()

#         # Login
#         server.login(sender_email, app_password)

#         # Send email
#         server.send_message(msg)
#         server.quit()
#         print("Email sent successfully!")

#     except Exception as e:
#         print(f"Error: {e}")

# # Example usage
# if __name__ == "__main__":
#     sender = "riaz222666@gmail.com"
#     load_dotenv()
#     app_pass = os.getenv("app_pass")  # Not your Gmail password
#     receiver = "riaz.khan.ruet@gmail.com"

#     #
    
#     # email_body = "Hi Riaz Khan!"
#     # Professional email content
#     email_body = """
#     <html>
#         <body>
#             <p>Dear Professor,</p>
            
#             <p>I hope this email finds you well.</p>
            
#             <p>
#                 I am writing to express my interest in your research on 
#                 <b>Control Systems and AI</b>. I have a background in 
#                 <i>Machine Learning</i> and would love to collaborate 
#                 or learn more about your work.
#             </p>
            
#             <p>
#                 Looking forward to your response.<br>
#                 Best regards,<br>
#                 <b>Riaz Khan</b><br>
#                 Mechatronics Engineer
#             </p>
#         </body>
#     </html>
#     """

#     recievers=['riaz.khan.ruet@gmail.com','zairkhannnn1998@gmail.com','riaz.khan.ruet.16@gmail.com','muktadir.bccb@gmail.com','sabit222999@gmail.com'  ]

#     # send_email(sender, app_pass, receiver, "Prospective ", email_body)

#     for r in recievers:
#         send_email(sender, app_pass, r, "Prospective 000", email_body)

