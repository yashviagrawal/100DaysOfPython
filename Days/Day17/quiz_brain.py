from data import question_data
import random


class Gameplay:
    def __init__(self):
        self.current_question = 0
        self.total_question = len(question_data)

    def printStuff(self, question_bank):
        print(f"{self.current_question + 1}. {question_bank[self.order[self.current_question]].text} (True/False): ")

    def play(self, question_bank):
        random.shuffle(question_bank)
        while self.current_question < self.total_question:
            # print(f"Right answer {question_bank[self.current_question].answer}")
            choice = bool(int(input(f"{self.current_question + 1}. {question_bank[self.current_question].text} (1/0): ")))
            if question_bank[self.current_question].check(choice):
                print("Well Done!\n")
                self.current_question += 1
            else:
                # print(f"Right answer {question_bank[self.current_question].answer}, user answer {choice}")
                print(f"Oops Game Over, Total points {self.current_question * 10}\n")
                break