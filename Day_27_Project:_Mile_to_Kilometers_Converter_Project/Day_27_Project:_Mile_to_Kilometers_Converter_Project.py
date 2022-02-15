from tkinter import *

window = Tk()
window.title("Mile to Km Conventer (By Emivvvvv)")
window.minsize(width=230, height=100)
window.config(padx=10, pady=10)

#Label
is_equal_to_label = Label(text="is equal to", font=("Arial", 12, "bold"))
is_equal_to_label.grid(column=0, row=1)
mile_to_km_label = Label(text="0", font=("Arial", 12, "bold"))
mile_to_km_label.grid(column=1, row=1)
mile_label = Label(text="mile", font=("Arial", 12, "bold"))
mile_label.grid(column=2, row=0)
km_label = Label(text="km", font=("Arial", 12, "bold"))
km_label.grid(column=2, row=1)

#Button
def mile_to_km_calculator():
    if input.get() == "":
        mile_to_km_label.config(text="SUS??")
    elif int(input.get()) > 0:
        new_mile = int(input.get())
        new_km = new_mile * 1.609
        mile_to_km_label.config(text=f"{new_km}")
    else:
        mile_to_km_label.config(text="Ah hell naw man ;((")



button = Button(text="Calculate", command=mile_to_km_calculator)
button.grid(column=1, row=2)

#Entry
input = Entry(width=10)
input.grid(column=1, row=0)

window.mainloop()

