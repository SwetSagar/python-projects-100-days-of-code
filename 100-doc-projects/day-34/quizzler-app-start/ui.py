THEME_COLOR = "#375362"

class QuizInterface :
    
    def __init__(self):
        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)
        self.canvas = Canvas(width=300, height=250, bg="white")
        
        self.score_label = Label(text="Score: 0", fg="white", bg=THEME_COLOR)
        self.score_label.grid(column=1, row=0)
        self.canvas.grid(column=0, row=1, columnspan=2)
        
        self.question_text = self.canvas.create_text(text="Some Question Text",fill="THEME_COLOR", font=("Arial", 20, "italic"), width=280)
        self.canvas.grid(column=0, row=1, columnspan=2)
        
        true_image = PhotoImage(file="images/true.png")
        self.true_button = Button(image=true_image, highlightthickness=0, command=self.true_pressed)
        self.true_button.grid(column=0, row=2)
        
        false_image = PhotoImage(file="images/false.png")
        self.false_button = Button(image=false_image, highlightthickness=0, command=self.false_pressed)
        self.false_button.grid(column=1, row=2)
        
        self.window.mainloop()
        
    def get_next_question(self):
        # This method should be implemented to fetch the next question
        q_text = self.quiz.current_question.text    
        self.canvas.itemconfig(self.question_text, text=q_text)
        
    def true_pressed(self):
        self.quiz.check_answer("True")
        self.get_next_question()
        
    def false_pressed(self):
        self.quiz.check_answer("False")
        self.get_next_question()