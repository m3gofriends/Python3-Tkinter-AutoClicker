"""                                      
      First publication date : 2020 / 10 / 30
      Author : 張哲銘(Che-Ming Chang)
"""

import tkinter as tk
import tkinter.ttk as ttk
from pynput import keyboard
from pynput.mouse import Button, Controller

class AutoClicker:
    
    mouse_button_list = {
        0 : Button.left, 
        1 : Button.middle, 
        2 : Button.right
        }
    
    key_list = {
        0 : keyboard.Key.f1, 
        1 : keyboard.Key.f2, 
        2 : keyboard.Key.f3, 
        3 : keyboard.Key.f4, 
        4 : keyboard.Key.f5, 
        5 : keyboard.Key.f6, 
        6 : keyboard.Key.f7, 
        7 : keyboard.Key.f8, 
        8 : keyboard.Key.f9, 
        9 : keyboard.Key.f10, 
        10 : keyboard.Key.f11, 
        11 : keyboard.Key.f12
        }

    # Default value 
    break_loop = True
    time_interval = 1.0
    user_defined_mouse_button = Button.left
    user_defined_start = keyboard.Key.f1
    user_defined_stop = keyboard.Key.f2
    user_defined_end = keyboard.Key.f3

    def __init__(self, master):
        self.master = master
        master.title("AutoClicker")
        master.geometry(str(master.winfo_screenwidth() // 4) + 'x' + str(master.winfo_screenheight() // 3))
        
        self.time_frame = tk.Frame(master)
        self.time_frame.pack()
        
        self.mouse_button_frame = tk.Frame(master)
        self.mouse_button_frame.pack()
        
        self.top_frame = tk.Frame(master)
        self.top_frame.pack()
        
        self.middle_frame = tk.Frame(master)
        self.middle_frame.pack()
        
        self.bottom_frame = tk.Frame(master)
        self.bottom_frame.pack()

        self.label_time = ttk.Label(self.time_frame, text = "Time interval : 1.0(s)")
        self.label_time.grid(column = 1, row = 0)

        self.label_mouse_button = ttk.Label(self.mouse_button_frame, text = "Mouse button : Left")
        self.label_mouse_button.grid(column = 1, row = 0)

        self.label_start = ttk.Label(self.top_frame, text = "Start key : F1")
        self.label_start.grid(column = 1, row = 0)

        self.label_stop = ttk.Label(self.middle_frame, text = "Stop key : F2")
        self.label_stop.grid(column = 1, row = 0)

        self.label_end = ttk.Label(self.bottom_frame, text = "End key : F3")
        self.label_end.grid(column = 1, row = 0)

        self.time_string = tk.StringVar()
        self.time_string.set("1.0")
        tk.Entry(self.time_frame, textvariable = self.time_string, width = 18).grid(column = 1, row = 1)

        self.mouse_button_index = ttk.Combobox(self.mouse_button_frame, width = 15, textvariable = tk.StringVar(), state = "readonly")
        self.mouse_button_index['values'] = (Button.left, Button.middle, Button.right)
        self.mouse_button_index.grid(column = 1, row = 1)
        self.mouse_button_index.current(0)

        self.key_start_index = ttk.Combobox(self.top_frame, width = 15, textvariable = tk.StringVar(), state = "readonly")
        self.key_start_index['values'] = (keyboard.Key.f1, keyboard.Key.f2, keyboard.Key.f3, keyboard.Key.f4, keyboard.Key.f5, keyboard.Key.f6, keyboard.Key.f7, keyboard.Key.f8, keyboard.Key.f9, keyboard.Key.f10, keyboard.Key.f11, keyboard.Key.f12)
        self.key_start_index.grid(column = 1, row = 1)
        self.key_start_index.current(0)

        self.key_stop_index = ttk.Combobox(self.middle_frame, width = 15, textvariable = tk.StringVar(), state = "readonly")
        self.key_stop_index['values'] = (keyboard.Key.f1, keyboard.Key.f2, keyboard.Key.f3, keyboard.Key.f4, keyboard.Key.f5, keyboard.Key.f6, keyboard.Key.f7, keyboard.Key.f8, keyboard.Key.f9, keyboard.Key.f10, keyboard.Key.f11, keyboard.Key.f12)
        self.key_stop_index.grid(column = 1, row = 1)
        self.key_stop_index.current(1)

        self.key_end_index = ttk.Combobox(self.bottom_frame, width = 15, textvariable = tk.StringVar(), state = "readonly")
        self.key_end_index['values'] = (keyboard.Key.f1, keyboard.Key.f2, keyboard.Key.f3, keyboard.Key.f4, keyboard.Key.f5, keyboard.Key.f6, keyboard.Key.f7, keyboard.Key.f8, keyboard.Key.f9, keyboard.Key.f10, keyboard.Key.f11, keyboard.Key.f12)
        self.key_end_index.grid(column = 1, row = 1)
        self.key_end_index.current(2)

        ttk.Button(self.time_frame, text = "Set", command = self.set_time).grid(column = 2, row = 1)
        ttk.Button(self.mouse_button_frame, text = "Set", command = self.set_mouse_button).grid(column = 2, row = 1)
        ttk.Button(self.top_frame, text = "Set", command = self.key_list_start).grid(column = 2, row = 1)
        ttk.Button(self.middle_frame, text = "Set", command = self.key_list_stop).grid(column = 2, row = 1)
        ttk.Button(self.bottom_frame, text = "Set", command = self.key_list_end).grid(column = 2, row = 1)

        self.mouse = Controller()
        
        self.key_listener = keyboard.Listener(on_press = self.on_press)
        self.key_listener.start()      

    def click_loop(self):
        if self.break_loop == False:
            self.mouse.press(self.user_defined_mouse_button)
            self.mouse.release(self.user_defined_mouse_button)
            self.master.after(int(self.time_interval * 1000), self.click_loop)

    def on_press(self, key):
        if key == self.user_defined_start and self.break_loop:
            self.break_loop = False
            self.click_loop()
        if key == self.user_defined_stop and self.break_loop == False:
            self.break_loop = True
        if key == self.user_defined_end:
            self.master.destroy()

    def set_time(self):
        try:
            if float(self.time_string.get()) <= 0:
                return
            self.time_interval = float(self.time_string.get())
        except:
            return
        self.label_time.config(text = "Time interval : " + self.time_string.get() + "(s)")

    def set_mouse_button(self):
        self.user_defined_mouse_button = self.mouse_button_list.get(self.mouse_button_index.current(), None)
        self.label_mouse_button.config(text = "Mouse button : " + str(self.user_defined_mouse_button).replace('Button.', '').title())

    def key_list_start(self):
        temp_key = self.user_defined_start
        self.label_start.config(text = "Start key : F" + str(self.key_start_index.current() + 1))
        self.user_defined_start = self.key_list.get(self.key_start_index.current(), None)
        if self.user_defined_start == self.user_defined_stop or self.user_defined_start == self.user_defined_end:
            if self.user_defined_start == self.user_defined_stop:
                num = ''.join([x for x in str(temp_key) if x.isdigit()])
                self.label_stop.config(text = "Stop key : F" + num)
                self.key_stop_index.current(int(num) - 1)
                self.user_defined_stop = temp_key
            else:
                num = ''.join([x for x in str(temp_key) if x.isdigit()])
                self.label_end.config(text = "End key : F" + num)
                self.key_end_index.current(int(num) - 1)
                self.user_defined_end = temp_key
        
    def key_list_stop(self):
        temp_key = self.user_defined_stop
        self.label_stop.config(text = "Stop key : F" + str(self.key_stop_index.current() + 1))
        self.user_defined_stop = self.key_list.get(self.key_stop_index.current(), None)
        if self.user_defined_stop == self.user_defined_start or self.user_defined_stop == self.user_defined_end:
            if self.user_defined_stop == self.user_defined_start:
                num = ''.join([x for x in str(temp_key) if x.isdigit()])
                self.label_start.config(text = "Start key : F" + num)
                self.key_start_index.current(int(num) - 1)
                self.user_defined_start = temp_key   
            else:
                num = ''.join([x for x in str(temp_key) if x.isdigit()])
                self.label_end.config(text = "End key : F" + num)
                self.key_end_index.current(int(num) - 1)
                self.user_defined_end = temp_key

    def key_list_end(self):
        temp_key = self.user_defined_end
        self.label_end.config(text = "End key : F" + str(self.key_end_index.current() + 1))
        self.user_defined_end = self.key_list.get(self.key_end_index.current(), None)  
        if self.user_defined_end == self.user_defined_start or self.user_defined_end == self.user_defined_stop:
            if self.user_defined_end == self.user_defined_start:
                num = ''.join([x for x in str(temp_key) if x.isdigit()])
                self.label_start.config(text = "Start key : F" + num)
                self.key_start_index.current(int(num) - 1)
                self.user_defined_start = temp_key   
            else:
                num = ''.join([x for x in str(temp_key) if x.isdigit()])
                self.label_stop.config(text = "Stop key : F" + num)
                self.key_stop_index.current(int(num) - 1)
                self.user_defined_stop = temp_key
    
if __name__ == '__main__':
    root = tk.Tk()
    AutoClicker(root)
    root.mainloop()
