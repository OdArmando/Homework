numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
            'v', 'w', 'x', 'y', 'z']
special_characters = ['¬', '`', '!', '"', '\'', '£', '$', '%', '^', '&', '*', '(', ')', '-', '_', '=', '+', '[', ']',
                      '{', '}', ';', ':', '@',
                      '#', '~', ',', '<', '.', '>', '/', '?', '|', ' ']
user_input = input("Passowrd: ")
user_password = list(user_input)


def check_numbers(password):
    for element in password:
        if element in numbers:
            return True
    else:
        print("Number is missing!")


def check_alfabet(password):
    for element in password:
        if element in alphabet:
            return True
    else:
        print("Letter is missing!")


def check_special_characters(password):
    for element in password:
        if element in special_characters:
            return True
    else:
        print("Special character is missing!")


def check_if_upper(password):
    for element in password:
        if element.isupper():
            return True
    else:
        print("One upper case is required!")


def check_length(password):
    if len(password) >= 8:
        return True
    else:
        print("Password must have at least 8 elements!")


def check_password(password):
    if all([check_numbers(password), check_alfabet(password), check_special_characters(password),
            check_if_upper(password), check_length(password)]):
        print("Correct!")
    else:
        print("Incorrect password!")


check_password(user_input)


