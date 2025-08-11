from tkinter import * 



# ---------------------------- CONSTANTS ------------------------------- #


PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
timer = None

# ---------------------------- TIMER RESET ------------------------------- # 

def reset_timer():
    window.after_cancel(timer)  # Cancel the current timer if it exists
    canvas.itemconfig(timer_text, text="00:00")  # Reset the timer display
    title_label.config(text="Timer", fg=GREEN)  # Reset the title label
    check_maraks.config(text="")  # Reset the check marks
    global reps
    reps = 0 
    

# ---------------------------- TIMER MECHANISM ------------------------------- # 

def start_timer():
    global reps
    reps += 1
    
    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60
    
    if reps % 8 == 0:
        # Long break
        count_down(long_break_sec)
        title_label.config(text="Break", fg=RED)
        
    elif reps % 2 == 0:
        # Short break
        count_down(short_break_sec)
        title_label.config(text="Break", fg=PINK)
        
    else:
        count_down(work_sec)
        title_label.config(text="Work", fg=GREEN)
    
    
    count_down(25 * 60)  # Start countdown from 25 minutes
    

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 

def count_down(count):
    """Counts down from the given count."""
    minutes = count // 60
    seconds = count % 60
    if seconds < 10:
        seconds = f"0{seconds}"
    canvas.itemconfig(timer_text, text=f"{minutes}:{seconds}")
        
    if count > 0:
        global timer
        timer =  window.after(1000, count_down, count - 1)
    else:
        start_timer()  # Automatically start the next timer
        print("Timer finished!")  # Placeholder for timer end action
        
        work_sessions = reps // 2
        
        for _ in range(work_sessions):
            check_maraks.config(text=check_maraks.cget("text") + "✔")
        check_marks.config(text="")  # Reset check marks after each session
        
        

# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)


title_label = Label(text="Timer", fg=GREEN, bg=YELLOW, font=(FONT_NAME, 35, "bold"))
title_label.grid(column=1, row=0)

canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=tomato_img)
timer_text = canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"), tag="timer")

canvas.grid(column=1, row=1)

start_button = Button(text="Start", highlightthickness=0, command=start_timer)
start_button.grid(column=0, row=2)

reset_button = Button(text="Reset", highlightthickness=0, command=reset_timer)
reset_button.grid(column=2, row=2)

check_maraks = Label(text="✔", fg=GREEN, bg=YELLOW, font=(FONT_NAME, 12, "bold"))
check_maraks.grid(column=1, row=3)

window.mainloop()
