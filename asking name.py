def ask_name():
    name = ""
    name_looks_good = False

    while not name_looks_good:
        name = input("What is your name?\n")
        if len(name) < 3:
            print("Name must be at least 3 characters")
        elif len(name) > 50:
            print("Name can be a maximum of 50 characters")
        else:
            print("Name looks good!")
            name_looks_good = True

    return name
