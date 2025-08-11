from tkinter import *

window = Tk()
window.title("Mile to Kilometer Converter")

miles_input = Entry(width=10)
miles_input.grid(column=1, row=0)


miles_label = Label(text="Miles")
miles_label.grid(column=2, row=0)


is_equal_label = Label(text="is equal to")
is_equal_label.grid(column=0, row=1)

kilometers_result_label = Label(text="0")
kilometers_result_label.grid(column=1, row=1)


kilometers_label = Label(text="Kilometers")
kilometers_label.grid(column=2, row=1)


calculate = Button(text="Calculate", command=lambda: kilometers_result_label.config(text=str(float(miles_input.get()) * 1.60934)))
calculate.grid(column=1, row=2)

window.mainloop()