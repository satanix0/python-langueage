from tkinter import W
from data import question_data
from question_model import Question
from quiz_brain import QuizBrain
question_bank = []
for i in question_data:
    question_text = i["text"]
    question_ans = i["answer"]
    new_ques = Question(question_text, question_ans)
    question_bank.append(new_ques)

brain = QuizBrain(question_bank)
while brain.still_has_question():
    brain.nextQes()
print("You have completed the quiz")
print(f"Your Fianl Score is : {brain.score}/{brain.question_no}")
