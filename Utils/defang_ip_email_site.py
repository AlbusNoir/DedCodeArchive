# enhancement to defang_ip.py
# now handles email, ip, sites

from IPy import IP
import re


def intro():
    print('''[D][efang]
        Please select an option to begin:
        1) Defang IP
        2) Defang website
        3) Defang email''')

    choice = int(input("> "))

    user_choice(choice)


def user_choice(choice):
    err = "Input not understood. Choose an option"

    if choice == 1:
        defang_ip()
    elif choice == 2:
        defang_website()
    elif choice == 3:
        defang_email()
    else:
        print(err)
        intro()


def defang_ip():
    ip = input("Enter IP to defang: ")

    if IP(ip):
        ip = ip.split(".")
        ip_defanged = "[.]".join(ip)

        print(ip_defanged)

        repeat()

    else:
        print("Invalid IP")
        defang_ip()

        repeat()


def defang_website():
    site = input("Enter website to defang: ")

    site = site.split(".com")

    site_defanged = "[.com]".join(site)

    print(site_defanged)

    repeat()


def defang_email():
    email = input("Enter an email to defang: ")

    email_re = re.compile(r"[^@]+@[^@]+\.[^@]+")

    if email_re.match(email):
        email = email.split("@")
        email_defanged = "[@]".join(email)

        print(email_defanged)

        repeat()
    else:
        print("Improperly formatted email")
        defang_email()

        repeat()


def repeat():
    rep = input("Do you need to defang again? yN")

    if rep.lower() == 'y':
        intro()
    else:
        exit()


intro()
