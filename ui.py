from tkinter import *
from quiz_brain import QuizBrain
THEME_COLOR = "#375362"
cross=r"C:\Users\ishas\PycharmProjects\day-34\day-34\quizzler-app-start\images\false.png"
tick=r"C:\Users\ishas\PycharmProjects\day-34\day-34\quizzler-app-start\images\true.png"
class QuizInterface:
    def __init__(self,quiz_brain:QuizBrain):
        self.quiz=quiz_brain
        self.window=Tk()
        self.window.title("Quizzler")
        self.window.config(padx=20,pady=20)
        self.window.config(bg=THEME_COLOR)
        self.my_label=(Label(text="Score:",fg="white",bg=THEME_COLOR))
        self.my_label.grid(column=1,row=0)
        self.canvas=Canvas(height=250,width=300)

        self.question_text=self.canvas.create_text(150,
                                                   125,
                                                   text="Some Question text",
                                                   fill=THEME_COLOR,
                                                   width=280,
                                                   font=("Arial",20,"italic"))
        self.canvas.grid(column=0,row=1,columnspan=2,pady=50)


        cross_image=PhotoImage(file=cross)
        self.cross=(Button(image=cross_image,highlightthickness=0,command=self.false_pressed))
        self.cross.grid(column=1,row=2)
        self.cross.config(pady=20,padx=20)


        tick_image=PhotoImage(file=tick)
        self.tick=Button(image=tick_image,highlightthickness=0,command=self.true_pressed)
        self.tick.grid(column=0,row=2)
        self.tick.config(padx=20,pady=20)
        self.get_next_question()
        self.window.mainloop()
    def get_next_question(self):
        self.canvas.config(bg="white")
        if self.quiz.still_has_questions():

            self.my_label.config(text=f"Score: {self.quiz.score}")
            q_text=self.quiz.next_question()
            self.canvas.itemconfig(self.question_text,text=q_text)
        else:
            self.canvas.itemconfig(self.question_text,text="You have reached the end of the quiz.")
            self.tick.config(state="disabled")
            self.cross.config(state="disabled")

    def true_pressed(self):
        is_right=self.quiz.check_answer("True")
        self.give_feedback(is_right)
    def false_pressed(self):
        is_right=self.quiz.check_answer("False")
        self.give_feedback(is_right)
    def give_feedback(self,is_right):
        if is_right:
            self.canvas.config(bg="green")
        else:
            self.canvas.config(bg="red")
        self.window.after(1000, self.get_next_question)





