'''
    GPA Calc
    Borrowed from Data Structures & Algorithms book
    Edited to use fstrings and a few other changes
'''
print('''
        GPA CALC
        Please enter all your letter grades, one per line
        Enter a blank line to designate the end
    ''')

# map letter to points
points = {'A+':4.0, 'A':4.0, 'A-':3.67, 'B+':3.33, 'B':3.0, 'B-':2.67, 'C+':2.33, 'C':2.0, 'C-':1.67, 'D+':1.33, 'D':1.0, 'F':0.0}
num_courses = 0
total_points = 0
done = False


# set while loop
while not done:
    grade = input('Grade: ').upper()
    if grade == '':
        # end if blank
        done = True
    elif grade not in points:
        # grade not found in points. I.e D-
        print(f'Unknown grade {grade}. Being ignored for calculation')
    else:
        num_courses += 1  # add count to num_courses
        total_points += points[grade]  # ref map and tally points

# 0 check. Avoid division by 0
if num_courses > 0:
    print(f'Your GPA is {total_points / num_courses}')
