class Guitar:
    def __int__(self, name, year, cost=0):
        self.name = name
        self.year = year
        self.cost = cost

    def __str__(self):
        print("{} ({}) : ${}".format(self.name, self.year, self.cost))


def get_age(year):
    age = 2021 - year
    return age


def is_vintage(age):
    if age >= 50:
        return True
    else:
        return False
