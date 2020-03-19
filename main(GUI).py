import tkinter as tk
import pyautogui
from bs4 import BeautifulSoup
import requests

headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) "
                         "Chrome/76.0.3809.132 Safari/537.36 OPR/63.0.3368.57756"}
num = 4

def get_fact():
    if num == 1:
        day = num_date_day_entry.get()
        month = num_date_month_entry.get()
        try:
            int(day)
            int(month)
        except ValueError:
            if day.lower() == "random" or month.lower() == "random":
                URL = "http://numbersapi.com/random/date"
            else:
                pyautogui.alert(text="Make Sure that both fields have a whole number in them")
                return
        else:
            if int(day) >= 32 or int(day) <= 0:
                pyautogui.alert(text="make sure that the number you put in the day field is between 1 and 31")
                return
            if int(month) >= 13 or int(month) <= 0:
                pyautogui.alert(text="make sure that the number you put in the month field is between 1 and 12")
                return
            # TODO add an option to write 'random'
            URL = "http://numbersapi.com/" + month + "/" + day + "/date"
    elif num == 2:
        year = num_entry.get()
        try:
            int(year)
        except ValueError:
            if year.lower() == "random":
                URL = "http://numbersapi.com/random/year"
            else:
                pyautogui.alert(text='Make sure that the field have a whole number in it')
                return
        else:
            URL = "http://numbersapi.com/" + year + "/year"
    elif num == 3:
        math_num = num_entry.get()
        try:
            int(math_num)
        except ValueError:
            if math_num.lower() == "random":
                URL = "http://numbersapi.com/random/math"
            else:
                pyautogui.alert(text='Make sure that the field have a whole number in it')
                return
        else:
            URL = "http://numbersapi.com/" + math_num + "/math"
    elif num == 4:
        number = num_entry.get()
        try:
            int(number)
        except ValueError:
            if number.lower() == "random":
                URL = "http://numbersapi.com/random"
            else:
                pyautogui.alert(text='Make sure that the field have a whole number in it')
                return
        else:
            URL = "http://numbersapi.com/" + number
    page = requests.get(URL, headers=headers)
    soup = BeautifulSoup(page.content, 'html.parser')
    info_text_info.delete('1.0', 'end')
    info_text_info.insert('1.0', soup)


def sett(number):
    global num
    num = number
    if number == 1:
        num_entry_label.place_forget()
        num_entry.place_forget()
        global num_date_day_entry_label
        global num_date_day_entry
        global num_date_month_entry_label
        global num_date_month_entry
        num_date_day_entry_label = tk.Label(text="Enter a Day: ", font=("Roboto Light", 16))
        num_date_day_entry_label.place(x=40, y=60)
        num_date_day_entry = tk.Entry(font=("Roboto Light", 12))
        num_date_day_entry.place(x=158, y=64)
        num_date_month_entry_label = tk.Label(text="Enter a Month: ", font=("Roboto Light", 16))
        num_date_month_entry_label.place(x=40, y=90)
        num_date_month_entry = tk.Entry(font=("Roboto Light", 12))
        num_date_month_entry.place(x=188, y=94)
    else:
        try:
            num_date_day_entry_label.place_forget()
            num_date_day_entry.place_forget()
            num_date_month_entry_label.place_forget()
            num_date_month_entry.place_forget()
        except NameError:
            pass
        finally:
            num_entry_label.place(x=40, y=60)
            num_entry.place(x=198, y=64)


win = tk.Tk()
win.title("Numbers Facts")
win.geometry("800x800")
win.iconbitmap('D:\\OFER\\Python\\Projects\\numbers_facts(api)\\Icons\\numbers_window_icon.ico')

var = tk.IntVar()
# --------- LABELS ----------
num_entry_label = tk.Label(text="Enter a Number: ", font=("Roboto Light", 16))
num_entry_label.place(x=40, y=60)
# ---------- Entry -----------
num_entry = tk.Entry(font=("Roboto Light", 12))
num_entry.place(x=198, y=64)
# --------- Radio Buttons ---------
radio_date = tk.Radiobutton(text="Date", font=("Roboto Light", 14), variable=var, value=1, command=lambda: sett(1))
radio_date.place(x=40, y=360)
radio_date.deselect()
radio_year = tk.Radiobutton(text="Year", font=("Roboto Light", 14), variable=var, value=2, command=lambda: sett(2))
radio_year.place(x=40, y=400)
radio_math = tk.Radiobutton(text="Math", font=("Roboto Light", 14), variable=var, value=3, command=lambda: sett(3))
radio_math.place(x=40, y=440)
radio_trivia = tk.Radiobutton(text="Trivia", font=("Roboto Light", 14), variable=var, value=4, command=lambda: sett(4))
radio_trivia.place(x=40, y=480)
radio_trivia.select()
# ------------ Buttons ------------
get_info_button = tk.Button(text="Get a Fact", font=("Roboto Light", 12), height=4, width=14, command=get_fact)
get_info_button.place(x=560, y=140)
# ------------ Text Box ----------
info_text_info = tk.Text(font=("Roboto Light", 11), height=20, width=34)
info_text_info.place(x=500, y=240)
win.mainloop()
