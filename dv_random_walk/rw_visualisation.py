import matplotlib.pyplot as plt
from random_walk import RandomWalk


while True:
    rw = RandomWalk(50_000)
    rw.fill_walk()

    plt.style.use('classic')

    #using a custom screen size
    fig, ax = plt.subplots(figsize=(10, 6), dpi=128)
    point_numbers = range(rw.num_points)
   
   
    ax.scatter(rw.get_x_values(), rw.get_y_values(), s=1, c=point_numbers, cmap=plt.cm.Blues, edgecolors='none')
    #Highlight first and last point and do some colouring
    ax.scatter(0, 0, c='green', edgecolors='none', s=100)
    ax.scatter(rw.get_x_values()[-1], rw.get_y_values()[-1], c='red', edgecolors='none', s=100)

    #Remove the axis
    ax.get_xaxis().set_visible(False)
    ax.get_yaxis().set_visible(False)

    plt.show()
    

    keep_running = input("Make another walk? (y/n): ")
    if keep_running == 'n':
        break 