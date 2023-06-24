import re


class QuizBrain:
    def __init__(self, q_list):
        self.question_no = 0
        self.question_list = q_list
        self.score = 0

    def still_has_question(self):

        return self.question_no < len(self.question_list)

    def nextQes(self):
        curr_ques = self.question_list[self.question_no]
        self.question_no += 1
        user_ans = input(
            f"Q.{self.question_no} {curr_ques.text} (True/False) : ").lower()
        self.check_ans(user_ans, curr_ques.answer)

    def check_ans(self, u_ans, curr_ans):
        if u_ans.lower() == curr_ans.lower():
            self.score += 1
            print("You got the right answer")
        else:
            print("Wrong answer")
        print(f"Correct answer is {curr_ans}")
        print(f"Your Current Score is {self.score}/{self.question_no}")
        print("\n")