class Question:
    def __init__(self, text, choices, answer):
        self.text = text
        self.choices = choices
        self.answer = answer

    def checkAnswer(self, answer):
        return self.answer == answer    

class Quiz:
    def __init__(self, questions):
        self.questions = questions
        self.score = 0
        self.questionIndex = 0

    def getQuestion(self):
        return self.questions[self.questionIndex]
    
    def displayQuestion(self):
        question = self.getQuestion()
        print(f'Question {self.questionIndex + 1} : {question.text}')

        for q in question.choices:
            print("-" + q)
    
        answer = input("Answer: ")
        print(question.checkAnswer(answer))

        self.guess(answer)
        self.loadQuestion()

    def guess(self, answer):
        question = self.getQuestion()

        if question.checkAnswer(answer):
            self.score += 1
        self.questionIndex += 1
        
    
    def loadQuestion(self):
        if len(questions) == self.questionIndex:
            self.showScore()
        else:
            self.displayProgress()
            self.displayQuestion()

    def showScore(self):
        print(f"score: {self.score}")

    def displayProgress(self):
        totalQuestion = len(self.questions)
        questionNumber = self.questionIndex + 1

        if (questionNumber > totalQuestion):
            print("Quiz is finished")
        else: 
            print(f'question {questionNumber} of {totalQuestion}'.center(100,'*'))

q1 = Question("What is the most Popular programming Language ?", ["Python", "Java", "C++"], "Python")
q2 = Question("Which is the Faster programming Language ?", ["Python", "Java", "C++"], "Python")
q3 = Question("Which is the Oldest programming Language ?", ["Python", "Java", "C"], "C")

questions = [q1, q2, q3]

quiz = Quiz(questions)

quiz.loadQuestion()