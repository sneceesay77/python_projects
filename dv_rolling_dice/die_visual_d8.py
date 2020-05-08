from die import Die
from plotly.graph_objs import Bar, Layout
from plotly import offline

die_1 = Die(8)
die_2 = Die(8)

#Using normal loop
# results = []
# for num_roll in range(0, 1000):
#     roll_result = die_1.roll() + die_2.roll()
#     results.append(roll_result)
# 
# print(results)

#Using list comprehension
results = [die_1.roll()+die_2.roll() for i in range(1000)]
print(results)

max_result = die_1.num_sides + die_2.num_sides
frequencies = [results.count(value) for value in range(2, max_result+1)]

#Visualise the results
x_values = list(range(2, max_result+1))
data = [Bar(x=x_values, y=frequencies)]

x_axis_config = {'title': 'Result', 'dtick': 1}
y_axis_config = {'title': 'Frequency of Results'}

my_layout = Layout(title='Result of rolling two D8 1_000 times', xaxis=x_axis_config, yaxis=y_axis_config)
offline.plot({'data': data, 'layout': my_layout}, filename='d8.html') 
    