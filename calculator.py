import tkinter as tk
from tkinter import messagebox
#functions

def calculate_BMI():
    try:
        height_cm = float(height.get())
        weight_kg = float(weight.get())
        height_metres = height_cm / 100
        bmi = weight_kg / (height_metres ** 2)
        messagebox.showinfo("BMI Result", f"Your BMI is: {bmi:.2f}")
    except ValueError:
        messagebox.showerror("Invalid Input", "Please enter valid numeric values for height and weight.")

#window
window=tk.Tk()
window.geometry("600x500")
window.title("BMI calculator")

#bmi label
label=tk.Label(window, text="BMI Calculator", font=("Arial", 16))
label.place(x=225, y=0)

#height label
height_label=tk.Label(window,text="Please enter your height in cm:", font=("Helvetica", 12), fg="black", bd=2)
height_label.place(x=0, y=40)

#height entry
height=tk.Entry(window, bd=3)
height.place(x=225, y=40)

#weight label
weight_label=tk.Label(window,text="Please enter your weight in Kg:", font=("Helvetica", 12), fg="black", bd=2)
weight_label.place(x=0, y=80)

#weight entry
weight=tk.Entry(window, bg="white", fg="black", bd=3)
weight.place(x=225, y=80)

#images
bmi_image = tk.PhotoImage(file="image.png")
image_label = tk.Label(window, image=bmi_image)
image_label.place(x=50, y=120)
#button
calculate=tk.Button(window, text="Calculate", font=("Helvetica",12), fg="white", bg="green",command=calculate_BMI)
calculate.place(x=250,y=450)

window.mainloop()