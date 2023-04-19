import tkinter as tk

# create the main window
root = tk.Tk()
root.title("Traffic Signal System")

# initialize variables
num_cars_a = 0
num_cars_b = 0
status_a = "GREEN"
status_b = "RED"

# create the widgets
label_a = tk.Label(root, text="Signal A: " + str(num_cars_a) + " cars passed", font=("Arial", 80))
label_b = tk.Label(root, text="Signal B: " + str(num_cars_b) + " cars passed", font=("Arial", 80))
label_status_a = tk.Label(root, text="Signal A is " + status_a, font=("Arial", 80), fg="green")
label_status_b = tk.Label(root, text="Signal B is " + status_b, font=("Arial", 80), fg="red")

# create the button event handlers
def add_car_a():
    global num_cars_a, status_a, status_b
    num_cars_a += 1
    label_a.config(text="Signal A: " + str(num_cars_a) + " cars passed")
    if num_cars_a > 1:
        status_a = "GREEN"
        status_b = "RED"
        label_status_a.config(text="Signal A is " + status_a, fg="green")
        label_status_b.config(text="Signal B is " + status_b, fg="red")

def add_car_b():
    global num_cars_b, status_a, status_b
    num_cars_b += 1
    label_b.config(text="Signal B: " + str(num_cars_b) + " cars passed")
    if num_cars_b > 1:
        status_a = "RED"
        status_b = "GREEN"
        label_status_a.config(text="Signal A is " + status_a, fg="red")
        label_status_b.config(text="Signal B is " + status_b, fg="green")

# create the buttons
button_a = tk.Button(root, text="Add Car to Signal A", font=("Arial", 80), command=add_car_a)
button_b = tk.Button(root, text="Add Car to Signal B", font=("Arial", 80), command=add_car_b)

# display the widgets
label_a.pack()
label_b.pack()
label_status_a.pack()
label_status_b.pack()
button_a.pack()
button_b.pack()

# start the main event loop
root.mainloop()
