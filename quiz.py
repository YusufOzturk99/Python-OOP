class Quiz:
    def __init__(self, question, choices, answer):
        self.question = question
        self.choices  = choices
        self.answer   = answer 
        print(f" Question: {question} \n Choices: {choices}")
    def checkAnswer(self, answer):
        return self.answer == answer

    
q1 = Quiz("What is the first letter of the alphabet ?", ["a","b","c","d"], "a")

print(q1.checkAnswer("a"))

