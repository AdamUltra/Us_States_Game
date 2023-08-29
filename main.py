import turtle
import pandas

data = pandas.read_csv("50_states.csv")
all_states = data.state.to_list()
correct_answers = []
missing_states = []
screen = turtle.Screen()
screen.title("U.S. States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

while len(correct_answers) < 50:
    answer_state = screen.textinput(title=f"{len(correct_answers)}/50 States Correct",
                                    prompt="What's another state's name?").title()

    if answer_state == "Exit":
        for state in all_states:
            if state not in correct_answers:
                missing_states.append(state)
        new_data = pandas.DataFrame(missing_states)
        new_data.to_csv("States_To_Learn.csv")
        break
    if answer_state in all_states:
        if answer_state not in correct_answers:
            correct_answers.append(answer_state)
            state_data = data[data.state == answer_state]
            x = state_data.x[state_data.index[0]]
            y = state_data.y[state_data.index[0]]
            name_in_map = turtle.Turtle()
            name_in_map.hideturtle()
            name_in_map.penup()
            name_in_map.goto(x, y)
            name_in_map.write(answer_state)


