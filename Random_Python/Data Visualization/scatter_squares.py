'''
    From python crash course
    scatter plot
'''
import matplotlib.pyplot as plt

# values
x_values = [1, 2, 3, 4, 5]
y_values = [1, 4, 9, 16, 25]

plt.style.use('seaborn')  # built in style
fix, ax = plt.subplots()
ax.scatter(x_values, y_values, s=100)

# set chart title and axis labels
ax.set_title('Square Numbers', fontsize=24)
ax.set_xlabel('Value', fontsize=14)
ax.set_ylabel('Square of Value', fontsize=14)

# set tick labels
ax.tick_params(axis='both', which='major', labelsize=14)


plt.show()
