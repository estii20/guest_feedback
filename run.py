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
    Get guest name input from the user until
    name data entered correctly.
    """
    while True:
        print("Please enter guest name.\n")
        print("Example: Joe Blogs\n")

        data_str = input("Enter guest first name, space, last name here: \n")

        name_data = data_str.split(" ")

        if validate_name(name_data):
            print("Name is valid!")
            break

    return name_data


def validate_name(input):
    """
    Raises action from user if name not entered
    in correct format.
    """
    try:
        if input == validate_name:
            print("Thanks\n")
    except ValueError:
        print("Enter first name, space, last name, please try again\n")
        return False

    return True


def update_name_guest_feedback_worksheet(name):
    """
    Update guest feedback worksheet,
    add new row with the name data provided
    """
    print("Updating name of guest feedback worksheet...\n")
    feedback_worksheet = SHEET.worksheet("feedback")
    feedback_worksheet.append_row(name)
    print("Name data updated successfully.\n")


name = get_name_data()
update_name_guest_feedback_worksheet(name)
