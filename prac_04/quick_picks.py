import random
lottery = []


user_input = int(input("How many quick picks? "))
print(lottery)


lottery_line = [number[0] for number in lottery]
for line in range(user_input):
    random_number = random.randint(1, 45)
    lottery_line.append(random_number)
    lottery.append(lottery_line)
