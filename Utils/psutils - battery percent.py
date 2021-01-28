import psutil


def secs_to_hours(secs):
    mm, ss = divmod(secs, 60)
    hh, mm = divmod(mm, 60)
    return '%d:%02d:%02d' % (hh, mm, ss)

batt = psutil.sensors_battery()



print('Charge = %s%%, Time Left = %s' % (batt.percent, secs_to_hours(batt.secsleft)))

input('press enter to close')
