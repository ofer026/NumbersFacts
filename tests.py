import unittest
import tkinter as tk

class MyTestCase(unittest.TestCase):
    def test_something(self):
        hex_colors = {'green': '#73e600', 'blue':'#005ce6'}
        #self.assertEqual(True, False)
        #str = "vvgh"
        #int(str)
        #str += "gggg"
        #print(str)
        #str = input()
        #bool = "" == " "
        #bool = str == None
        #print(str)
        #print(bool)
        def change_frame():
            first_frame.place(x=40, y=80)
            second_frame.place_forget()
            n = entry.get()
            if n is not None:
                print('1')
            else:
                print('0')
        def change_frame2():
            second_frame.place(x=40, y=80)
            first_frame.place_forget()
        win = tk.Tk()
        win.geometry("800x800")
        first_frame = tk.Frame(height=80, width=60, bg=hex_colors['green'])
        first_frame.place(x=40, y=80)
        second_frame = tk.Frame(height=80, width=60, bg=hex_colors['blue'])
        second_frame.place(x=40, y=80)
        change_button = tk.Button(text='Change Frame to green', font=("Robto Light", 16), command=change_frame)
        change_button.place(x=480, y=80)
        change_button = tk.Button(text='Change Frame to blue', font=("Robto Light", 16), command=change_frame2)
        change_button.place(x=480, y=140)
        entry = tk.Entry()
        entry.place(x=40, y=200)
        win.mainloop()

if __name__ == '__main__':
    unittest.main()
