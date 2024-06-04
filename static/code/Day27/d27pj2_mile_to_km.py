# import tkinter
from tkinter import *


window = Tk()
window.title("Mile to Km Converter")
window.minsize(width=300, height=150)
window.config(padx=50, pady=50)

def scale_used(value):
    # return value
    miles = value
    result = round(float(miles) * 1.609344, 2)
    label_result.config(text=result)
# Scale
scale = Scale(from_=0, to=100, command=scale_used, orient=HORIZONTAL, length=500)
scale.grid(column=1, row=0)

# Label Miles
label_miles = Label(text="Miles", font=("Arial", 10, "normal"))
label_miles.grid(column=2, row=0)

# Label is equal to
label_equal = Label(text="is equal to", font=("Arial", 10, "normal"))
label_equal.grid(column=0, row=1)

# Label result
# result = str(0)
label_result = Label(text="0", font=("Arial", 10, "normal"))
label_result.grid(column=1, row=1)

# Label Km
label_km = Label(text="Km", font=("Arial", 10, "normal"))
label_km.grid(column=2, row=1)



window.mainloop()
