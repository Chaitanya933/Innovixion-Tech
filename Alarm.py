import tkinter as tk
from tkinter import messagebox
import time

# Defining a class
class AlarmClock:
    # Initializations for our code
    def __init__(self, master):
        self.master = master
        # Title
        master.title("Alarm Clock")
        # Date Label
        self.d_l = tk.Label(master, text="Set Alarm Date (YYYY-MM-DD):")
        self.d_l.pack()
        # Entry for Date Label
        self.d_e = tk.Entry(master)
        self.d_e.pack()
        # Time Label
        self.t_l = tk.Label(master, text="Set Alarm Time (HH:MM):")
        self.t_l.pack()
        # Entry for Time Label
        self.t_e = tk.Entry(master)
        self.t_e.pack()
        # Button for Set Alarm
        self.set_btn = tk.Button(master, text="Set Alarm", command=self.set_alarm)
        self.set_btn.pack()
        # Variables to store alarm date and time
        self.alarm_year = None
        self.alarm_month = None
        self.alarm_day = None
        self.alarm_hour = None
        self.alarm_minute = None

    # Another function for giving input and checking
    def set_alarm(self):
        alarm_date = self.d_e.get()
        alarm_time = self.t_e.get()
        # Try block for taking user input of date and time
        try:
            self.alarm_year, self.alarm_month, self.alarm_day = map(int, alarm_date.split('-'))
            self.alarm_hour, self.alarm_minute = map(int, alarm_time.split(':'))
            # Checks user date and time input with current time and date by inbuilt methods
            current_time = time.localtime()
            current_year, current_month, current_day = current_time.tm_year, current_time.tm_mon, current_time.tm_mday
            current_hour, current_minute = current_time.tm_hour, current_time.tm_min
            # If matches alerts as message defined in def alert function
            if (time.mktime((self.alarm_year, self.alarm_month, self.alarm_day, self.alarm_hour, self.alarm_minute, 0, 0, 0, 0)) >
                time.mktime((current_year, current_month, current_day, current_hour, current_minute, 0, 0, 0, 0))):
                time_difference_seconds = time.mktime((self.alarm_year, self.alarm_month, self.alarm_day, self.alarm_hour, self.alarm_minute, 0, 0, 0, 0)) - time.mktime((current_year, current_month, current_day, current_hour, current_minute, 0, 0, 0, 0))
                messagebox.showinfo("Alarm Set", f"Alarm set for {alarm_date} {alarm_time}")
                self.is_alarm_set = True
                self.check_alarm()
            else:
                messagebox.showwarning("Invalid Input", "Please enter correct date and time")
        except ValueError:
            messagebox.showerror("Invalid Input", "Please enter valid date in YYYY-MM-DD and time in HH:MM format")
    def check_alarm(self):
        current_time = time.localtime()
        current_year, current_month, current_day = current_time.tm_year, current_time.tm_mon, current_time.tm_mday
        current_hour, current_minute = current_time.tm_hour, current_time.tm_min
        if self.is_alarm_set and (current_year, current_month, current_day, current_hour, current_minute) == (
                self.alarm_year, self.alarm_month, self.alarm_day, self.alarm_hour, self.alarm_minute):
            self.alert()
        else:
            # Check every second 1000 means 1000 millisecond which is equal to 1 second
            self.master.after(1000, self.check_alarm)  
    # Alerts if alarm time matches with current time
    def alert(self):
        messagebox.showinfo("Alarm", "Wake up! The Time is up!!")
# Main Function
def main():
    root = tk.Tk()
    alarm_clock = AlarmClock(root)
    root.mainloop()

# Calling main function
if __name__ == "__main__":
    main()
