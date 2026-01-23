
class QuizBrain:
    def __init__(self, question_list):
        self.questionNumber = 0
        self.question_list = question_list

    def next_question(self):
        new_question = self.question_list[self.questionNumber]
        self.questionNumber +=1
        return input(f"Q.{self.questionNumber}: {new_question.question} (True/False): ").lower()

    def still_has_question(self):
        return self.questionNumber < len(self.question_list)

    def get_answer(self):
        return self.question_list[self.questionNumber-1].answer