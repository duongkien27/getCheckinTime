import tkinter as tk
from datetime import datetime, timedelta
import getpass
import os
USER_NAME = getpass.getuser()


def add_to_startup(file_path=""):
    if file_path == "":
        file_path = os.path.dirname(os.path.abspath("data.txt"))
        file_path = file_path + "\\autoLogin.exe"
    bat_path = r'C:\Users\%s\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Startup' % USER_NAME
    if not os.path.exists(bat_path + "\\open.bat"):
        with open(bat_path + '\\' + "open.bat", "w+") as bat_file:
            bat_file.write(r'start "" "%s"' % file_path)


checkin_time = datetime.now()
cur_timeFormated = checkin_time.strftime('%H:%M')
end_time = checkin_time + timedelta(hours=9)
end_timeFormated = end_time.strftime('%H:%M')


def update_time():
    cur_time = datetime.now()
    if  end_time >= cur_time:
        remaining_time = end_time - cur_time
        time_label3.after(1000, update_time)  # Update every 1000 milliseconds (1 second)
        time_label3.config(text= str(remaining_time).split(".")[0])
    else: 
        remaining_time = cur_time - end_time
        time_label3.config(text= str(remaining_time).split(".")[0], fg="green")

    
root = tk.Tk()
root.title("Digital Clock")
root.attributes("-topmost", True)
root.wm_attributes("-toolwindow", 1)
#root.overrideredirect(True)
#root.wm_attributes("-disabled", True)
root.wm_attributes("-transparentcolor", "black")
root.config(bg="black")
#root.overrideredirect(1)
#def move(event):
    #root.geometry(f'+{event.x_root}+{event.y_root}')
root.geometry("-250-5")
add_to_startup("")
time_label1 = tk.Label(root,fg="green",bg="black", font=("Helvetica", 12))
time_label1.pack(side="left", anchor="w")
time_label1.config(text= cur_timeFormated)

time_label2 = tk.Label(root,fg="red",bg="black", font=("Helvetica", 12))
time_label2.pack(side="left", anchor="w")
time_label2.config(text= end_timeFormated)

time_label3 = tk.Label(root,fg="red",bg="black", font=("Helvetica", 18))
time_label3.pack(side='right', anchor="e")

update_time()  # Start the clock
#root.bind('<B1-Motion>',move)
root.mainloop()