import gspread
from google.oauth2.service_account import Credentials
import os
import time
import colorama
"""
To import the entire gspread library so we access any class
function or method within it.
Import credentials class which is part of the service account
function from the google oauth library.
"""
#  List the API that the program should access in order to run
SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive"
    ]

CREDS = Credentials.from_service_account_file('creds.json')
SCOPED_CREDS = CREDS.with_scopes(SCOPE)
GSPREAD_CLIENT = gspread.authorize(SCOPED_CREDS)
# To access 'tourism_survey' sheet, name must be same as sheet.
SHEET = GSPREAD_CLIENT.open('tourism_survey')

# To access the data in the worksheet
# Parameter name must be same as the sheet name
text = SHEET.worksheet('text')
data = text.get_all_values()

q_and_a = SHEET.worksheet('q_and_a')
data_qa = q_and_a.get_all_values()

survey_answer = SHEET.worksheet('survey_answer')
data_answer = survey_answer.get_all_values()
# print(data_answer)
# This is to validated the worksheet retrieved successfully


def clear_scr():
    """
    This function is for clear screen for different os
    Call the clear_scr() to clear the terminal
    """
    os.system("cls if os.name == 'nt' else 'clear'")


# Global variable for result
user_choice = []


# def age_group(1):
# def gender(2):
# def continents(3):
# def destination(4):
# def planning(5):
# def motivations(6):
# def decision(7):
# def accommodation(8):
# def spending(9):
# def share_experiences(10):
# def return_holiday(11):
