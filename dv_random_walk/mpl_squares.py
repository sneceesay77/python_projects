import matplotlib.pyplot as plt


squares = []
for i in range(1,100):
    squares.append(i*i)
#using builtin styles
plt.style.use('seaborn')
fig, ax = plt.subplots()
ax.plot(squares, linewidth=3)
##set chart title
ax.set_title("Square Numbers", fontsize=24)
ax.set_xlabel("Value", fontsize=14)
ax.set_ylabel("Square of Value", fontsize=14)
#Set size of tick labels
ax.tick_params(axis='both', labelsize=14)
plt.show()

