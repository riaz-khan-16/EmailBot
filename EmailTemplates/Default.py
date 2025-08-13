
class defaultEmail:
    def __init__(self, professor_name, research_interests):
        self.professor_name=professor_name
        self.research_interests=research_interests

    
    def writeEmail(self):
        email_body = f"""
        <html>
            <body>
                <p>Dear {self.professor_name},</p>
                
                <p>I hope this email finds you well.</p>
                
                <p>
                    I am writing to express my interest in your research on 
                    <b>{self.research_interests}</b>. I have a background in 
                    <i>Machine Learning</i> and would love to collaborate 
                    or learn more about your work.
                </p>
                
                <p>
                    Looking forward to your response.<br>
                    Best regards,<br>
                    <b>Riaz Khan</b><br>
                </p>
            </body>
        </html>
        """
        return email_body
    
