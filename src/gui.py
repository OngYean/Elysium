# gui.py

import tkinter as tk
from tkinter import *
from tkinter.messagebox import showerror
from tkinter.simpledialog import askinteger

from random import *

from sensor import *

class GUI(tk.Tk):
    """Elysium GUI based on Tkinter"""
    def __init__(self, env, *args, **kwargs):
        """Initializes the GUI instance"""

        self.mainwindow_widgets = {}
        self.mainwindow_variables = {}
        self.__env = env
        self.__nibp = NIBP(self.__env["NORMAL_CHANCE"])
        self.__oxi = PulseOximeterSpO2(self.__env["NORMAL_CHANCE"])
        self.__resp = RespiratoryRate(self.__env["NORMAL_CHANCE"])
        self.__temp = Temperature(self.__env["NORMAL_CHANCE"])

        super().__init__(*args, **kwargs)

    def init(self):
        pass

    def mainloop(self):
        # Perform first update
        self.update()
        super().mainloop()
        
    def update(self):
        """Updates vital parameters"""
        w = self.mainwindow_widgets
        v = self.mainwindow_variables
        arr = [
            self.__nibp.generate_value(),
            self.__oxi.generate_value(),
            self.__resp.generate_value(),
            self.__temp.generate_value()
        ]
        names = ["nibp", "oxi", "resp", "temp"]
        ab = [
            "Bradycardia",
            "Tachycardia",
            "Hypoactive P wave",
            "P pulmonale",
            "Short PR interval",
            "Prolonged PR interval",
            "Hypercapnia",
            "Hypocapnia",
            "Low lung compliance",
            "Hyperventilation",
            "Airway hyperinflation",
            "Airway hypoinflation",
            "Tachysystole",
            "Dystocia",
            "Tachycardia",
            "Bradycardia",
            "Low fetal pulse oximetry",
            "High fetal pulse oximetry"
        ]
        v["abnormal"].set("")
        if (random() >= self.__env["NORMAL_CHANCE"]):
            v["abnormal"].set(v["abnormal"].get() + choice(ab) + "\n")
        for i in range(4):
            v[names[i]].set(arr[i][0])
            w["lbl_" + names[i]].configure(foreground="#14ff53")
            w[names[i]].configure(foreground="#14ff53")
            w["unit_" + names[i]].configure(foreground="#14ff53")
            if (arr[i][1] != "Normal"):
                w["lbl_" + names[i]].configure(foreground="#ff3838")
                w[names[i]].configure(foreground="#ff3838")
                w["unit_" + names[i]].configure(foreground="#ff3838")
                v["abnormal"].set(v["abnormal"].get() + arr[i][1] + "\n")
        self.after(self.__env["INTERVAL"], self.update)
  
    def render_mainwindow(self):
        w = self.mainwindow_widgets
        v = self.mainwindow_variables
        top = self.winfo_toplevel()

        # Configure GUI
        self.title("Elysium")
        #self.iconbitmap(default=self.__env["PATH_ICO"])
        self.geometry("640x480")
        self.resizable(False, False)
        self.configure(background="black")

        # Add Variables
        v["nibp"] = StringVar(self)
        v["oxi"] = IntVar(self)
        v["resp"] = IntVar(self)
        v["temp"] = DoubleVar(self)
        v["abnormal"] = StringVar(self)

        # Add widgets
        w["lbl_nibp"] = Label(
            text="Noninvasive blood pressure (NIBP)",
            font=(self.__env["FONT_DEFAULT"], 12),
            background="black",
            foreground="#14ff53"
        )
        w["lbl_oxi"] = Label(
            text="Pulse oximeter SpO2",
            font=(self.__env["FONT_DEFAULT"], 12),
            background="black",
            foreground="#14ff53"
        )
        w["lbl_resp"] = Label(
            text="Respiratory rate",
            font=(self.__env["FONT_DEFAULT"], 12),
            background="black",
            foreground="#14ff53"
        )
        w["lbl_temp"] = Label(
            text="Body temperature",
            font=(self.__env["FONT_DEFAULT"], 12),
            background="black",
            foreground="#14ff53"
        )
        w["lbl_abnormal"] = Label(
            text="Abnormalities",
            font=(self.__env["FONT_DEFAULT"], 12),
            background="black",
            foreground="white"
        )
        w["nibp"] = Label(
            textvariable=v["nibp"],
            font=(self.__env["FONT_DEFAULT"], 48),
            background="black",
            foreground="#14ff53"
        )
        w["oxi"] = Label(
            textvariable=v["oxi"],
            font=(self.__env["FONT_DEFAULT"], 48),
            background="black",
            foreground="#14ff53"
        )
        w["resp"] = Label(
            textvariable=v["resp"],
            font=(self.__env["FONT_DEFAULT"], 48),
            background="black",
            foreground="#14ff53"
        )
        w["temp"] = Label(
            textvariable=v["temp"],
            font=(self.__env["FONT_DEFAULT"], 48),
            background="black",
            foreground="#14ff53"
        )
        w["abnormal"] = Label(
            textvariable=v["abnormal"],
            font=(self.__env["FONT_DEFAULT"], 12),
            background="black",
            foreground="#ff3838",
            justify=LEFT
        )
        w["unit_nibp"] = Label(
            text=self.__nibp.get_unit(),
            font=(self.__env["FONT_DEFAULT"], 24),
            background="black",
            foreground="#14ff53"
        )
        w["unit_oxi"] = Label(
            text=self.__oxi.get_unit(),
            font=(self.__env["FONT_DEFAULT"], 24),
            background="black",
            foreground="#14ff53"
        )
        w["unit_resp"] = Label(
            text=self.__resp.get_unit(),
            font=(self.__env["FONT_DEFAULT"], 24),
            background="black",
            foreground="#14ff53"
        )
        w["unit_temp"] = Label(
            text=self.__temp.get_unit(),
            font=(self.__env["FONT_DEFAULT"], 24),
            background="black",
            foreground="#14ff53"
        )

        # Place widgets
        w["lbl_nibp"].place(anchor=NW, relx=0.05, rely=0.05)
        w["lbl_oxi"].place(anchor=NW, relx=0.05, rely=0.25)
        w["lbl_resp"].place(anchor=NW, relx=0.05, rely=0.45)
        w["lbl_temp"].place(anchor=NW, relx=0.05, rely=0.65)
        w["lbl_abnormal"].place(anchor=NW, relx=0.65, rely=0.05)
        w["nibp"].place(anchor=NW, relx=0.05, rely=0.1)
        w["oxi"].place(anchor=NW, relx=0.05, rely=0.3)
        w["resp"].place(anchor=NW, relx=0.05, rely=0.5)
        w["temp"].place(anchor=NW, relx=0.05, rely=0.7)
        w["abnormal"].place(anchor=NW, relx=0.65, rely=0.1)
        w["unit_nibp"].place(anchor=NW, relx=0.45, rely=0.16)
        w["unit_oxi"].place(anchor=NW, relx=0.45, rely=0.36)
        w["unit_resp"].place(anchor=NW, relx=0.45, rely=0.56)
        w["unit_temp"].place(anchor=NW, relx=0.45, rely=0.76)