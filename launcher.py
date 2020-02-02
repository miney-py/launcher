import tkinter as tk
from tkinter import messagebox
import traceback
import subprocess
import os
from idlelib.tooltip import Hovertip
import webbrowser
import miney


# Exception handling
def show_error(self, *args):
    err = traceback.format_exception(*args)
    messagebox.showerror('Exception', err)


tk.Tk.report_callback_exception = show_error

launcher_root = os.path.dirname(os.path.realpath(__file__))

if "MINEYDISTDIR" in os.environ:
    dist_root = os.environ["MINEYDISTDIR"]
else:
    dist_root = os.getcwd()


def create_tool_tip(widget, text, delay=500):
    tooltip = Hovertip(widget, " " + text + " ", delay)

    def enter(event):
        tooltip.showtip()

    def leave(event):
        tooltip.hidetip()

    widget.bind('<Enter>', enter)
    widget.bind('<Leave>', leave)


class Application(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.pack()
        self.background_img = None
        self.create_widgets()

    def create_widgets(self):
        self.background_img = tk.PhotoImage(file=os.path.join(launcher_root, "res", "miney-background.png"))
        background_label = tk.Label(self.master, image=self.background_img)
        background_label.place(x=0, y=0, relwidth=1, relheight=1)

        button_quickstart = tk.Button(
            self.master,
            text="Quickstart",
            command=quickstart,
            bg="#EDBA68",
            fg="#45678F",
            relief=tk.FLAT,
            padx=10,
            pady=5,
            font='Helvetica 18 bold'
        )

        button_start_minetest = tk.Button(
            self.master,
            text="Start Minetest",
            command=start_minetest,
            bg="#EDBA68",
            fg="#45678F",
            relief=tk.FLAT,
            padx=10,
            pady=5,
            font='Helvetica 12 bold'
        )

        button_start_idle = tk.Button(
            self.master,
            text="Start Python's IDLE",
            command=start_idle,
            bg="#EDBA68",
            fg="#45678F",
            relief=tk.FLAT,
            padx=10,
            pady=5,
            font='Helvetica 10 bold'
        )

        button_quit = tk.Button(
            self.master,
            text="QUIT",
            fg="#45678F",
            command=self.master.destroy,
            bg="#EDBA68",
            relief=tk.FLAT,
            padx=10,
            pady=5,
            font='Helvetica 10 bold'
        )

        button_doc_miney = tk.Button(
            self.master,
            text="Miney",
            fg="#45678F",
            command=open_doc_miney,
            bg="#EDBA68",
            relief=tk.FLAT,
            padx=10,
            pady=5,
            font='Helvetica 10 bold'
        )

        button_doc_minetest = tk.Button(
            self.master,
            text="Minetest",
            fg="#45678F",
            command=open_doc_minetest,
            bg="#EDBA68",
            relief=tk.FLAT,
            padx=10,
            pady=5,
            font='Helvetica 10 bold'
        )

        button_doc_python = tk.Button(
            self.master,
            text="Python",
            fg="#45678F",
            command=open_doc_python,
            bg="#EDBA68",
            relief=tk.FLAT,
            padx=10,
            pady=5,
            font='Helvetica 10 bold'
        )

        button_doc_examples = tk.Button(
            self.master,
            text="Examples",
            fg="#45678F",
            command=open_doc_examples,
            bg="#EDBA68",
            relief=tk.FLAT,
            padx=10,
            pady=5,
            font='Helvetica 10 bold'
        )

        button_quickstart.place(relx=0.5, y=180, x=-290, width=250)
        button_start_minetest.place(relx=0.5, y=300, x=-290, width=250)
        button_start_idle.place(relx=0.5, y=360, x=-290, width=250)
        button_quit.place(relx=0.5, y=440, x=160, width=150)

        create_tool_tip(button_quickstart, "Places you in a minetest world and opens IDLE")
        create_tool_tip(button_start_minetest, "Start Minetest with Mainmenu")
        create_tool_tip(button_start_idle, "Start Python IDLE IDE")

        button_doc_row_start = 215
        button_row_spacing = 46

        button_doc_miney.place(relx=0.5, y=button_doc_row_start + button_row_spacing * 0, x=65, width=200)
        button_doc_minetest.place(relx=0.5, y=button_doc_row_start + button_row_spacing * 1, x=65, width=200)
        button_doc_python.place(relx=0.5, y=button_doc_row_start + button_row_spacing * 2, x=65, width=200)
        button_doc_examples.place(relx=0.5, y=button_doc_row_start + button_row_spacing * 3, x=65, width=200)
        create_tool_tip(button_doc_miney, "Open Miney documentation in your webbrowser")
        create_tool_tip(button_doc_minetest, "Open Minetest documentation in your webbrowser")
        create_tool_tip(button_doc_python, "Open Python documentation in your webbrowser")
        create_tool_tip(button_doc_examples, "Open examples folder in explorer")


def quickstart():
    start_miney_game()
    start_idle()


def start_miney_game():
    miney.run_miney_game()


def start_minetest():
    miney.run_minetest()


def start_idle():
    subprocess.Popen(
        [os.path.join(dist_root, "Python", "pythonw.exe"),
         os.path.join(dist_root, "Python", "Lib", "idlelib", "idle.pyw"),
         "-s", "-r", os.path.join(launcher_root, "quickstart.py")]
    )


def open_doc_miney():
    webbrowser.open("https://miney.readthedocs.io/en/latest/")


def open_doc_minetest():
    webbrowser.open("https://wiki.minetest.net/Main_Page")


def open_doc_python():
    webbrowser.open("https://docs.python.org/3/")


def open_doc_examples():
    path = os.path.join(os.path.dirname(os.path.realpath(__file__)), "examples")
    os.startfile(path)


if __name__ == "__main__":
    root = tk.Tk()
    root.title("Miney Launcher - " + miney.__version__)
    root.iconbitmap(os.path.join(launcher_root, "res", "miney-logo-hires.ico"))
    root.geometry("707x500")
    root.resizable(False, False)

    app = Application(master=root)
    app.mainloop()
