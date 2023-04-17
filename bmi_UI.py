import tkinter as tk

# create a function to calculate the BMI and display the result
def calculate_bmi():
    height = float(height_entry.get()) / 100
    weight = float(weight_entry.get())
    bmi = weight / (height ** 2)
    result_label.config(text=f"Your BMI is {bmi:.2f}")
    
    # determine the weight status based on the BMI
    if bmi < 18.5:
        status_label.config(text="You are underweight")
    elif bmi < 25:
        status_label.config(text="You are normal weight")
    elif bmi < 30:
        status_label.config(text="You are overweight")
    else:
        status_label.config(text="You are obese")

# create the main window
root = tk.Tk()
root.title("BMI Calculator")

# create the labels and entry boxes for height and weight
height_label = tk.Label(root, text="Height (cm):")
height_label.pack()
height_entry = tk.Entry(root)
height_entry.pack()

weight_label = tk.Label(root, text="Weight (kg):")
weight_label.pack()
weight_entry = tk.Entry(root)
weight_entry.pack()

# create a button to calculate the BMI
calculate_button = tk.Button(root, text="Calculate BMI", command=calculate_bmi)
calculate_button.pack()

# create labels to display the BMI result and weight status
result_label = tk.Label(root)
result_label.pack()

status_label = tk.Label(root)
status_label.pack()

# start the main loop
root.mainloop()
