# get yearly quarters
# calculate hours per quarter

q1 = ['Jan', 'Feb', 'Mar']
q2 = ['Apr', 'May', 'Jun']
q3 = ['Jul', 'Aug', 'Sep']
q4 = ['Oct', 'Nov', 'Dec']

d_jan = 31
d_feb = 28  # 29 in leap year
d_mar = 31
d_apr = 30
d_may = 31
d_jun = 30
d_jul = 31
d_aug = 31
d_sep = 30
d_oct = 31
d_nov = 30
d_dec = 31

h = 24  # lazy so made days hours into a var

h_jan = d_jan * h
h_feb = d_feb * h
h_feb_ly = (d_feb + 1) * h  # 29 days
h_mar = d_mar * h
h_apr = d_apr * h
h_may = d_may * h
h_jun = d_jun * h
h_jul = d_jul * h
h_aug = d_aug * h
h_sep = d_sep * h
h_oct = d_oct * h
h_nov = d_nov * h
h_dec = d_dec * h


def hours():

    print(f'''
Hours in Jan: {h_jan}
Hours in Feb: {h_feb}
Hours in Feb(leapyear): {h_feb_ly}
Hours in Mar: {h_mar}
Hours in Apr: {h_apr}
Hours in May: {h_may}
Hours in Jun: {h_jun}
Hours in Jul: {h_jul}
Hours in Aug: {h_aug}
Hours in Sep: {h_sep}
Hours in Oct: {h_oct}
Hours in Nov: {h_nov}
Hours in Dec: {h_dec}''')


def quarters():
    print(f'''
Q1: {q1}
Q2: {q2}
Q3: {q3}
Q4: {q4}''')


def quarter_hours():
    q1_total = h_jan + h_feb + h_mar
    q1_total_ly = h_jan + (h_feb+24) + h_mar  # account for leapyear
    q2_total = h_apr + h_may + h_jun
    q3_total = h_jul + h_aug + h_sep
    q4_total = h_oct + h_nov + h_dec
    print(f'''
Hours in Q1: {q1_total}
Hours in Q1 for leapyears: {q1_total_ly}
Hours in Q2: {q2_total}
Hours in Q3: {q3_total}
Hours in Q4: {q4_total}''')


hours()
quarters()
quarter_hours()
