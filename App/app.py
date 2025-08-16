import tkinter as tk
from Storage.addNew import addNewData
from Storage.createFile import CrateExcel
import os
from EmailTemplates.Default import defaultEmail
from Components.EmailSender import EmailSender

class ProfessorForm:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Professor Details Form")
        self.root.geometry("500x500")
        
        
        
        #create main page
        # Name input
        tk.Label(self.root, text="Professor Name:").pack()
        self.professor_name = tk.Entry(self.root, width=50, font=("Arial", 12))
        self.professor_name.pack(pady=10, ipady=5)

        # Email ID input
        tk.Label(self.root, text="Professor Email:").pack()
        self.professor_email_id = tk.Entry(self.root, width=50, font=("Arial", 12))
        self.professor_email_id.pack(pady=10, ipady=5)

        # Research Interests (multi-line)
        tk.Label(self.root, text="Professor's Research Interests:").pack()
        self.research_interests = tk.Text(self.root, width=50, height=5, font=("Arial", 12))
        self.research_interests.pack(pady=10)

        # Website Link
        tk.Label(self.root, text="Professor's Website").pack()
        self.website = tk.Entry(self.root, width=50, font=("Arial", 12))
        self.website.pack(pady=10)

        # Submit button - keep reference as self.button
        self.button = tk.Button(self.root, text="Save Data", command=self.storeData)
        self.button.pack(pady=5)

        # Send Email
        self.button = tk.Button(self.root, text="Send Email", command=self.sendEmail)
        self.button.pack(pady=5)

        # Success message label (initially empty)
        self.success_label = tk.Label(self.root, text="", font=("Arial", 12))
        self.success_label.pack(pady=5)



    

    def storeData(self):
        name = self.professor_name.get()
        email_id = self.professor_email_id.get()
        research = self.research_interests.get("1.0", tk.END).strip()
        website = self.website.get()

        file_name = 'Storage/main.xlsx'
        if os.path.isfile(file_name):
            file = addNewData(file_name)
        else:
            CrateExcel('main').create()
            file = addNewData(file_name)

        file.add_new(name, email_id, research, website)

        print("Professor Name:", name)
        print("Professor Email:", email_id)
        print("Research Interests:", research)
        print("Website Link:", website)

        # Update button color
        self.button.config(bg="green", fg="white")

        # Show success message
        self.success_label.config(text="Submission successful!", fg="green")

    def sendEmail(self):
        # Show success message
        

        name = self.professor_name.get()
        professor_email_id = self.professor_email_id.get()
        research = self.research_interests.get("1.0", tk.END).strip()
        website = self.website.get()

        email_body=defaultEmail(name, research).writeEmail()


        email=EmailSender('riaz222666@gmail.com', professor_email_id, "Prospective Graduate Student", email_body)
        email.sendEmail()


        self.success_label.config(text="Email Sent to " +name +" successfully!", fg="green")


    def run(self):
        self.root.mainloop()
