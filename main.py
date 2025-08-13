import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import os
from dotenv import  load_dotenv


from Components.EmailSender import EmailSender

from EmailTemplates.Default import defaultEmail




# Run your app
from App.app import ProfessorForm

if __name__ == "__main__":
    app = ProfessorForm()
    app.run()
    
    
