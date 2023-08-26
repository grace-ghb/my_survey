import gspread
from google.oauth2.service_account import Credentials
import os
import time
import colorama
from colorama import Fore, Back, Style
colorama.init(autoreset=True)   # To initialize the colorama library
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


RED = Fore.RED      # Red color text
YELLOW = Fore.YELLOW    # Yellow color text
BLUE = Fore.BLUE    # Blue color text
RESET = Style.RESET_ALL     # Resets all the color to default
BRIGHT = Style.BRIGHT       # Text bright


def clear_scr():
    """
    This function is for clear screen for different os
    Call the clear_scr() to clear the terminal
    """
    os.system('cls' if os.name == 'nt' else 'clear')


# Global variable for result
user_choice = []


def main_page():
    """
    This function allow user to choose whether to take the survey
    """
    select = 0
    while select != 1 and select != 2:
        try:
            print('Select an option: ')
            print('1. Take the survey')
            print('2. No and Exit')
            print()
            select = int(input('Please enter your choice: '))

            if select != 1 and select != 2:
                print('Invalid Number!')
        except ValueError:
            print('Please enter a valid number 1 or 2')
    if select == 1:
        # display_questions_and_options(column=1)
        age_group()
    elif select == 2:
        exit()


def welcome():
    """
    Welcome message before start the survey.
    """
    welcome_text = SHEET.worksheet('text').col_values(1)
    instruction = SHEET.worksheet('text').col_values(2)
    print()
    print(welcome_text[1])
    print()
    print()
    print(Fore.CYAN + 'System loading...' + RESET)
    time.sleep(3)
    print()
    clear_scr()
    print()
    print(RED + instruction[1].upper() + RESET)
    print()
    print(instruction[2].upper())
    print()
    input(Fore.CYAN + 'Press enter to continue...' + RESET)
    print()
    # clear_scr()
    main_page()


def end():
    """
    Ask user if they want to exit or not.
    End of survey.
    """
    select = 0
    while select != 1 and select != 2:
        try:
            print('Are you sure you want to exit?\n')
            print('1. Yes')
            print('2. No')
            select = int(input('Enter your choice: '))
            if select != 1 and select != 2:
                print('Invalid number! Please enter 1 or 2')
        except ValueError:
            print('Please enter a valid number.')

    if select == 1:
        """
        Retrieve message from sheet 'text' the third column
        """ 
        goodbye_msg = SHEET.worksheet('text').col_values(3)
        print(BLUE + goodbye_msg[1].upper() + RESET)
        time.sleep(3)
        exit()
    elif select == 2:
        main_page()


welcome()