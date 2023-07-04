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
    Get guest front desk score input from the user until
    score data entered correctly.
    """
    while True:
        print("Please enter score 1=Excellent, 2=Good 3=Satisfactory 4=Poor\n")
        print("Example: 1\n")

        data_str = input("Enter guest front desk score here: \n")

        front_desk_data = data_str.split(" ")

        if validate_front_desk_score(front_desk_data):
            print("Score is valid!")
            break

    return front_desk_data


def validate_front_desk_score(input):
    """
    Raises action from user if score not entered
    in correct format.
    """
    try:
        if input == validate_front_desk_score:
            print("Thanks\n")
    except ValueError:
        print("Score format incorrect, please try again\n")
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


def validate_restaurant_score(input):
    """
    Raises action from user if score not entered
    in correct format.
    """
    try:
        if input == validate_restaurant_score:
            print("Thanks\n")
    except ValueError:
        print("Score format incorrect, please try again\n")
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


def validate_spa_score(input):
    """
    Raises action from user if score not entered
    in correct format.
    """
    try:
        if input == validate_spa_score:
            print("Thanks\n")
    except ValueError:
        print("Score format incorrect, please try again\n")
        return False

    return True


def update_spa_score_guest_feedback_worksheet(spa):
    """
    Update guest feedback worksheet,
    add new row with the restaurant score provided
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


def validate_hotel_room_score(input):
    """
    Raises action from user if score not entered
    in correct format.
    """
    try:
        if input == validate_hotel_room_score:
            print("Thanks\n")
    except ValueError:
        print("Score format incorrect, please try again\n")
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

        special_offers_data = data_str.split(" ")

        if validate_special_offers(special_offers_data):
            print("It is valid!")
            break

    return special_offers_data


def validate_special_offers(input):
    """
    Raises action from user if data not entered
    in correct format either yes or no.
    """
    try:
        if input == validate_special_offers:
            print("Thanks\n")
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
