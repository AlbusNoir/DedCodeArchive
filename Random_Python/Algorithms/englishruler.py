'''
    English Ruler
    English Rulers are examples of fractals. Shapes that have a self-recursive structure at various levels of magnification.
'''


def draw_line(tick_length, tick_label=''):
    '''Draw one line with given tick length (optional label)'''
    line = '-' * tick_length
    if tick_label:  # if there is a label
        line += ' ' + tick_label
    print(line)


def draw_interval(center_length):
    '''Draw tick interval based on central tick length'''
    if center_length > 0:  # stop when 0
        draw_interval(center_length - 1)  # recursively draw top ticks
        draw_line(center_length)  # draw center tick
        draw_interval(center_length - 1)  # recursively draw bottom ticks


def draw_ruler(num_inches, major_length):
    '''Draw English ruler with given num of inches, major tick length'''
    draw_line(major_length, '0')  # draw inch 0 line
    for j in range(1, 1 + num_inches):
        draw_interval(major_length - 1)  # draw ticks for each inch
        draw_line(major_length, str(j))  # draw inch line and label for j
