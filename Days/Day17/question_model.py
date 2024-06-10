class Question:
    def __init__(self, text, answer):
        self.text = text
        self.answer = answer

    def check(self, choice):
        if self.answer == choice:
            return True
        else:
            return False
