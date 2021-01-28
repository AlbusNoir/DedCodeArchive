'''
    Variation of scatter_squares done automatically
'''
import matplotlib.pyplot as plt

# values
x_values = range(1, 1001)
y_values = [x**2 for x in x_values]

plt.style.use('seaborn')  # built in style
fix, ax = plt.subplots()
# plot and assign colour based on y_value using cmap(colormap)
ax.scatter(x_values, y_values, c=y_values, cmap=plt.cm.Blues, s=10)

# set chart title and axis labels
ax.set_title('Square Numbers', fontsize=24)
ax.set_xlabel('Value', fontsize=14)
ax.set_ylabel('Square of Value', fontsize=14)

# set range for each axis
ax.axis([0, 1100, 0, 1100000])

# set tick labels
ax.tick_params(axis='both', which='major', labelsize=14)


plt.show()
# uncomment below to save figure with trimmed whitespace
# plt.savefig('squares_plot.png', bbox_inches='tight')
