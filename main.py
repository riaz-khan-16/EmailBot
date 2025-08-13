import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import os
from dotenv import  load_dotenv


from Components.multipleEmailSender import EmailSender

from EmailTemplates.Default import defaultEmail

body=defaultEmail("Dr. Duan", "Machine Learning").writeEmail()
email=EmailSender("riaz222666@gmail.com", "riaz.khan.ruet@gmail.com",  "Prospective PhD Student", body)
# email.sendEmail()



# Run your app
from App.app import ProfessorForm

if __name__ == "__main__":
    app = ProfessorForm()
    app.run()
    
    
