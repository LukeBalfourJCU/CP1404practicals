def main():
    trigger = False

    while not trigger:
        trigger = get_password(trigger)


def get_password(trigger):
    user_password = input("Enter password: ")
    length = len(user_password)
    if length >= 5:
        trigger = print_asterisk(length, trigger)
    else:
        print("Password must be more than 4 characters")
    return trigger


def print_asterisk(length, trigger):
    trigger = True
    print("*" * length)
    return trigger


main()
