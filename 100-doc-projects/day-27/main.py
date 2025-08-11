import tkinter

window = tkinter.Tk()
window.title("My First GUI Program")
window.minsize(width=500, height=300)

#Label

my_lable = tkinter.Label(text="I am a Label", font=("Arial", 24, "bold"))
my_lable.pack(side="left")

my_lable["text"] = "New Text"
my_lable.config(text="New Text")

def button_clicked():
    print("I got clicked")
    newtext = input.get()
    my_lable.config(text="Button Clicked")

button = tkinter.Button(text="Click Me", command=button_clicked)

button.pack(side="right")

input = tkinter.Entry(width=10)
input.pack(side="bottom")
print(input.get())

window.mainloop()