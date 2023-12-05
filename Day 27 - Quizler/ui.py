THEME_COLOR = "#375362"
from tkinter import *
from quiz_brain import QuizBrain
import html

game_on=True

class UI_Interface:
    def true_func(self):
        global game_on
        if game_on==False:
            return 0
        self.get_next_question()
        if self.quiz.current_question.answer=='True':
            self.score=self.score+1
            self.score_label.destroy()
            self.score_label=Label(text='Score: '+str(self.score),font=('Arial',20,'normal'))
            self.score_label.grid(column=0,row=0)



    def false_func(self):
        global game_on
        if game_on == False:
            return 0
        self.get_next_question()
        if self.quiz.current_question.answer == 'False':
            self.score = self.score + 1
            self.score_label.destroy()
            self.score_label = Label(text='Score: ' + str(self.score), font=('Arial', 20, 'normal'))
            self.score_label.grid(column=0, row=0)

    def __init__(self,quiz: QuizBrain):
        self.quiz=quiz
        self.quiz.next_question()
        self.screen=Tk()
        self.screen.title('Quizzler')
        self.screen.config(padx=20,pady=20)

        self.canvas=Canvas(width=250,height=250,bg='yellow')
        self.canvas_question = self.canvas.create_text(125, 125, width=200, justify='center',
                                                       font=('Arial', 15, 'normal'),
                                                       text=html.unescape(self.quiz.current_question.text))

        self.True_photo=PhotoImage(file='images/true.png')
        self.TrueButton=Button(self.screen,width=100,height=97,image=self.True_photo,command=self.true_func)
        self.TrueButton.grid(column=0,row=2)

        self.False_photo=PhotoImage(file='images/false.png')
        self.FalseButton=Button(self.screen,width=100,height=97,image=self.False_photo,command=self.false_func)
        self.FalseButton.grid(column=1,row=2)

        self.canvas.grid(row=1,column=0,columnspan=2,pady=20)

        self.score=0
        self.score_label=Label(text='Score: '+str(self.score),font=('Arial',20,'normal'))
        self.score_label.grid(column=0,row=0)




        self.screen.mainloop()

    def get_next_question(self):
        global game_on
        if self.quiz.question_number<10:

            self.quiz.next_question()
            self.canvas.delete(self.canvas_question)
            self.canvas_question=self.canvas.create_text(125, 125, width=200, justify='center', font=('Arial', 15, 'normal'),
                                    text=html.unescape(self.quiz.current_question.text))

        else:
            game_on=False
            self.canvas.delete(self.canvas_question)
            self.canvas_question = self.canvas.create_text(125, 125, width=200, justify='center',
                                                           font=('Arial', 15, 'normal'),
                                                           text='You finished the quiz!')



