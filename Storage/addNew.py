from openpyxl import Workbook
from openpyxl import load_workbook


class addNewData:
    def __init__(self, file_name):
        self.file_name=file_name
    
    def add_new(self, name, email, research, website):
        wb = load_workbook(self.file_name)
        ws=wb.active
        ws.append([name, email, research, website])
        wb.save(self.file_name)
        print("Data added Sueccessully!")
    