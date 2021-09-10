from prac_06.guitar import Guitar


def main():
    guitars = []
    name = input("Name: ")
    year = int(input("Year: "))
    cost = float(input("Cost: "))
    guitar = Guitar(name, year, cost)
    guitars.append(guitar)
    print(guitar, "added.")
    guitars.append(Guitar("Gibson L-5 CES", 1922, 16035.40))
    guitars.append(Guitar("Line 6 JTV-59", 2010, 1512.9))

    print("These are my guitars: ")
    for i, guitar in enumerate(guitars, 1):
        vintage = ""
        if guitar.is_vintage():
            vintage = " is vintage"
        print("Guitar {}: {} ({}), worth ${:,.2f} {}".format(i, guitar.name, guitar.year, guitar.cost, vintage))


main()
