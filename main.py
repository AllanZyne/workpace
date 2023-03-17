# from win10toast import ToastNotifier
import tkinter as tk
import time

MICROPAUSE_INTERVAL = 6 * 60
MICROPAUSE_DURATION = 8
WOKRBREAK_INTERVAL = 40 * 60
WOKRBREAK_DURATION = 5 * 60
HIGHUSAGE_THRESHOLD = 6 * 60 * 60
TRYAGAIN_DURATION = 30

# TODOs:
#  - [ ] Skip tips when in meeting/full screen
#  - [ ] Micropause tips
#  - [ ] Workbreak excerises

def micropause(wait=5):
    window = tk.Tk()
    window.eval('tk::PlaceWindow . center')
    window.attributes("-topmost", True)
    greeting = tk.Label(text="Micropause")
    greeting.pack()
    window.after(wait * 1000, window.destroy)
    window.mainloop()
    return True

def workspace_break(wait):
    window = tk.Tk()
    window.eval('tk::PlaceWindow . center')
    window.attributes("-topmost", True)
    greeting = tk.Label(text="Workpace Break")
    greeting.pack()
    window.after(wait * 1000, window.destroy)
    window.mainloop()
    return True

def high_daily_usage():
    window = tk.Tk()
    window.eval('tk::PlaceWindow . center')
    window.attributes("-topmost", True)
    greeting = tk.Label(text="High Usage")
    greeting.pack()
    window.mainloop()
    return True

def main():
    mircopause_start = time.time()
    workbreak_start = time.time()
    highusage_start = time.time()
    while True:
        mircopause_elapse = time.time() - mircopause_start
        workbreak_elapse = time.time() - workbreak_start
        highusage_elapse = time.time() - highusage_start

        if highusage_elapse > HIGHUSAGE_THRESHOLD:
            if high_daily_usage():
                exit()
            else:
                time.sleep(TRYAGAIN_DURATION)

        if workbreak_elapse > WOKRBREAK_INTERVAL:
            if workspace_break(wait=WOKRBREAK_DURATION):
                workbreak_start = time.time()
                mircopause_start = time.time()
            else:
                time.sleep(TRYAGAIN_DURATION)
        
        if mircopause_elapse > MICROPAUSE_INTERVAL:
            if micropause(wait=MICROPAUSE_DURATION):
                mircopause_start = time.time()
            else:
                time.sleep(TRYAGAIN_DURATION)

if __name__ == "__main__":
    main()


# toast = ToastNotifier()
# toast.show_toast(
#     "Notification",
#     "Notification body",
#     duration = 10,
#     # icon_path = "icon.ico",
#     threaded = True,
# )
