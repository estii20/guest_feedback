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
    print("Please enter guest name.")
    print("Example: Joe Blogs\n")

    data_str = input("Enter guest name here: ")
    print(f"The data provided is {data_str}")

get_name_data()


