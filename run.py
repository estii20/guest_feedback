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


def get_email_data():
    """
    Get guest email input from the user until
    name data entered correctly.
    """
    while True:
        print("Please enter guest email.\n")
        print("Example: joe.blogs@gmail.com\n")

        data_str = input("Enter guest email here: \n")

        email_data = data_str.split("@")

        if validate_email(email_data):
            print("Email is valid!")
            break

    return email_data


def validate_email(input):
    """
    Raises action from user if email not entered
    in correct format.
    """
    try:
        if input == validate_email:
            print("Thanks\n")
    except ValueError:
        print("Email format incorrect, please try again\n")
        return False

    return True


def update_email_guest_feedback_worksheet(email):
    """
    Update guest feedback worksheet,
    add new row with the email data provided
    """
    print("Updating email of guest feedback worksheet...\n")
    feedback_worksheet = SHEET.worksheet("feedback")
    feedback_worksheet.append_row(email)
    print("Email data updated successfully.\n")


email = get_email_data()
update_email_guest_feedback_worksheet(email)


def get_front_desk_score():
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
