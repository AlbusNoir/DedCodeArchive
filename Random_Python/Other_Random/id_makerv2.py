# found id maker and decided to make it better and less student focused? idk

def make_id():
    name = input("Enter your first name: ")
    last_name = input("Enter your last name: ")
    birth_year = input("Enter your birth year: ")

    if len(name) <= 3:
        s = (name[0] + last_name[0:3] + birth_year[2:])
    else:
        s = (name[0:2] + last_name[0:2] + birth_year[2:])

    print(s)


make_id()
