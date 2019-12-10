import random
import operator
import csv
import matplotlib.pyplot

def distance_between(agents_row_a, agents_row_b):
    return (((agents_row_a[0] - agents_row_b[0])**2) +
        ((agents_row_a[1] - agents_row_b[1])**2))**0.5

num_of_agents = 10
num_of_iterations = 100
agents = []
# Make the agents.
for i in range(num_of_agents):
    agents.append([random.randint(0,300),random.randint(0,300)])


f = open('drunk.txt')
reader = csv.reader(f,delimiter=',')
environment = []
for row in reader:
    rowlist = []
    for value in row:
        rowlist.append(int(value))
    environment.append(rowlist)
f.close()

matplotlib.pyplot.figure(figsize = (10,10))
matplotlib.pyplot.imshow(environment)
# Move the agents.
trajectories = [[[],[]] for i in range(num_of_agents)]
for j in range(num_of_iterations):
    
    for i in range(num_of_agents):
        
       
        if random.random() < 0.5:
            agents[i][0] = (agents[i][0] + 1) % 300
        else:
            agents[i][0] = (agents[i][0] - 1) % 300

        if random.random() < 0.5:
            agents[i][1] = (agents[i][1] + 1) % 300
        else:
            agents[i][1] = (agents[i][1] - 1) % 300
        trajectories[i][0].append(agents[i][0])
        trajectories[i][1].append(agents[i][1])
        
matplotlib.pyplot.xlim(0, 300)
matplotlib.pyplot.ylim(0, 300)
for i in range(num_of_agents):
    matplotlib.pyplot.plot(trajectories[i][1],trajectories[i][0])
matplotlib.pyplot.show()

for agents_row_a in agents:
    for agents_row_b in agents:
        distance = distance_between(agents_row_a, agents_row_b)