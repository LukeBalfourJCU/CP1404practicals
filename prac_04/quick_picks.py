import random

"""
I have absolutely no clue what I'm doing.
"""

def main():
    user_input = int(input("How many quick picks? "))
    for line in range(1, user_input):
        generate_numbers(user_input)
        print(result)

# lottery_line = [number[0] for number in lottery]
# for line in range(user_input):
#    random_number = random.randint(1, 45)
#    lottery_line.append(random_number)
#    lottery.append(lottery_line)


def generate_numbers(user_input):
    random_number = random.randint(1, 45)
    lottery_line = str((random_number + " ") * user_input)
    result = str(lottery_line)
    return result

main()
