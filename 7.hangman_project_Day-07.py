import random
words_list = ["monkey", "dinosaur", "amphibian", "chimpanzee", "kangaroo"]
word = random.choice(words_list)
# print(word)
display = []
for i in range(len(word)):
    display.append("_")
print(display)

end_of_game = False
while end_of_game == False:
    guess = input("Guess a letter : ").lower()
    for pos in range(0, len(word)):
        char = word[pos]
        if char == guess:
            display[pos] = guess
    print(display)
    if "_" not in display:
        end_of_game = True
        print("You won.")
