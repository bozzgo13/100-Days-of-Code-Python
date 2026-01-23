from   question_model import Question
from data import question_data
from quiz_brain import QuizBrain

question_bank =[]

for question in question_data:
    question_bank.append(Question(question["text"], question["answer"]))

points = 0

brain = QuizBrain(question_bank)

while brain.still_has_question():
    answer = brain.next_question()
    if answer == brain.get_answer().lower():
        points += 1
        print(f"Correct! {points}/{brain.questionNumber}")
    else:
        print(f"Wrong! Correct answer: {brain.get_answer()}")