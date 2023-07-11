# API to add and view guest data in guest feedback spreadsheet
# For authorisation for app access to gspread API
import gspread
from google.oauth2.service_account import Credentials
# For access to the dataframes function
import pandas as pd
# For access to mean function
import numpy as np
# For matching the email format with the input a RegEx pattern
import re

SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive"
    ]

CREDS = Credentials.from_service_account_file('creds.json')
SCOPED_CREDS = CREDS.with_scopes(SCOPE)
GSPREAD_CLIENT = gspread.authorize(SCOPED_CREDS)
SHEET = GSPREAD_CLIENT.open('guest_feedback')


def get_name_input():
    """
    Get guest name input from the user until
    name data entered correctly.
    """
    while True:
        print("Please enter guest name.\n")
        print("Example: Joe Blogs\n")

        name_str = input("Enter guest first name, space, last name here: \n")
        print(f"The name provided is {name_str}")

        name_input = name_str.strip()

        if validate_name(name_input):
            print("Name is valid!")
            break

    return name_input


def validate_name(input):
    """
    Raises action from user if name not entered
    is not atleast 2 characters, and is not letters
    it raises a ValueError
    """
    try:
        if len(input) < 2:
            raise ValueError(
                "Please enter a name that is at least 2 characters long."
                )

        else:
            if not input.isalpha():
                raise ValueError(
                    "Please enter a name only containing letters"
                    )

    except ValueError as e:
        print(f'Invalid name: {e}, please try again.\n')
        return False
    return True


def get_email_data():
    """
    Get guest email input from the user until
    name data entered correctly.
    """
    while True:
        print("Please enter guest email.\n")
        print("Example: joe.blogs@gmail.com\n")

        data_str = input("Enter guest email here: \n")

        email_data = data_str.strip()

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
        if not re.match(r"[^@]+@[^@]+\.[^@]+", input):
            raise ValueError(
                "Enter valid email please try again\n"
                    )
    except ValueError as e:
        print(f'Invalid data: {e}, please try again.\n')
        return False
    return True


def get_front_desk_score():
    """
    Get guest front desk score input from the user until
    score data entered correctly.
    """
    while True:
        print("Please enter score 1=Excellent, 2=Good 3=Satisfactory 4=Poor\n")
        print("Example: 1\n")

        data_str = input("Enter guest front desk score here: \n")

        front_desk_data = data_str.strip()

        if validate_front_desk_score(front_desk_data):
            print("Score is valid!")
            break

    return front_desk_data


def validate_front_desk_score(values):
    """
    Raises action from user if score not entered
    in correct format.
    """
    try:
        [int(value) for value in values]
        if not ["1", "2", "3", "4", "5"]:
            raise ValueError(
                print("A value between 1 - 5 required, try again please")
            )
    except ValueError as e:
        print(f"Invalid data: {e}, please try again.\n")
        return False

    return True


def get_restaurant_score():
    """
    Get guest restaurant score input from the user until
    score data entered correctly.
    """
    while True:
        print("Please enter score 1=Excellent, 2=Good 3=Satisfactory 4=Poor\n")
        print("Example: 1\n")

        data_str = input("Enter guest restaurant score here: \n")

        restaurant_data = data_str.strip()

        if validate_restaurant_score(restaurant_data):
            print("Score is valid!")
            break

    return restaurant_data


def validate_restaurant_score(values):
    """
    Raises action from user if score not entered
    in correct format.
    """
    try:
        [int(value) for value in values]
        if not ["1", "2", "3", "4", "5"]:
            raise ValueError(
                print("A value between 1 - 5 required, try again please")
            )
    except ValueError as e:
        print(f"Invalid data: {e}, please try again.\n")
        return False

    return True


def get_spa_score():
    """
    Get guest spa score input from the user until
    score data entered correctly.
    """
    while True:
        print("Please enter score 1=Excellent, 2=Good 3=Satisfactory 4=Poor\n")
        print("Example: 1\n")

        data_str = input("Enter guest spa score here: \n")

        spa_data = data_str.strip()

        if validate_spa_score(spa_data):
            print("Score is valid!")
            break

    return spa_data


def validate_spa_score(values):
    """
    Raises action from user if score not entered
    in correct format.
    """
    try:
        [int(value) for value in values]
        if not ["1", "2", "3", "4", "5"]:
            raise ValueError(
                print("A value between 1 - 5 required, try again please")
            )
    except ValueError as e:
        print(f"Invalid data: {e}, please try again.\n")
        return False

    return True


def get_hotel_room_score():
    """
    Get guest hotel room score input from the user until
    score data entered correctly.
    """
    while True:
        print("Please enter score 1=Excellent, 2=Good 3=Satisfactory 4=Poor\n")
        print("Example: 1\n")

        data_str = input("Enter guest hotel room score here: \n")

        hotel_room_data = data_str.strip()

        if validate_hotel_room_score(hotel_room_data):
            print("Score is valid!")
            break

    return hotel_room_data


def validate_hotel_room_score(values):
    """
    Raises action from user if score not entered
    in correct format.
    """
    try:
        [int(value) for value in values]
        if not ["1", "2", "3", "4", "5"]:
            raise ValueError(
                print("A value between 1 - 5 required, try again please")
            )
    except ValueError as e:
        print(f"Invalid data: {e}, please try again.\n")
        return False

    return True


def get_special_offers():
    """
    Get guest input from the user if guests would like special offers
    checks yes or no is entered correctly.
    """
    while True:
        print("Please enter yes or no if you would like special offers\n")

        data_str = input("Enter guest special offer option here: \n")

        special_offers_data = data_str.strip()

        if validate_special_offers(special_offers_data):
            print("It is valid!")
            break

    return special_offers_data


def validate_special_offers(user_input):
    """
    Raises action from user if data not entered
    in correct format either yes or no.
    """
    user_input = input("Answer: \n")
    yes_choices = ['yes', 'y']
    no_choices = ['no', 'n']
    try:
        if user_input.lower() in yes_choices:
            print("User typed yes \n")
        else:
            user_input.lower() in no_choices
            print("User typed no\n")
    except ValueError:
        print("Format incorrect, please try again with yes or no\n")
        return False

    return True


def enter_responses():
    """
    Choice 1 to enter data to the spreadsheet
    """
    print("Choice 1: Enter guest responses \n")

    name = get_name_input()

    email = get_email_data()

    front_desk = get_front_desk_score()
    front_desk = [int(num) for num in front_desk]

    restaurant = get_restaurant_score()
    restaurant = [int(num) for num in restaurant]

    spa = get_spa_score()
    spa = [int(num) for num in spa]

    hotel_room = get_hotel_room_score()
    hotel_room = [int(num) for num in hotel_room]

    special_offers = get_special_offers()

    row_data = (
        [name, email, front_desk, restaurant, spa, hotel_room, special_offers]
    )
    feedback_worksheet = SHEET.worksheet("feedback")
    update_feedback_worksheet(row_data, feedback_worksheet)


def update_feedback_worksheet(row_data, feedback_worksheet):
    """
    Given a list of cell values, add a row to the Google sheet with the data.

    Args:
        row_data: List if str - A list of values for each cell in the row
        for name, email, front desk, restaurant, spa, room and special offers
    """
    print("Updating guest feedback worksheet...\n")

    name = get_name_input()

    email = get_email_data()

    front_desk = get_front_desk_score()
    front_desk = [int(num) for num in front_desk]

    restaurant = get_restaurant_score()
    restaurant = [int(num) for num in restaurant]

    spa = get_spa_score()
    spa = [int(num) for num in spa]

    hotel_room = get_hotel_room_score()
    hotel_room = [int(num) for num in hotel_room]

    special_offers = get_special_offers()

    row_data = (
        [name, email, front_desk, restaurant, spa, hotel_room, special_offers]
    )
    feedback_worksheet = SHEET.worksheet("feedback")
    feedback_worksheet.append_row(row_data, "feedback")
    print("Data updated successfully.\n")

    enter_responses()


def view_responses():
    """
    Get access code from the user
    """
    while True:
        print("Please enter an access code: \n")
        print("Example: **** \n")

        data_str = input("Access code: \n")

        view_responses = data_str.strip()

        if validate_view_responses(view_responses):
            print("Code is valid!")
            break


def validate_view_responses(values):
    """
    Validates access code from the user
    """
    access_code = "5", "7", "9", "4"

    try:
        [int(value) for value in values]
        if not access_code:
            raise ValueError(
                print("A valid access code is required, try again please")
            )
    except ValueError as e:
        print(f"Invalid data: {e}, please try again.\n")
        return False

    return True


def main():
    """
    Program starts, main menu is displayed.
    Main menu has two options.
    1. Enter responses
        - get and validate data from user
        -- name, email, score for each (front desk, restaurant, room, spa)
        --- rating for each on scale 1-5
    2. View responses
        - admin enters access code (hardcoded password)
        -- later improvement: maintain a list of access codes
        --- admin views data average score for each e.g. front desk
        ---- admin gets guests emails who wish to receive special offers
        """
    print('Welcome to the Guest Feedback Form.\n')

    print("What would you like to do?\n")
    print("1. Enter responses\n")
    print("2. View responses\n")

    while True:
        # 1. Ask for input.
        menu_choice = input("Enter choice\n").strip()

        # 2. Check if the input violates any of your criteria.
        if menu_choice not in ["1", "2"]:
            print("Please enter one of the choices above.\n")
            continue
        # Eventually, exit the loop and use the input
        break

    # after validation, use the input:
    if menu_choice == "1":
        enter_responses()

    else:
        view_responses()
