from cmath import e
import pandas as pd
student_dict = {
    "student": ["Angela", "James", "Lily"],
    "score": [56, 76, 98]
}

# Looping through dictionaries:
for (key, value) in student_dict.items():
    # Access key and value
    pass

student_data_frame = pd.DataFrame(student_dict)

# Loop through rows of a data frame
for (index, row) in student_data_frame.iterrows():
    # Access index and row
    # Access row.student or row.score
    pass

# Keyword Method with iterrows()
# {new_key:new_value for (index, row) in df.iterrows()}


# TODO 1. Create a dictionary in this format:
alphabets = pd.read_csv(
    "Projects/D26_NATO-alphabet/nato_phonetic_alphabet.csv")
alphabet_dict = {row.letter: row.code for ind, row in alphabets.iterrows()}
# or, we can use
# letters = alphabets.letter.to_list()
# codes = alphabets.code.to_list()
# alphabet_dict = {letters[i]: codes[i] for i in range(len(letters))}
# print(alphabet_dict)

# TODO 2. Create a list of the phonetic code words from a word that the user inputs.
def prog():
    phonetic_list = []
    name = input("Enter your name: ").upper()
    try:
        phonetic_list = [{i: alphabet_dict[i]} for i in name]
    except KeyError:
        print("Please enter a valid key with alphabets")
        prog()
    print(phonetic_list)

prog()


# Equivalent to line 41 👇🏻👇🏻
# for i in range(len(name)):
#     if name[i] in alphabet_dict.keys():
#         phonetic_list.append({name[i]: alphabet_dict[name[i]]})
