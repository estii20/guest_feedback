# API to add and view guest data in guest feedback spreadsheet
# For authorisation for app access to gspread API
import gspread
from google.oauth2.service_account import Credentials
# For access to the dataframes function
# import pandas as pd
# For access to mean function
# import numpy as np
# To print to the terminal
# from pprint import pprint
import getpass
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


def main_menu():
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
        ---- admin gets guests who wish to receive special offers
        """
    print("Welcome")
    print("What would you like to do?\n")
    print("1. Enter responses \n")
    print("2. View responses \n")

    while True:
        # 1. Ask for input from the admin
        menu_choice = input("Enter response: \n").strip()
        view_responses = input("Viewing responses...\n").strip()
        # 2. Check if the input violates the criteria 1 or 2
        if menu_choice not in ["1", "2"]:
            print("Please enter one of the choices above.")
            continue
        else:
            break

        """
        # after validation, user can input choice
        """
        if menu_choice == "1":
            get_name_data()
        else:
            view_responses()


def get_name_data():
    """
    Get guest name input from the user until
    name data entered correctly.
    """
    while True:
        print("Please enter guest name.\n")
        print("Example: Joe Blogs\n")

        data_str = input("Enter guest first name, space, last name here: \n")

        name_data = data_str.strip()

        if validate_name(name_data):
            print("Name is valid!")
            break

    return name_data


def validate_name(input):
    # Raises action from user if name not entered
    # in correct format.
    try:
        if len(input) < 2:
            print("Please enter a name that is at least 2 characters long.")
            return False

        else:
            if not input.isalpha():
                print("Please enter a name only containing letters.")
                return False

    except ValueError as e:
        print(f'Invalid data: {e}, please try again.\n')
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
        if not re.match(r"[^@]+@[^@]+\.[^@]+", email):
            raise ValueError(
                "Enter valid email please try again\n"
                    )
    except ValueError as e:
        print(f'Invalid data: {e}, please try again.\n')
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
        if not range(0, 6):
            raise ValueError(
                print("A value between 1 - 5 required, try again please")
            )
    except ValueError as e:
        print(f"Invalid data: {e}, please try again.\n")
        return False

    return True


def update_front_desk_score_guest_feedback_worksheet(front_desk):
    """
    Update guest feedback worksheet,
    add new row with the front desk score provided
    """
    print("Updating score of front desk of guest feedback worksheet...\n")
    feedback_worksheet = SHEET.worksheet("feedback")
    feedback_worksheet.append_row(front_desk)
    print("Front desk score updated successfully.\n")


front_desk = get_front_desk_score()
update_front_desk_score_guest_feedback_worksheet(front_desk)


def get_restaurant_score():
    """
    Get guest restaurant score input from the user until
    score data entered correctly.
    """
    while True:
        print("Please enter score 1=Excellent, 2=Good 3=Satisfactory 4=Poor\n")
        print("Example: 1\n")

        data_str = input("Enter guest restaurant score here: \n")

        restaurant_data = data_str.split(" ")

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
        if not range(0, 6):
            raise ValueError(
                print("A value between 1 - 5 required, try again please")
            )
    except ValueError as e:
        print(f"Invalid data: {e}, please try again.\n")
        return False

    return True


def update_restaurant_score_guest_feedback_worksheet(restaurant):
    """
    Update guest feedback worksheet,
    add new row with the restaurant score provided
    """
    print("Updating score of restaurant of guest feedback worksheet...\n")
    feedback_worksheet = SHEET.worksheet("feedback")
    feedback_worksheet.append_row(restaurant)
    print("Restaurant score updated successfully.\n")


restaurant = get_restaurant_score()
update_restaurant_score_guest_feedback_worksheet(restaurant)


def get_spa_score():
    """
    Get guest spa score input from the user until
    score data entered correctly.
    """
    while True:
        print("Please enter score 1=Excellent, 2=Good 3=Satisfactory 4=Poor\n")
        print("Example: 1\n")

        data_str = input("Enter guest spa score here: \n")

        spa_data = data_str.split(" ")

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
        if not range(0, 6):
            raise ValueError(
                print("A value between 1 - 5 required, try again please")
            )
    except ValueError as e:
        print(f"Invalid data: {e}, please try again.\n")
        return False

    return True


def update_spa_score_guest_feedback_worksheet(spa):
    """
    Update guest feedback worksheet,
    add new row with the spa score provided
    """
    print("Updating score of spa of guest feedback worksheet...\n")
    feedback_worksheet = SHEET.worksheet("feedback")
    feedback_worksheet.append_row(spa)
    print("Spa score updated successfully.\n")


spa = get_spa_score()
update_spa_score_guest_feedback_worksheet(spa)


def get_hotel_room_score():
    """
    Get guest hotel room score input from the user until
    score data entered correctly.
    """
    while True:
        print("Please enter score 1=Excellent, 2=Good 3=Satisfactory 4=Poor\n")
        print("Example: 1\n")

        data_str = input("Enter guest hotel room score here: \n")

        hotel_room_data = data_str.split(" ")

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
        if not range(0, 6):
            raise ValueError(
                print("A value between 1 - 5 required, try again please")
            )
    except ValueError as e:
        print(f"Invalid data: {e}, please try again.\n")
        return False

    return True


def update_hotel_room_score_guest_feedback_worksheet(hotel_room):
    """
    Update guest feedback worksheet,
    add new row with the restaurant score provided
    """
    print("Updating score of hotel room of guest feedback worksheet...\n")
    feedback_worksheet = SHEET.worksheet("feedback")
    feedback_worksheet.append_row(hotel_room)
    print("Hotel room score updated successfully.\n")


hotel_room = get_hotel_room_score()
update_hotel_room_score_guest_feedback_worksheet(hotel_room)


def get_special_offers():
    """
    Get guest input from the user if guests would like special offers
    checks yes or no is entered correctly.
    """
    while True:
        print("Please enter yes or no if you would like special offers\n")
        print("Example: yes\n")

        data_str = input("Enter guest special offer option here: \n")

        special_offers_data = data_str.strip()

        if validate_special_offers(special_offers_data):
            print("It is valid!")
            break

    return special_offers_data


def validate_special_offers(input):
    """
    Raises action from user if data not entered
    in correct format either yes or no.
    """
    user_input = input("Answer yes/no: ")
    yes_choices = ['yes', 'y']
    no_choices = ['no', 'n']
    try:
        if user_input.lower() in yes_choices:
            print("User typed yes \n")
        elif user_input.lower() in no_choices:
            print("User typed no\n")
        else:
            print("Type yes or no")
    except ValueError:
        print("Format incorrect, please try again with yes or no\n")
        return False

    return True


def update_special_offers_guest_feedback_worksheet(special_offers):
    """
    Update guest feedback worksheet,
    add new row with the yes for special offer and no for no special offer
    """
    print("Updating special offer of guest feedback worksheet...\n")
    feedback_worksheet = SHEET.worksheet("feedback")
    feedback_worksheet.append_row(special_offers)
    print("Special offers updated successfully.\n")


special_offers = get_special_offers()
update_special_offers_guest_feedback_worksheet(special_offers)


def calculate_mean_score():
    """
    Calculate the mean score for each column front desk, restaurant, spa, room.
    """
    print("Calculating mean front desk score...\n")
    front_desk_column = SHEET.worksheet("guest_feedback").get_all_values()
    front_desk_mean = front_desk_column
    print("Mean average of front desk score is: " + front_desk_mean)
    restaurant_column = SHEET.worksheet("guest_feedback").get_all_values()
    restaurant_mean = restaurant_column
    print("Mean average of restaurant score is: " + restaurant_mean)
    spa_column = SHEET.worksheet("guest_feedback").get_all_values()
    spa_mean = spa_column
    print("Mean average of spa score is: " + spa_mean)
    room_column = SHEET.worksheet("guest_feedback").get_all_values()
    room_mean = room_column
    print("Mean average of spa score is: " + room_mean)


calculate_mean_score()


def main():
    print('Welcome to the Guest Feedback Form.\n')
    main_menu()
