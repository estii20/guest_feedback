# API to add and view guest data in guest feedback spreadsheet
# For authorisation for app access to gspread API
import gspread
from google.oauth2.service_account import Credentials
# For matching the email format with the input a RegEx pattern
import re
# For exit from the main menu
import sys
# For creating DataFrames for column average calculations
import pandas as pd
import numpy as np


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

        name_str = input("Enter guest name: \n")
        print(f"The name provided is {name_str}")

        name_input = name_str.strip()

        if validate_name(name_input):
            print("Name is valid!")
            break

    return name_input


def validate_name(input):
    """
    Raises action from user if name not entered
    is not atleast 2 characters
    Args:
        input: str - the name is input by the admin

    Returns:
        bool: True if the input 2 characters
                False otherwise
    """
    try:
        if len(input) < 2:
            raise ValueError(
                "Please enter a name that is at least 2 characters long."
                )
    except ValueError as e:
        print(f"Invalid name: {e}, please try again.\n")
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

    Args:
        input: str - the email is input by the admin

    Returns:
        bool: True if the value matches the email format
                False otherwise
    """
    try:
        if not re.match(r"[^@]+@[^@]+\.[^@]+", input):
            raise ValueError(
                "Enter valid email, please try again\n"
                    )
    except ValueError as e:
        print(f"Invalid email: {e}, please try again.\n")
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

        if validate_score(front_desk_data):
            print("Score is valid!")
            break

    return front_desk_data


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

        if validate_score(restaurant_data):
            print("Score is valid!")
            break

    return restaurant_data


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

        if validate_score(spa_data):
            print("Score is valid!")
            break

    return spa_data


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

        if validate_score(hotel_room_data):
            print("Score is valid!")
            break

    return hotel_room_data


def validate_score(value):
    """
    Raises action from user if score not entered
    in correct format.

    Args:
        values: str - the value 1 - 5 is input by the admin

    Returns:
        bool: True if the value matches the 1,2,3,4,5
                False otherwise
    """
    try:
        if value not in ["1", "2", "3", "4", "5"]:
            raise ValueError(
                print("A value between 1 - 5 required, try again please\n")
            )
    except ValueError as e:
        print(f"Invalid score: {e}, please try again.\n")
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


def validate_special_offers(input):
    """
    Raises action from user if data not entered
    in correct format either yes or no.

    Args:
        input: str - the data yes or no is input by the admin

    Returns:
        bool: True if the value matches the input
                False otherwise
    """
    try:
        if input.lower() not in ["yes", "no"]:
            raise ValueError(
                    print("yes or no required, try again please\n")
                )
    except ValueError as e:
        print(f"Invalid input: {e}, please try again.\n")
        return False

    return True


def update_feedback_worksheet(data):
    """
    Given a list of cell values, add a row to the Google sheet with the data.

    Args:
        data: A list of values for each cell in the row
        for name, email, front desk, restaurant, spa, room and special offers
    """
    print("Updating guest feedback worksheet...\n")
    feedback_worksheet = SHEET.worksheet("feedback")
    feedback_worksheet.append_row(data)
    print("Data updated successfully.\n")

    name = get_name_input()

    email = get_email_data()

    front_desk = get_front_desk_score()

    restaurant = get_restaurant_score()

    spa = get_spa_score()

    hotel_room = get_hotel_room_score()

    special_offers = get_special_offers()

    data = (
        [name, email, front_desk, restaurant, spa, hotel_room, special_offers]
        )


def enter_responses():
    """
    Choice 1 to enter data to the spreadsheet
    Runs the functions from choice 1
    get name, get email, get scores, special offers
    and the updates sheet
    """
    print("Choice 1: Enter guest responses \n")

    name = get_name_input()

    email = get_email_data()

    front_desk = get_front_desk_score()

    restaurant = get_restaurant_score()

    spa = get_spa_score()

    hotel_room = get_hotel_room_score()

    special_offers = get_special_offers()

    data = (
        [name, email, front_desk, restaurant, spa, hotel_room, special_offers]
        )

    update_feedback_worksheet(data)


def calculate_front_desk_mean_score():
    """
    Calculate the mean score for the front desk
    using pandas DataFrames
    """
    print("Calculating front desk mean score...\n")
    print("Mean front desk score is: \n")

    front_desk_column = SHEET.worksheet("feedback").col_values(3)

    front_desk_df = pd.DataFrame(
        {"front_desk": front_desk_column[1:]}
    )

    front_desk_mean_score = front_desk_df["front_desk"].mean(
        axis=0, skipna=False,
        )

    print(front_desk_mean_score)


def calculate_restaurant_mean_score():
    """
    Calculate the mean score for the restaurant
    usinf pandas DataFrames
    """
    print("Calculating restaurant mean score...\n")
    print("Mean restaurant score is: \n")

    restaurant_column = SHEET.worksheet("feedback").col_values(4)

    restaurant_df = pd.DataFrame(
        {"restaurant": restaurant_column[1:]}
    )

    restaurant_mean_score = restaurant_df["restaurant"].mean(
        axis=0, skipna=False
        )

    print(restaurant_mean_score)


def calculate_spa_mean_score():
    """
    Calculate the mean score for the spa
    using pandas DataFrames
    """
    print("Calculating spa mean score...\n")
    print("Mean spa score is: \n")

    spa_column = SHEET.worksheet("feedback").col_values(5)

    spa_df = pd.DataFrame(
        {"spa": spa_column[1:]}
    )

    spa_mean_score = spa_df["spa"].mean(
        axis=0, skipna=False
        )

    print(spa_mean_score)


def calculate_hotel_room_mean_score():
    """
    Calculate the mean score for the hotel room
    using pandas DataFrames
    """
    print("Calculating hotel room mean score...\n")

    hotel_room_column = SHEET.worksheet("feedback").col_values(6)

    hotel_room_df = pd.DataFrame(
        {"hotel_room": hotel_room_column[1:]}
    )

    hotel_room_mean_score = hotel_room_df["hotel_room"].mean(
        axis=0, skipna=False
        )

    print(hotel_room_mean_score)


def get_guest_feedback():
    """
    Get the guest information for special offers
    if guests answered yes to receive them
    """
    print("Getting info from guest feedback...\n")

    guest_feedback = SHEET.worksheet("feedback").get_all_values()

    guest_feedback_df = pd.DataFrame(guest_feedback[1:])

    print(guest_feedback_df)


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
            print("Code is valid!\n")
            break

    calculate_front_desk_mean_score()

    calculate_restaurant_mean_score()

    calculate_spa_mean_score()

    calculate_hotel_room_mean_score()

    get_guest_feedback()


def validate_view_responses(input):
    """
    Validates access code from the user

    Args:
        values: str - the code is input by the admin

    Returns:
        bool: True if the value matches the code
                False otherwise
    """

    try:
        if input != "5794":
            raise ValueError(
                print("A valid access code is required, try again please")
            )
    except ValueError:
        print("Invalid data, please try again.\n")
        return False

    return True


def exit_feedback_form():
    print("Exiting the Guest Feedback Form...\n")
    sys.exit('Bye')


def main():
    """
    Program starts, main menu is displayed.
    Main menu has two options.
    1. Enter responses to get and validate data from the admin
    such as name, email and score for each (front desk, restaurant, spa, room)
    the rating for each on scale 1-5
    (1 = Excellent, 2 = Good 3 = Satisfactory 5 = Poor)
    2. View responses
    The admin enters access code (hardcoded password)
    then the admin can view data average score for each e.g. front desk.
    Also the admin can get guest feedback information as a pandas DataFrame.
    """
    print('Welcome to the Guest Feedback Form.\n')

    print("What would you like to do?\n")
    print("1. Enter responses\n")
    print("2. View responses\n")
    print("3. Exit the Guest Feedback Form\n")

    while True:
        # 1. Ask admin for input.
        menu_choice = input("Enter choice\n").strip()

        # 2. Checks if the input violates any of the criteria.
        if menu_choice not in ["1", "2", "3"]:
            print("Please enter one of the choices above.\n")
            continue
        # Exit the loop and uses the input
        break

    # after validation, uses the input to either enter
    # or view responses or exit the terminal.
    if menu_choice == "1":
        enter_responses()
    elif menu_choice == "2":
        view_responses()
    else:
        menu_choice == "3"
        exit_feedback_form()


if __name__ == "__main__":
    main()
