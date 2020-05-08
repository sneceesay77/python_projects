import matplotlib.pyplot as plt


plt.style.use('seaborn')
fig, ax = plt.subplots()
x_values = [value for value in range(1,1001)]
y_values = [value*value for value in range(1,1001)]
#ax.scatter(x_values,y_values, s=10, c='red')
ax.scatter(x_values,y_values, s=10, c=y_values, cmap=plt.cm.Blues)

ax.set_title("Square of Numbers", fontsize=24)
ax.set_xlabel("Value", fontsize=14)
ax.set_ylabel("Square of Value", fontsize=14)

ax.axis([0, 1100, 0, 1100000])

plt.show()
#Save the plot
plt.savefig('square_plot.png', bbox_inches='tight')