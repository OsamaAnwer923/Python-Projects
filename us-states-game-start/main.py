import turtle
import pandas
screen = turtle.Screen()

image = r'G:\osama\TO DO OSAMA\Python Projects(100 Days of Python Boot Camp)\us-states-game-start\blank_states_img.gif'
screen.addshape(image)
turtle.shape(image)
data = pandas.read_csv(r'G:\osama\TO DO OSAMA\Python Projects(100 Days of Python Boot Camp)\us-states-game-start\50_states.csv')
counter = 0 
states = data.state.to_list()
guess_states = []
while counter<50:
    answer=screen.textinput(title=f'{counter}/50 US States Game',prompt="What's another state name?").title()
    if answer == 'Exist':
        break
    if answer in states and not answer in guess_states:
        counter = counter+1
        guess_states.append(answer)
        state_data = data[data.state == answer]
        name_appear = turtle.Turtle()
        name_appear.hideturtle()
        name_appear.penup()
        name_appear.goto(int(state_data.x),int(state_data.y))
        name_appear.write(answer)
guess_states_set = set(guess_states)
states_set = set(states)
remaining_states = list(states_set.difference(guess_states_set))

# print(f"remaining states are {remaining_states}")
dic = {'Remaing states':remaining_states}
file_data = pandas.DataFrame(dic)
file_data.to_csv(r"./us-states-game-start/Remaining States.csv")

screen.exitonclick()
