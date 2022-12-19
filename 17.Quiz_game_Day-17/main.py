# create class
# class User:
#     def __init__(self, id, user_name):  # Constructor
#         print("New user is created...")
#         self.id = id
#         self.user_name = user_name
#         self.followers = 0  # we can give constant to an attribute
#         self.following = 0

#     def follow(self, user):
#         user.followers += 1
#         self.following += 1


# without constructor
# user = User()
# user.id = 45
# user.user_name = "Rohit"
# print(user.user_name)
# user1 = User()
# user1.id = 18
# user1.user_name = "Virat"
# print(user1.user_name)


# after constructor
# user1 = User(45, "Rohit")
# user2 = User(18, "Virat")
# print(user1.user_name)
# print(user2.user_name)

# user1.follow(user2)
# print(user1.following)
# print(user1.followers)
# print(user2.following)
# print(user2.followers)

from data import question_data
from question_model import quizz
from quiz_brain import quizzbrain

question_bank = []
for questions in question_data:
    question_text = questions["text"]
    question_answer = questions["answer"]
    New_question = quizz(question_text, question_answer)
    question_bank.append(New_question)

quiz = quizzbrain(question_bank)

while quiz.still_has_question():
    quiz.next_question()
 
print("You've completed your Quiz.")
print(f"Your Final score is {quiz.score}/{quiz.question_number}.")