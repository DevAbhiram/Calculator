from tkinter import *
#---------------backend
def Calculate(value):
    if value == "=":
        try:
            expression = Evaluate_area.get("1.0", END).strip()
            expression = expression.replace("÷", "/").replace("×", "*").replace("−", "-")
            result = eval(expression)
            Evaluate_area.delete("1.0", END)
            Evaluate_area.insert(END, result)
        except ZeroDivisionError:
            Evaluate_area.delete("1.0", END)
            Evaluate_area.insert(END, "Error: Division by zero")
        except Exception as e:
            Evaluate_area.delete("1.0", END)
            Evaluate_area.insert(END, f"Error: {str(e)}")
    elif value == "AC":
        Evaluate_area.delete("1.0", END)
    elif value == "⌫":
        current_text = Evaluate_area.get("1.0", END).strip()
        if current_text:  
            Evaluate_area.delete("end - 2 char", "end - 1 char")  
    else:
        Evaluate_area.insert(END, value)

# Front-End 
window = Tk()
window.geometry("300x400")
window.title("Abhiram's Calculator")
window.resizable(False, False)
icon = PhotoImage(file="C:/Users/balaj/OneDrive/Desktop/ABHIRAM/PYTHON/PROJECT/favicon.png")
window.iconphoto(True, icon)
window.configure(bg="#34aeeb")
Evaluate_area = Text(window,
                      fg="#515c61",
                      bg="white",
                      height=1.5,
                      width=12,
                      font=('Arial', 30))
Evaluate_area.grid(row=0, column=0, columnspan=4, pady=10, padx=11)

buttons = [
    'AC', '()', '%', '÷',
    '7', '8', '9', '×',
    '4', '5', '6', '−',
    '1', '2', '3', '+',
    '0', '.', '⌫', '='
]
row_value = 1
col_value = 0

for button in buttons:
    btn = Button(window,
                 text=button,
                 width=5,
                 height=2,
                 font=('Arial', 11),
                 fg="#050505",
                 bg="white",
                 command=lambda value=button: Calculate(value))
    btn.grid(row=row_value, column=col_value, padx=5, pady=5)  
    col_value += 1
    if col_value > 3:  
        col_value = 0
        row_value += 1

window.mainloop()
