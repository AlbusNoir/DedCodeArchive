'''
    Visualazation file for random walk
'''
import matplotlib.pylab as plt

from random_walk import RandomWalk

# make a random walk while True
while True:
    rw = RandomWalk(50_000)  # can pass values
    rw.fill_walk()

    # plot points
    plt.style.use('classic')
    fig, ax = plt.subplots(figsize=(10, 6), dpi=128)  # alter to fit screen
    point_numbers = range(rw.num_points)
    ax.scatter(rw.x_values, rw.y_values, c=point_numbers, cmap=plt.cm.Blues, edgecolors='none', s=1)

    # emphasize the first and last points
    ax.scatter(0, 0, c='green', edgecolors='none', s=100)
    ax.scatter(rw.x_values[-1], rw.y_values[-1], c='red', edgecolors='none', s=100)

    # remove axes
    ax.get_xaxis().set_visible(False)
    ax.get_yaxis().set_visible(False)

    plt.show()

    keep_running = input("Make another walk? Enter 'q' to quit: ")
    if keep_running == 'q':
        break
