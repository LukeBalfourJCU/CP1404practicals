"""
CP1404/CP5632 - Practical
Broken program to determine score status
"""

import random


def main():
    score = random.randint(0, 100)
    print(score)
    result = calculate_score(score)
    print("{}".format(result))


def calculate_score(score):
    if score < 51:
        result = "Bad"
    elif score > 90:
        result = "Excellent"
    else:
        result = "Passable"
    return result


main()
