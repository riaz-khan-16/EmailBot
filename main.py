import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import os
from dotenv import  load_dotenv

from Components.EmailSender import EmailSender
from EmailTemplates.Default import defaultEmail




# Run your app
from App.app import ProfessorForm
from registration import Registration
from UserProfile.User import isRegistered


if __name__ == "__main__":
    if isRegistered:
        app = ProfessorForm()
        app.run()
        
    else:
        obj=Registration()
        obj.run()
        

    
    
