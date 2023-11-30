import turtle
import pandas

screen = turtle.Screen()
screen.title("U.S. States Game")
image = "blank_states_img.gif"
screen.addshape(image)
# ^^^ Add or U.S. states image as a shape for turtle to use (as seen below)

turtle.shape(image)

states_t = turtle.Turtle()
states_t.pu()
states_t.hideturtle()

states_data = pandas.read_csv("50_states.csv")
# ^^^ states_data is a data frame

states_remaining = len(states_data["state"])

gaming = True

print(states_data)

while states_remaining >= 1:
  user_state = screen.textinput(title="Guess a U.S. State", prompt=f"You have {states_remaining} States left")
  # Check if the user wants to exit the game
  if user_state.lower() == 'exit':
    break
  # Check if the guessed state is in the DataFrame
  if user_state.lower() in states_data["state"].str.lower().values:
    # Place name of state on the map
    answer = states_data[states_data["state"].str.lower() == user_state.lower()]
    # print(answer)
    answer_list = answer.iloc[0].values.tolist()
    # print(answer_list)
    states_t.setpos(x=answer_list[1], y=answer_list[2])
    states_t.write(f"{answer_list[0]}", 'center', font=('Courier', 8, 'normal'))
    # Drop the row where the state matches the user's input
    states_data = states_data[states_data["state"].str.lower() != user_state.lower()]
    states_remaining = len(states_data)
    # print(states_remaining)
    # print(states_data)
    print(states_data)
