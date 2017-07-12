from sys import argv


def get_password_strength(password, blacklist_path=None):
    points = 1
    if len(password) > 3:
        points += len(password) // 5
        points += check_for_standard_recommendations(password)
        points += count_unique_letters(password) // 2
        points -= check_for_duplicate_letters(password)
        if blacklist_path:
            points -= check_by_blacklist(password, blacklist_path)

    if points < 0:
        points = 1
    elif points > 10:
        points = 10

    return points


def check_for_duplicate_letters(password):
    for number, letter in enumerate(password):
        if letter == password[number - 1] and letter == password[number - 2]:
            return 2
    return 0


def count_unique_letters(password):
    unique_letters = ""
    for letter in password:
        if letter not in unique_letters:
            unique_letters += letter
    return len(unique_letters)


def check_for_standard_recommendations(password):
    points = 0
    control_list = ["abcdefghijklmnopqrstuvwxyz", "ABCDEFGHIJKLMNOPQRSTUVWXYZ",
                    "~`!@#$%^&*()-_+=", "1234567890"]
    for control_string in control_list:
        for letter in password:
            if letter in control_string:
                points += 1
                break
    return points


def check_by_blacklist(password, blacklist_path):
    try:
        with open(blacklist_path, "r") as blacklist_file:
            password_blacklist = blacklist_file.readlines()
    except:
        return 0

    for word in password_blacklist:
        if password in word:
            return 8
    return 0


if __name__ == '__main__':
    password = input("Input your password: ")
    if not password:
        exit()
    if len(argv) == 2:
        rating = get_password_strength(password, argv[1])
    else:
        rating = get_password_strength(password)
    print("Password rating - " + str(rating))
    print("1 - very weak; 10 - cool")
