#step 1: create main window
import tkinter as tk
import os
from App.app import ProfessorForm
from UserProfile.User import isRegistered

class Registration:
    def __init__(self):
        self.root = tk.Tk()
        self.root.geometry("800x800")
        self.root.title("My Application")

        #fields
        self.name=None
        self.email=None
        self.target_semester=None
        self.major=None
        self.university=None
        self.graduation_year=None
        self.experiences=None
        self.email_pass_key=None

        


    def createFrame(self):
    
        self.registration_frame = tk.Frame(self.root)
        return self.registration_frame

    def buildRegiUI(self, frame):
        label = tk.Label(frame, text="Registration Form")
        label.pack(pady=20)

        tk.Label(frame, text="Name:").pack()
        self.name_entry= tk.Entry(frame)
        self.name_entry.pack()

        tk.Label(frame, text="Email:").pack()
        self.email_entry= tk.Entry(frame)
        self.email_entry.pack()

        tk.Label(frame, text="Target Semester:").pack()
        self.target_semester_entry = tk.Entry(frame)
        self.target_semester_entry.pack()

        tk.Label(frame, text="Your Major:").pack()
        self.major_entry = tk.Entry(frame)
        self.major_entry.pack()

        tk.Label(frame, text="University:").pack()
        self.university_entry = tk.Entry(frame)
        self.university_entry.pack()

        tk.Label(frame, text="Your Passing year:").pack()
        self.graduation_year_entry = tk.Entry(frame)
        self.graduation_year_entry.pack()


        tk.Label(frame, text="List of Experiences you have:").pack()
        self.experiences_entry = tk.Entry(frame)
        self.experiences_entry.pack()

        tk.Label(frame, text="Your Email_pass_key:").pack()
        self.email_pass_key_entry = tk.Entry(frame)
        self.email_pass_key_entry.pack()


        submit_btn = tk.Button(frame, text="Submit", command=self.save_registration)
        submit_btn.pack(pady=10)


    def save_registration(self):
            
        
            with open("status.txt", "w") as f:
                f.write("registered")

            self.name=self.name_entry.get()
            self.email=self.email_entry.get()
            self.target_semester=self.target_semester_entry.get()
            self.major=self.major_entry.get()
            self.university=self.university_entry.get()
            self.graduation_year=self.graduation_year_entry.get()
            self.experiences=self.experiences_entry.get()
            self.email_pass_key=self.email_pass_key_entry.get()

            

            
        

            # dictionary
            profile= {
                "name": self.name,
                "email": self.email,
                "target_semester":self.target_semester,
                "major":self.major,
                "university":self.university,
                "graduation_year":self.graduation_year,
                "experienes":[self.experiences],
                "email_pass_key":self.email_pass_key
            }

            # create a python file and write dictionary into it
            with open("UserProfile/User.py", "w") as f:
                f.write(f"isRegistered=True")
                f.write(f"\n")
                f.write(f"profile = {profile}")

            self.root.destroy()
            self.gotoMain()
            
            
            # registration_frame.pack_forget()  # hide registration frame
            # show_main_page()  # show main frame

    def show(self, frame):
        frame.pack(fill="both", expand=True)

    def run(self):
        frame=self.createFrame()
        self.buildRegiUI(frame)
        self.show(frame)
        self.root.mainloop()

    def gotoMain(self):

        app=ProfessorForm()
        app.run()

        

# obj=Registration()
# frame=obj.createFrame()
# obj.buildRegiUI(frame)
# obj.show(frame)
# obj.run()














# ##Step 6 – Write helper functions to show each page

# def show_registration_page():
#     registration_frame.pack(fill="both", expand=True)

# def show_main_page():
#     main_frame.pack(fill="both", expand=True)




# Step 5 – Write a function that is called when the user finishes registration When the user presses “Submit”, we want to do two things:

        # Save a flag (so we remember the user already registered)

        # Show the main page`



# def save_registration():
#     with open("status.txt", "w") as f:
#         f.write("registered")
    
#     registration_frame.pack_forget()  # hide registration frame
#     show_main_page()  # show main frame
    






# #Step 2 – Create two different Frames

# registration_frame = tk.Frame(root)
# main_frame = tk.Frame(root)

# # Step 3 – Build the Registration Form UI

# label = tk.Label(registration_frame, text="Registration Form")
# label.pack(pady=10)

# tk.Label(registration_frame, text="Name:").pack()
# name_entry = tk.Entry(registration_frame)
# name_entry.pack()

# tk.Label(registration_frame, text="Email:").pack()
# email_entry = tk.Entry(registration_frame)
# email_entry.pack()

# submit_btn = tk.Button(registration_frame, text="Submit", command=save_registration)
# submit_btn.pack(pady=10)


# # Step 4 – Build the Main Page UI

# welcome_label = tk.Label(main_frame, text="Welcome to the Main Page!")
# welcome_label.pack(pady=20)




# #step 7: When the application starts, check if the user is already registered

# # If the file status.txt exists => go directly to Main Page

# # If the file does not exist => show the Registration Page



# if os.path.exists("status.txt"):
#     show_main_page()
# else:
#     show_registration_page()

# root.mainloop()
