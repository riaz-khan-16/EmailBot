from UserProfile.User import profile

profile['name']='Riaz Khan'
profile['target_semester']='Fall 2026'
profile['university']='Rajshahi University of Engineering & Technology'
profile['BSC']='Mechatronics Engineering'
profile['graduation_year']
#previous expereincs
profile['experiences']


##matched experiencc



class defaultEmail:
    def __init__(self, professor_name, research_interests):
        
        self.professor_name=professor_name.split()[-1]
        self.research_interests=research_interests
        self.reasons=self.reason()



    def findMachedExp(self):
        output=[]
        for item in [self.research_interests]:
            if item in profile['experiences']:
                output+=[item]
        if not output:
            return ''

        return ', '.join(output)
    
    def reason(self):
        print(self.research_interests)
        x=''
        if self.findMachedExp():
            x=self.findMachedExp()
        
        if x:
            return " I have visited your research website and am very enthusiastic about the work being done in + "[x]+". During my undergraduate studies, I conducted research in +"[x]+", which has given me a foundational understanding and strong interest in this area. I would be excited to contribute to your ongoing projects in this field."
        else:
            print('No matched topic found')
            return  "I have visited your research website and am very enthusiastic about the work being done in " + self.research_interests + ". During my undergraduate studies, I conducted research related to these areas, which has given me a strong foundation and keen interest in this field. I would be excited to contribute to your ongoing projects across these topics."
        




       


    
    def writeEmail(self):


        email_body = f"""
            <html>
            <head>
                <meta charset="UTF-8">
            </head>
            <body style="font-family: Arial, sans-serif; font-size: 14px; color: #000;">
                <p>Dear Dr. {self.professor_name},</p>

                <p>Greetings! I am {profile['name']} from Bangladesh, a prospective graduate student for {profile['target_semester']}. 
                I completed my B.Sc. in {profile['BSC']} in {profile['graduation_year']} from {profile['university']}, one of the leading engineering institutions in my country.</p>

                <p>{self.reasons}</p>

                <p>It would be a great opportunity if you consider me for an assistantship position in any research project that aligns with our interests and is available under your supervision. I would greatly appreciate the chance to meet with you online (e.g., via Zoom) to learn more about your research.</p>
                
                <p> Kindly evaluate my profile below: 
                <br>
                <b>CGPA: </b> 3.14/4.00 (Last term GPA: 3.82) <br>
                <b>IELTS: </b> 6.5 <br>
                <b>Publication: </b> 3 (2 Q1) <br>
                <b>Job Experience: </b> 3 years<br>
                <b>Research Experience: </b> 2 Years<br>
                </p>

                <p>I have attached my CV for a better understanding of my profile. I will be looking forward to hearing from you regarding any potential opportunities in your lab. </p>

                <p>Looking forward to your response.<br>
                Best regards,<br>
                <b>{profile['name']}</b></p>


            </body>
            </html>
            """

        return email_body
    
