from tkinter import *
from quiz_brain import QuizBrain
THEME_COLOR = "#375362"

class QuizInterface:
    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain
        self.score = 0
        self.window = Tk()
        self.window.title("Quizzler")

        self.window.config(padx=20, pady=20, bg=THEME_COLOR)

        self.score_label = Label(text=f"Score: {self.score}", fg="white", bg=THEME_COLOR)
        self.score_label.grid(row=0, column=1)

        self.canvas = Canvas(width=300, height=250,  bg="white")
        self.question_text = self.canvas.create_text(
            150,
            125,
            text="Question!",
            fill=THEME_COLOR,
            width=280,  # Omogoči prelamljanje vrstic
            justify="center",  # Poravna besedilo na sredino
            font=("Arial", 20, "italic")
        )
        self.canvas.grid(row=1, column=0, columnspan=2, pady=50)

        true_image = PhotoImage(file="images/true.png")
        self.true_button = Button(image=true_image, highlightthickness=0, command=lambda: self.click_for_true())
        self.true_button.grid(row=2, column=0)

        false_image = PhotoImage(file="images/false.png")
        self.false_button = Button(image=false_image, highlightthickness=0, command=lambda: self.click_for_false())
        self.false_button.grid(row=2, column=1)

        self.get_next_question() # to get the first question
        self.window.mainloop()

    def get_next_question(self):
        question = self.quiz.next_question()
        self.canvas.config(bg="white")
        self.canvas.itemconfig(self.question_text, text=question)

    def click_for_true(self):
        is_right = self.quiz.check_answer("True")
        self.give_feedback(is_right)
        if is_right:
            self.score += 1
            self.score_label.config(text=f"Score: {self.score}")


    def click_for_false(self):
        is_right = self.quiz.check_answer("False")
        self.give_feedback(is_right)
        if is_right:
            self.score += 1
            self.score_label.config(text=f"Score: {self.score}")


    def give_feedback(self, is_right):
        if is_right:
            self.canvas.config(bg="green")
        else:
            self.canvas.config(bg="red")

        self.window.after(1000, self.get_next_question)

