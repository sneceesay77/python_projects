from random import choice


class RandomWalk:
    def __init__(self, num_points=5000):
        #defines the number or random points
        self.num_points = num_points
        #stores the x and y coordinates of the point.
        self.x_values = [0]
        self.y_values = [0]

    def get_x_values(self):
        return self.x_values

    def get_y_values(self):
        return self.y_values

    def fill_walk(self):
        while len(self.x_values) < self.num_points:
            x_direction = choice([1, -1])
            x_distance = choice([0, 1, 2, 3, 5])
            x_step = x_direction * x_distance

            y_direction = choice([1, -1])
            y_distance = choice([0, 1, 2, 3, 4, 5])
            y_step = y_direction * y_distance

            #get last value in the list [-1] and add it to x_step
            x = self.x_values[-1] + x_step
            y = self.y_values[-1] + y_step

            self.x_values.append(x)
            self.y_values.append(y)

