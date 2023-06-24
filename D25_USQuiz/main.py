import pandas as pd
import turtle as t
screen = t.Screen()
screen.title("U.S. States Quiz")
image = "Projects/D25_USQuiz/blank_states_img.gif"
screen.addshape(image)
t.shape(image)


gameData = pd.read_csv("Projects/D25_USQuiz/50_states.csv")
states = gameData.state.to_list()
guessedStates = []

while len(guessedStates) < 50:
    answer = screen.textinput(title=f"{len(guessedStates)}/50 States Correct",
                              prompt="Enter the name of the State").title()
    if answer == "Exit":
        # missingStates=[]
        # for state in states:
        #     if state not in guessedStates:
        #         guessedStates.append(state)
        missingStates = [state for state in states if state not in guessedStates] # By list Comprehension
        missing = pd.DataFrame(missingStates)
        missing.to_csv("Projects/D25_USQuiz/MissingStates.csv")
        break
    
    if answer in states:
        state_row = gameData[gameData.state == answer]
        guessedStates.append(answer)
        name = t.Turtle()
        name.ht()
        name.pu()
        name.goto(int(state_row.x), int(state_row.y))
        name.write(answer)





# Another approach -- add these to
# xco = gameData.x.to_list()
# yco = gameData.y.to_list()
# while len(guessedStates) < 50:
#     answer = screen.textinput(title="Name the State",
#                               prompt="Enter the name of the State").capitalize()
#     for i in range(0, 50):
#         if answer == states[i]:
#             guessedStates.append(answer)
#             name = t.Turtle()
#             name.ht()
#             name.pu()
#             x = xco[i]
#             y = yco[i]
#             name.goto(int(x), int(y))
#             name.write(answer)
