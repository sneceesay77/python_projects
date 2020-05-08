from die import Die
from plotly.graph_objs import Bar, Layout
from plotly import offline

die1 = Die()#default six sided die
die2 = Die(10)#lets roll a 10 sided die

results = []
for roll_num in range(50_000):
    result = die1.roll() + die2.roll()
    results.append(result)

frequencies =  []
max_result = die1.num_sides + die2.num_sides
for value in range(2, max_result+1):
    frequency = results.count(value)
    frequencies.append(frequency)

print(frequencies)


#Visualise the results
x_values = list(range(2, max_result+1))
data = [Bar(x=x_values, y=frequencies)]

x_axis_config = {'title': 'Result', 'dtick': 1}
y_axis_config = {'title': 'Frequency of Results'}

my_layout = Layout(title='Result of rolling a D6 and a D10 50_000 times', xaxis=x_axis_config, yaxis=y_axis_config)
offline.plot({'data': data, 'layout': my_layout}, filename='d6_d10.html')
