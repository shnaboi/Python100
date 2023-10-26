from question_model import Question
from data import question_data, question_data_2, question_data_3
from quiz_brain import QuizBrain

question_bank = []

for q in question_data_3:
  var = Question(q["question"], q['correct_answer'])
  question_bank.append(var)

#   var is a class from the Question constructor, with q and a attributes, which is then appended to the qbank

quiz = QuizBrain(question_bank)

while quiz.still_has_questions():
  quiz.next_question()
