import tkinter as tk
from test import get_data

# win = tk.Tk()
# win.geometry("800x800")
# win.title("Facts about numbers")

get_data.URL = "http://numbersapi.com/04/11/date"
print(get_data.get_info())

# win.mainloop()
