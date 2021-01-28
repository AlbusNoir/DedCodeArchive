import sys
import time


def progressbar(count, total, status=''):
    bar_len = 60
    filled_len = int(round(bar_len * count / float(total)))

    percents = round(100.0 * count / float(total), 1)
    bar = '=' * filled_len + '-' * (bar_len - filled_len)

    sys.stdout.write(f'\r[{bar}] {percents}% ...{status}')
    sys.stdout.flush()

total = 10
i = 0
while i < total+1:  # allows for 100%, fixes off by one error
    progressbar(i, total, status='Working')
    time.sleep(0.5)  # emulating long-playing job
    i += 1
