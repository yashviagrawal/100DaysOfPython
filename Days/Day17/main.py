from question_model import Question
from data import question_data
from quiz_brain import Gameplay


question_bank=[]
for question in question_data:
    question_bank.append(Question(question["text"], question["answer"]))

game = Gameplay()
game.play(question_bank)