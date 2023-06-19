import pandas as pd
data = pd.read_csv("nato_phonetic_alphabet.csv")
my_dict = {row.letter:row.code for (index, row) in data.iterrows()}
def input_name():
    name = input("Enter a Word : ").upper()
    try:
        result = [my_dict[letter] for letter in name]
    except KeyError:
        print("Sorry, only letters in the alphabets please.")
        input_name()
    else:
        print(result)
input_name()

#changing the code after learning data handling to handle errors where the input has charachters other than alphabets