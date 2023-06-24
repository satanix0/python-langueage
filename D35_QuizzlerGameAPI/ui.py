from tkinter import *
from quiz_brain import QuizBrain
THEME_COLOR = "#375362"


class UI:
    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain
        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)

        self.score_label = Label(
            text=f"scrore: {0}", bg=THEME_COLOR, fg="white")
        self.score_label.grid(row=0, column=1)

        self.text_canvas = Canvas(width=300, height=250, bg="white")
        self.text = self.text_canvas.create_text(
            150, 125,       # canvas size has to be provided
            width=250,      # width has to be set tof makethe question fit into canvas
            text="some text",
            fill=THEME_COLOR,
            font="Arial 20 italic"
        )

        self.text_canvas.grid(row=1, column=0, columnspan=2, pady=20)

        true_img = PhotoImage(
            file="Projects/D35_QuizzlerGameAPI/images/true.png")
        self.corr_btn = Button(
            image=true_img, highlightthickness=0, command=self.true_pressed)
        self.corr_btn.grid(row=2, column=0)

        false_img = PhotoImage(
            file="Projects/D35_QuizzlerGameAPI/images/false.png")
        self.incorr_btn = Button(
            image=false_img, highlightthickness=0, command=self.false_pressed)
        self.incorr_btn.grid(row=2, column=1)
        self.get_next_question()

        self.window.mainloop()

    def get_next_question(self):
        self.text_canvas.config(bg='white')  # keeps the canvas bg as white

        # check if still question left in the list
        if self.quiz.still_has_questions():
            self.score_label.config(text=f"Score: {self.quiz.score}")
            que = self.quiz.next_question()
            self.text_canvas.itemconfig(self.text, text=que)
        else:
            self.text_canvas.itemconfig(
                self.text, text="You've reached to the end of the quiz")

            # disables the buttons after end of the quiz
            self.corr_btn.itemconfig(state="disabled")
            self.incorr_btn.itemconfig(state="disabled")

    def true_pressed(self):
        self.give_feedback(self.quiz.check_answer(user_answer="True"))

    def false_pressed(self):
        is_right = self.quiz.check_answer(user_answer="False")
        self.give_feedback(is_right)

    def give_feedback(self, is_right):
        if is_right:
            self.text_canvas.config(bg='green')
        else:
            self.text_canvas.config(bg='red')

        # Changes background color for 1 sec and then func gets called
        self.window.after(1000, func=self.get_next_question)
