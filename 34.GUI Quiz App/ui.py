from tkinter import *
THEME_COLOR = "#375362"
from quiz_brain import QuizBrain

class QuizInterface:
    def __init__(self, quiz_brain : QuizBrain):
        self.quiz = quiz_brain
        self.score = 0
        #UI
        self.window = Tk()
        self.window.title("Quizzler")
        self.window.configure(pady=20,padx=20,background=THEME_COLOR)

        #images
        self.true_img = PhotoImage(file="./images/true.png")
        self.false_img = PhotoImage(file="./images/false.png")


        #Canvas
        self.canvas = Canvas(width=300,height=250, bg="white")
        self.question_text = self.canvas.create_text(
            150,125,
            width=280,
            text = "Questions here",
            fill=THEME_COLOR,
            font=("Arial", 20, "italic"))
        self.canvas.grid(column=0,row=1, columnspan=2, padx=20, pady=20)


        #label
        self.score_label = Label(text=f"Score : {self.score}",background=THEME_COLOR, fg="white")
        self.score_label.grid(column=1, row=0)


        #Buttons
        self.true_button = Button(image=self.true_img, highlightthickness=0, command=self.true_pressed)
        self.true_button.grid(column=0,row=2, padx=20, pady=20)

        self.false_button = Button(image=self.false_img,highlightthickness=0, command=self.false_pressed)
        self.false_button.grid(column=1,row=2, padx=20, pady=20)
        self.get_next_question()

        self.window.mainloop()

    def get_next_question(self):
        self.canvas.configure(bg = "white")
        if self.quiz.still_has_questions():
            self.score_label.config(text=f"Score : {self.quiz.score}")
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.question_text, text = q_text)
        else:
            self.canvas.itemconfig(self.question_text, text = "You've reached the end of the questions")
            self.true_button.config(state="disabled")
            self.false_button.config(state="disabled")

    def true_pressed(self):
        self.give_feedback(self.quiz.check_answer("True"))

    def false_pressed(self):
        self.give_feedback(self.quiz.check_answer("False"))

    def give_feedback(self,is_right: bool):
        if is_right:
            self.canvas.configure(bg = "green")
        else:
            self.canvas.configure(bg = "red")
        self.window.after(1000,self.get_next_question)


