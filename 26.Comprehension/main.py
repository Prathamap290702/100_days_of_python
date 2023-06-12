import pandas as pd
data = pd.read_csv("nato_phonetic_alphabet.csv")
my_dict = {row.letter:row.code for (index, row) in data.iterrows()}
name = input("Enter a Word : ").upper()
result = [my_dict[letter] for letter in name]
print(result)
