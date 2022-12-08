import random
words_list = ["monkey", "dinosaur", "amphibian", "chimpanzee", "kangaroo"]
word = random.choice(words_list)
print(word)
for g in range(len(word)):
    guess =  input("Guess a letter : ")
    l = [i for i in word]
    for i in l:
        if guess == i:
            print(guess)
        else:
            print("_")