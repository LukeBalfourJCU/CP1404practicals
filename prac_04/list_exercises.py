"""
PART 1
"""
numbers = []

for number in range(5):
    user_input = int(input("Please enter number: "))
    numbers.append(user_input)

print("The first number is: {}".format(numbers[0]))

print("The last number is: {}".format(numbers[-1]))

print("The smallest number is: {}".format(min(numbers)))

print("The largest number is: {}".format(max(numbers)))

print("The average is: {}".format(sum(numbers)/len(numbers)))

"""
PART 2
"""
usernames = ['jimbo', 'giltson98', 'derekf', 'WhatSup', 'NicolEye', 'swei45', 'BaseInterpreterInterface', 'BaseStdIn',
             'Command', 'ExecState', 'InteractiveConsole', 'InterpreterInterface', 'StartServer', 'bob']
user_password = str(input("Please enter password: "))
if user_password in usernames:
    print("Access granted")
else:
    print("Access denied")
