from html import unescape
from question_model import Question
from quiz_brain import QuizBrain
from quiz_data import QuizData


quiz_data = QuizData()
question_data = quiz_data.get_questions()

question_bank = []
for question in question_data:
    question_text = unescape(question["question"])
    question_answer = question["correct_answer"]
    new_question = Question(question_text, question_answer)
    question_bank.append(new_question)

quiz = QuizBrain(question_bank)

while quiz.still_has_questions():
    quiz.next_question()

print("You've completed the quiz")
print(f"Your final score was: {quiz.score}/{quiz.question_number}")
