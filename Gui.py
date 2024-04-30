import tkinter as tk
from tkinter import ttk, messagebox
import loan_calculator


base_cost = 15000
interest_rate = 0.05  
admin_cost = 500

def calculate_cost():
    num_years = years_var.get()
    if num_years.isdigit() and int(num_years) in range(1, 6):
        num_years = int(num_years)
        total_cost = loan_calculator.calculate_total_cost(base_cost, interest_rate, admin_cost, num_years)
        result_label.config(text=f"If paid off over {num_years} year(s): R{total_cost:.2f}")
    else:
        messagebox.showerror("Invalid Input", "Please enter a number between 1 and 5 for the number of years.")

def reset_fields():
    years_var.set("")
    result_label.config(text="")

def update_values():
    global base_cost, interest_rate, admin_cost
    try:
        base_cost = int(base_cost_var.get())
        interest_rate = float(interest_rate_var.get()) / 100
        admin_cost = int(admin_cost_var.get())
        base_cost_label.config(text=f"Base cost of the laptop: R{base_cost}")
        interest_rate_label.config(text=f"Interest rate: {interest_rate * 100}%")
        admin_cost_label.config(text=f"Administrative cost: R{admin_cost}")
    except ValueError:
        messagebox.showerror("Invalid Input", "Please enter valid numeric values.")

root = tk.Tk()
root.title("Loan Calculator")

input_frame = ttk.Frame(root, padding=10)
input_frame.grid(row=0, column=0, sticky="nsew")

result_frame = ttk.Frame(root, padding=10)
result_frame.grid(row=1, column=0, sticky="nsew")

years_label = ttk.Label(input_frame, text="Enter the number of years (1 to 5):")
years_label.grid(row=0, column=0, sticky="w")

years_var = tk.StringVar()
years_entry = ttk.Entry(input_frame, textvariable=years_var)
years_entry.grid(row=0, column=1, sticky="w")

calculate_button = ttk.Button(input_frame, text="Calculate", command=calculate_cost)
calculate_button.grid(row=0, column=2, sticky="w")

reset_button = ttk.Button(input_frame, text="Reset", command=reset_fields)
reset_button.grid(row=0, column=3, sticky="w")

base_cost_var = tk.StringVar(value=str(base_cost))
base_cost_entry = ttk.Entry(input_frame, textvariable=base_cost_var)
base_cost_entry.grid(row=1, column=0, sticky="w")

interest_rate_var = tk.StringVar(value=str(interest_rate * 100))
interest_rate_entry = ttk.Entry(input_frame, textvariable=interest_rate_var)
interest_rate_entry.grid(row=1, column=1, sticky="w")

admin_cost_var = tk.StringVar(value=str(admin_cost))
admin_cost_entry = ttk.Entry(input_frame, textvariable=admin_cost_var)
admin_cost_entry.grid(row=1, column=2, sticky="w")

update_button = ttk.Button(input_frame, text="Update Values", command=update_values)
update_button.grid(row=1, column=3, sticky="w")

result_label = ttk.Label(result_frame, text="")
result_label.grid(row=0, column=0, sticky="w")

base_cost_label = ttk.Label(root, text=f"Base cost of the laptop: R{base_cost}")
base_cost_label.grid(row=2, column=0, sticky="w")

interest_rate_label = ttk.Label(root, text=f"Interest rate: {interest_rate * 100}%")
interest_rate_label.grid(row=3, column=0, sticky="w")

admin_cost_label = ttk.Label(root, text=f"Administrative cost: R{admin_cost}")
admin_cost_label.grid(row=4, column=0, sticky="w")

root.mainloop()