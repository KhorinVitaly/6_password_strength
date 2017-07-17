from sys import argv
import string, re, getpass


def get_password_strength(password, blacklist_path=None):
    points = 1

    lenght_coef = 5
    unique_symbols_quantity_coef = 2
    minimal_lenght = 3

    min_point = 1
    max_point = 10

    if len(password) > minimal_lenght:
        points += len(password) // lenght_coef
        points += check_for_symbols_diversity(password)
        points += count_unique_symbols(password) // unique_symbols_quantity_coef
        points -= check_for_duplicate_symbols(password)

        blacklist = get_blacklist(blacklist_path)
        points -= check_by_blacklist(password, blacklist)

    if points < min_point:
        points = min_point
    elif points > max_point:
        points = max_point

    return points


def check_for_duplicate_symbols(password):
    if re.search(r'(.)\1{1,}', password):
        return 2
    else:
        return 0


def count_unique_symbols(password):
    password_as_set = set(password)
    return len(password_as_set)


def check_for_symbols_diversity(password):
    points = 0
    password_as_set = set(password)
    control_list = [string.ascii_lowercase, string.ascii_uppercase,
                    string.punctuation, string.digits]
    for control_string in control_list:
        if password_as_set & set(control_string):
            points += 1
    return points


def get_blacklist(blacklist_path):
    try:
        with open(blacklist_path, "r") as blacklist_file:
            return blacklist_file.readlines()
    except FileNotFoundError:
        return []

    
def check_by_blacklist(password, blacklist):
    for word in blacklist:
        if password in word:
            return 8
    return 0


if __name__ == '__main__':
    password = getpass.unix_getpass("Input your password: ")
    if not password:
        exit()
    if len(argv) == 2:
        rating = get_password_strength(password, argv[1])
    else:
        rating = get_password_strength(password)
    print("Password rating - " + str(rating))
    print("1 - very weak; 10 - cool")
