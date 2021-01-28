"""
    output:
    1 - basal metabolic rate - input  current weight age height
    2 - how many cals to lose weight - same input
    3 - how many cals to gain weight - same input

    Make gui
"""


def calc_bmr():
    gender = input('Please specify if you identify as male or female using m or f: ')

    if gender.lower() == 'm':
        age = int(input('Please enter your age: '))

        weight = int(input('Please enter your weight, in pounds: '))

        height = int(input('Please enter your height, in inches: '))

        # switch weight to kilos - lbs / 2.205
        weight_kg = weight / 2.205

        # switch height to cm - in * 2.54
        height_cm = height * 2.54

        # calc bmr - male calc
        bmr = 10 * weight_kg + 6.25 * height_cm - 5 * age + 5

        lose_amt = bmr - 500
        gain_amt = bmr + 500

        print(f'Your BMR is roughly {bmr:.0f}.\nTo lose weight you should consume roughly {lose_amt:.0f}.\nTo gain weight, you should consume roughly {gain_amt:.0f}.')

        repeat()

    elif gender.lower() == 'f':
        age = int(input('Please enter your age: '))

        weight = int(input('Please enter your weight, in pounds: '))

        height = int(input('Please enter your height, in inches: '))

        # switch weight to kilos - lbs / 2.205
        weight_kg = weight / 2.205

        # switch height to cm - in * 2.54
        height_cm = height * 2.54

        # calc bmr - female calc
        bmr = 10 * weight_kg + 6.25 * height_cm - 5 * age - 161

        lose_amt = bmr - 500
        gain_amt = bmr + 500

        print(f'Your BMR is roughly {bmr:.0f}.\nTo lose weight you should consume roughly {lose_amt:.0f}.\nTo gain weight, you should consume roughly {gain_amt:.0f}.')

        repeat()


def repeat():
    r = input('\nDo you want to calculate something else? yN: ')

    if r.lower() == 'y':
        calc_bmr()
    else:
        quit()


calc_bmr()
