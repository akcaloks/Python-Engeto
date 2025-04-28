"""
projekt_1.py: první projekt do Engeto Online Python Akademie

author: Jana Barotová
email: jana.barotova@seznam.cz
"""
import sys

TEXTS = [
    '''Situated about 10 miles west of Kemmerer,
    Fossil Butte is a ruggedly impressive
    topographic feature that rises sharply
    some 1000 feet above Twin Creek Valley
    to an elevation of more than 7500 feet
    above sea level. The butte is located just
    north of US 30 and the Union Pacific Railroad,
    which traverse the valley.''',
    '''At the base of Fossil Butte are the bright
    red, purple, yellow and gray beds of the Wasatch
    Formation. Eroded portions of these horizontal
    beds slope gradually upward from the valley floor
    and steepen abruptly. Overlying them and extending
    to the top of the butte are the much steeper
    buff-to-white beds of the Green River Formation,
    which are about 300 feet thick.''',
    '''The monument contains 8198 acres and protects
    a portion of the largest deposit of freshwater fish
    fossils in the world. The richest fossil fish deposits
    are found in multiple limestone layers, which lie some
    100 feet below the top of the butte. The fossils
    represent several varieties of perch, as well as
    other freshwater genera and herring similar to those
    in modern oceans. Other fish such as paddlefish,
    garpike and stingray are also present.'''
]

USERS = {
    "bob": "123",
    "ann": "pass123",
    "mike": "password123",
    "liz": "pass123"
}
username = input("username:")
password = input("password:")

if username in USERS and USERS[username] == password:
    print("-" * 40, f'Welcome to the app, {username}', f'We have {len(TEXTS)} texts to be analyzed.', "-" * 40, sep="\n")
    selected = input("Enter a number btw. 1 and 3 to select:")
    print("-" * 40)

    if not selected.isdigit() or int(selected) < 1 or int(selected) > len(TEXTS):
        print("Invalid input. Must be a number between 1 and 3. Terminating the program.")
        sys.exit()

    else:
        if selected == "1":
            text = TEXTS[0]
        elif selected == "2":
            text = TEXTS[1]
        elif selected == "3":
            text = TEXTS[2]
    
    cleared_words = [word.strip(".,") for word in text.split()]

    titlecase_count = sum(1 for word in cleared_words if word.istitle())
    uppercase_count = sum(1 for word in cleared_words if word.isupper())
    lowercase_count = sum(1 for word in cleared_words if word.islower())
    numeric_strings_count = sum(1 for word in cleared_words if word.isdigit())
    number_sum = sum(int(word) for word in cleared_words if word.isdigit())

    print(f'There are {len(cleared_words)} words in the selected text.')
    print(f'There are {titlecase_count} titlecase words.')
    print(f'There are {uppercase_count} uppercase words.')
    print(f'There are {lowercase_count} lowercase words.')
    print(f'There are {numeric_strings_count} numeric strings.')
    print(f'The sum of all the numbers {number_sum}', "-" * 40, sep = "\n")
    print(f'{"LEN":>3}|{"OCCURRENCES":^15}|NR.', "-" * 40, sep="\n")

    word_length_count = {}
    for word in cleared_words:
        word_length = len(word)
        if word_length not in word_length_count:
            word_length_count[word_length] = 1
        else:
            word_length_count[word_length] += 1

    for length in sorted(word_length_count):
        count = word_length_count[length]
        stars = "*" * count
        print(f"{length:>3}| {stars:<20}|{count}")

else: 
    print(f'unregistered user, terminating the program..')
    sys.exit()
