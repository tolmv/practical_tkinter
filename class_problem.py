import sys
import math
from Tkinter import *



class Restraints:

    def __init__(self, main):
        self.all_entry = []
        self.clear_entry = ()
        self.abc = []
        self.entry = Entry(main)
        self.button_e = Button(main, text="Input")
        self.label_answer = Label(main, font=15)
        self.label_numb = Label(main, font=15)


        self.entry.grid(row=0, column=0)
        self.button_e.grid(row=0, column=1)
        self.label_numb.grid(row=0, column=2)
        self.label_answer.grid(row=0, column=3)

        self.entry.pack()
        self.button_e.pack()
        self.label_answer.pack()
        self.label_numb.pack()

        self.button_e.bind("<Button-1>", self.inp)

    def inp(self, event):

        txt = self.entry.get()
        try:
            txt = float(txt)

            self.all_entry.append(txt)
            if len(self.all_entry) >= 13:
                self.all_entry = self.all_entry[13:24]

                self.label_numb["text"] = str(len(self.all_entry))



            else:
                self.label_numb["text"] = str(len(self.all_entry))

        except:
            self.label_answer["text"] = "Error, please check your input"
            self.all_entry = self.clear_entry
            print(self.clear_entry)
            print(self.all_entry)
        if len(self.all_entry) == 12:
            self.label_answer['text'] = self.calculate()
            self.label_answer = self.abc







    def calculate(self):

        K = self.all_entry[0]  # Gas constant in kJ/mol/K
        V = self.all_entry[1]  # standard volume in nm^3

        T = self.all_entry[2]  # Temperature in Kelvin
        r0 = self.all_entry[3]  # Distance in nm
        thA = self.all_entry[4]  # Angle in degrees
        thB = self.all_entry[5]  # Angle in degrees

        K_r = self.all_entry[6]  # force constant for distance (kJ/mol/nm^2)
        K_thA = self.all_entry[7]  # force constant for angle (kJ/mol/rad^2)
        K_thB = self.all_entry[8]  # force constant for angle (kJ/mol/rad^2)
        K_phiA = self.all_entry[9]  # force constant for dihedral (kJ/mol/rad^2)
        K_phiB = self.all_entry[10] # force constant for dihedral (kJ/mol/rad^2)
        K_phiC = self.all_entry[11]  # force constant for dihedral (kJ/mol/rad^2)

        thA = math.radians(thA)  # convert angle from degrees to radians --> math.sin() wants radians
        thB = math.radians(thB)  # convert angle from degrees to radians --> math.sin() wants radians

        arg = (
                (8.0 * math.pi ** 2.0 * V) / (r0 ** 2.0 * math.sin(thA) * math.sin(thB))
                *
                (
                        ((K_r * K_thA * K_thB * K_phiA * K_phiB * K_phiC) ** 0.5) / ((2.0 * math.pi * K * T) ** (3.0))
                )
        )

        dG = - K * T * math.log(arg)

        return "dG_off = {:.3f} kJ/mol".format(dG), "dG_on  = {:.3f} kJ/mol".format(-dG)

root = Tk()

root.title("restraints-2")

que = Restraints(root)

root.mainloop()
