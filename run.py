import gspread
from google.oauth2.service_account import Credentials

SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive"
    ]

CREDS = Credentials.from_service_account_file('creds.json')
SCOPED_CREDS = CREDS.with_scopes(SCOPE)
GSPREAD_CLIENT = gspread.authorize(SCOPED_CREDS)
SHEET = GSPREAD_CLIENT.open('guest_feedback')

def get_name_data():
    """
    Get guest name input from the user.
    """
    print("Please enter guest name.\n")
    print("Example: Joe Blogs\n")

    data_str = input("Enter guest first name, space, last name here: \n")
    
    name_data = data_str.split(" ")
    validate_name(name_data)

def validate_name(input):
    """
    Raises action from user if strings not entered first name, space, last name.
    """
    try:
        if data_str == validate_name:
            print("Thanks " + name_data())
    except: 
        print("Enter first name, space, last name, please try again\n")

get_name_data()