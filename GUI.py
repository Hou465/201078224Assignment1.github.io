import matplotlib
#allows to make plots
matplotlib.use('TkAgg')
import random
import operator
import matplotlib.pyplot
#allows plots to be created

import matplotlib.animation
#matplotlib.use('TkAgg')
import agentframework
#connects to the agentframework file
import csv
#allows for csv files to be added
import requests
#allows to take info from internet
import bs4
#allows to use functions to read html data
import tkinter
#allows set up of GUI window
#import tkMessageBox

#top = tkinter.tk()
#
#def helloCallBack():
#   tkMessageBox.showinfo( "Hello Python", "Hello World")
#
#B = tkinter.Button(top, text ="Hello", command = helloCallBack)
#
#B.pack()
#top.mainloop()





#this function will be where you set up your agents
# inside it you will need to 'get' the value from the slider (using .get)
#def sel():
#define a function 
#   selection = "Value = " + str(var.get())
#   tkinter.label.config(text = selection)

# this bit here defines and explains the pop-up (which we're calling root)
#root = tkinter.Tk()
#var = DoubleVar()

# this is the information about your slider - what it looks like, values etc
#scale = tkinter.Scale( root )
#scale.pack()

# this is the information about your button - when you press this it will run
# a command e.g. in the example command=sel
# your command will be the function above where you set up your agents
#button = tkinter.Button(root, text="Set Up the Agent", command=sel)
#button.pack()

#label = Label(root)
#label.pack()

#root.mainloop()





r = requests.get('http://www.geog.leeds.ac.uk/courses/computing/practicals/python/agent-framework/part9/data.html')
#gets html from the website used in 'web scraping' prac
content = r.text
#taking the text from the web link above
soup = bs4.BeautifulSoup(content, 'html.parser')
#setting up the website data to be readible
td_ys = soup.find_all(attrs={"class" : "y"})
#setting the y coordinates
td_xs = soup.find_all(attrs={"class" : "x"})

print(td_ys)
print(td_xs)

num_of_agents = 10
num_of_iterations = 100
neighbourhood = 20
agents = []


f = open('in.txt', newline='')
#open the csv file in working directory
reader = csv.reader(f, quoting=csv.QUOTE_NONNUMERIC)

# 
environment = []

for row in reader:
    
    rowlist = []
    
    for value in row:
        
        rowlist.append(value)
 #at end of list put a value       
        
    environment.append(rowlist)
#stops from filling up on just one rowlist    
f.close
#done looking at CSV



# Make the agents.
for i in range(num_of_agents):
    y = int(td_ys[i].text)
    x = int(td_xs[i].text)
    agents.append(agentframework.Agent(environment, agents, y, x))


fig = matplotlib.pyplot.figure(figsize=(7, 7))
ax = fig.add_axes([0, 0, 1, 1])


#ax.set_autoscale_on(False)
carry_on = True

def update(frame_number):
    
    fig.clear()   
    matplotlib.pyplot.imshow(environment)

    # Move the agents.
    for i in range(num_of_agents):
        agents[i].move()
    
    for i in range(num_of_agents):
        matplotlib.pyplot.scatter(agents[i].y,agents[i].x)
        print(agents[i].x,agents[i].y)
        
    # here you will need to draw your sheep - using matplotlib.pyplot.scatter

    
def gen_function(b = [0]):
    a = 0
    global carry_on #Not actually needed as we're not assigning, but clearer
    while (a < 10) & (carry_on) :
        yield a			# Returns control and waits next call.
        a = a + 1


def run():
    animation = matplotlib.animation.FuncAnimation(fig, update, frames=gen_function, repeat=False)
    canvas.draw()


#root = tkinter.Tk()
#root.wm_title("Model")





root = tkinter.Tk()
root.wm_title("Model")
menu = tkinter.Menu(root)
root.config(menu=menu)
model_menu = tkinter.Menu(menu)
canvas = matplotlib.backends.backend_tkagg.FigureCanvasTkAgg(fig, master=root)
canvas._tkcanvas.pack(side=tkinter.TOP, fill=tkinter.BOTH, expand=1)
menu.add_cascade(label="Model 4", menu=model_menu)
model_menu.add_command(label="Run model", command=run)



root.mainloop
tkinter.mainloop()





