import tkinter as tk
import tkinter.ttk as ttk
from pynput import keyboard
from pynput.mouse import Button, Controller

root = tk.Tk()
root.title('AutoClicker')
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
root.geometry(str(int(screen_width/4))+'x'+str(int(screen_height/3)))

time_frame = tk.Frame(root)
time_frame.pack()

mouse_button_frame = tk.Frame(root)
mouse_button_frame.pack()

top_frame = tk.Frame(root)
top_frame.pack()

middle_frame = tk.Frame(root)
middle_frame.pack()

bottom_frame = tk.Frame(root)
bottom_frame.pack()

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

break_loop = True
time_interval = 1.0
user_defined_mouse_button = Button.left
user_defined_start = keyboard.Key.f1
user_defined_stop = keyboard.Key.f2
user_defined_end = keyboard.Key.f3
mouse = Controller()

def click_loop(event = None):
    global break_loop, time_interval
    if break_loop == False:
        mouse.press(user_defined_mouse_button)
        mouse.release(user_defined_mouse_button)
        root.after(int(time_interval*1000), click_loop)

def on_press(key):
    global break_loop, user_defined_start, user_defined_end
    if key == user_defined_start and break_loop:
        break_loop = False
        click_loop()
    if key == user_defined_stop and break_loop == False:
        break_loop = True
    if key == user_defined_end:
        root.destroy()
        
listener = keyboard.Listener(on_press = on_press)
listener.start()

def set_time():
    global _time, time_interval
    try:
        if float(_time.get()) < 0:
            return
        time_interval = float(_time.get())
    except:
        return
    label_time.config(text = "Time interval:" + _time.get() + "(s)")

def set_mouse_button():
    global user_defined_mouse_button, mouse_button_list
    user_defined_mouse_button = mouse_button_list.get(mouse_button_index.current(), None)
    label_mouse_button.config(text = "Mouse button:" + str(user_defined_mouse_button).replace('Button.', '').title())
   
def key_list_start():
    global user_defined_start, user_defined_stop, user_defined_end, key_list
    temp = user_defined_start
    label_start.config(text = "Start key:F" + str(key_start_index.current()+1))
    user_defined_start = key_list.get(key_start_index.current(), None)
    if user_defined_start == user_defined_stop or user_defined_start == user_defined_end:
        if user_defined_start == user_defined_stop:
            num = ''.join([x for x in str(temp) if x.isdigit()])
            label_stop.config(text = "Stop key:F" + num)
            key_stop_index.current(int(num)-1)
            user_defined_stop = temp
        else:
            num = ''.join([x for x in str(temp) if x.isdigit()])
            label_end.config(text = "End key:F" + num)
            key_end_index.current(int(num)-1)
            user_defined_end = temp
    
def key_list_stop():
    global user_defined_start, user_defined_stop, user_defined_end, key_list
    temp = user_defined_stop
    label_stop.config(text = "Stop key:F" + str(key_stop_index.current()+1))
    user_defined_stop = key_list.get(key_stop_index.current(), None)
    if user_defined_stop == user_defined_start or user_defined_stop == user_defined_end:
        if user_defined_stop == user_defined_start:
            num = ''.join([x for x in str(temp) if x.isdigit()])
            label_start.config(text = "Start key:F" + num)
            key_start_index.current(int(num)-1)
            user_defined_start = temp   
        else:
            num = ''.join([x for x in str(temp) if x.isdigit()])
            label_end.config(text = "End key:F" + num)
            key_end_index.current(int(num)-1)
            user_defined_end = temp

def key_list_end():
    global user_defined_start, user_defined_stop, user_defined_end, key_list
    temp = user_defined_end
    label_end.config(text = "End key:F" + str(key_end_index.current()+1))
    user_defined_end = key_list.get(key_end_index.current(), None)  
    if user_defined_end == user_defined_start or user_defined_end == user_defined_stop:
        if user_defined_end == user_defined_start:
            num = ''.join([x for x in str(temp) if x.isdigit()])
            label_start.config(text = "Start key:F" + num)
            key_start_index.current(int(num)-1)
            user_defined_start = temp   
        else:
            num = ''.join([x for x in str(temp) if x.isdigit()])
            label_stop.config(text = "Stop key:F" + num)
            key_stop_index.current(int(num)-1)
            user_defined_stop = temp

label_time = ttk.Label(time_frame, text = "Time interval:1.0(s)")
label_time.grid(column = 1, row = 0)

label_mouse_button = ttk.Label(mouse_button_frame, text = "Mouse button:Left")
label_mouse_button.grid(column = 1, row = 0)

label_start = ttk.Label(top_frame, text = "Start key:F1")
label_start.grid(column = 1, row = 0)

label_stop = ttk.Label(middle_frame, text = "Stop key:F2")
label_stop.grid(column = 1, row = 0)

label_end = ttk.Label(bottom_frame, text = "End key:F3")
label_end.grid(column = 1, row = 0)

_time = tk.StringVar()
_time.set("1.0")
content = tk.Entry(time_frame, textvariable = _time, width = 18).grid(column=1, row=1)

mouse_button = tk.StringVar()
mouse_button_index = ttk.Combobox(mouse_button_frame, width = 15, textvariable = mouse_button, state = "readonly")
mouse_button_index['values'] = (Button.left, Button.middle, Button.right)
mouse_button_index.grid(column = 1, row = 1)
mouse_button_index.current(0)

key_start = tk.StringVar()
key_start_index = ttk.Combobox(top_frame, width = 15, textvariable = key_start, state = "readonly")
key_start_index['values'] = (keyboard.Key.f1, keyboard.Key.f2, keyboard.Key.f3, keyboard.Key.f4, keyboard.Key.f5, keyboard.Key.f6, keyboard.Key.f7, keyboard.Key.f8, keyboard.Key.f9, keyboard.Key.f10, keyboard.Key.f11, keyboard.Key.f12)
key_start_index.grid(column = 1, row = 1)
key_start_index.current(0)

key_stop = tk.StringVar()
key_stop_index = ttk.Combobox(middle_frame, width = 15, textvariable = key_stop, state = "readonly")
key_stop_index['values'] = (keyboard.Key.f1, keyboard.Key.f2, keyboard.Key.f3, keyboard.Key.f4, keyboard.Key.f5, keyboard.Key.f6, keyboard.Key.f7, keyboard.Key.f8, keyboard.Key.f9, keyboard.Key.f10, keyboard.Key.f11, keyboard.Key.f12)
key_stop_index.grid(column = 1, row = 1)
key_stop_index.current(1)

key_end = tk.StringVar()
key_end_index = ttk.Combobox(bottom_frame, width = 15, textvariable = key_end, state = "readonly")
key_end_index['values'] = (keyboard.Key.f1, keyboard.Key.f2, keyboard.Key.f3, keyboard.Key.f4, keyboard.Key.f5, keyboard.Key.f6, keyboard.Key.f7, keyboard.Key.f8, keyboard.Key.f9, keyboard.Key.f10, keyboard.Key.f11, keyboard.Key.f12)
key_end_index.grid(column = 1, row = 1)
key_end_index.current(2)

action_time = ttk.Button(time_frame, text = "Set", command = set_time).grid(column = 2, row = 1)
action_mouse_button = ttk.Button(mouse_button_frame, text = "Set", command = set_mouse_button).grid(column = 2, row = 1)
action_start = ttk.Button(top_frame, text = "Set", command = key_list_start).grid(column = 2, row = 1)
action_stop = ttk.Button(middle_frame, text = "Set", command = key_list_stop).grid(column = 2, row = 1)
action_end = ttk.Button(bottom_frame, text = "Set", command = key_list_end).grid(column = 2, row = 1)

root.mainloop()
