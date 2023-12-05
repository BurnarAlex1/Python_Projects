class Player:
    def __init__(self):
        self.score=0
        self.questions_answered=0

    def correct_answer(self):
        self.score+=1
        self.questions_answered+=1

    def wrong_answer(self):
        self.questions_answered+=1