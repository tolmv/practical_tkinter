import sys
import math
from Tkinter import *
import numpy as np



class Restraints():

    def __init__(self, main):
        self.help = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
        self.a = 1



        self.r_var = IntVar()
        self.r_var.set(0)
        self.rcal1 = Radiobutton(text="kCal", variable=self.r_var, value=0)
        self.rj1 = Radiobutton(text='kJ', variable=self.r_var, value=1)
        self.r_varr = BooleanVar()
        self.r_varr.set(0)
        self.rcal2 = Radiobutton(text="kCal", variable=self.r_varr, value=0)
        self.rj2 = Radiobutton(text='kJ', variable=self.r_varr, value=1)


        self.rj1.grid(row=0, column=0)
        self.rcal1.grid(row=0, column=1)
        self.rj2.grid(row=11, column=0)
        self.rcal2.grid(row=11, column=1)




        self.entry0 = Entry(main)
        self.entry1 = Entry(main)
        self.entry2 = Entry(main)
        self.entry3 = Entry(main)
        self.entry4 = Entry(main)
        self.entry5 = Entry(main)
        self.entry6 = Entry(main)
        self.entry7 = Entry(main)
        self.entry8 = Entry(main)
        self.entry9 = Entry(main)

        self.button0 = Button(main, text="Input")
        self.button1 = Button(main, text="Input")
        self.button2 = Button(main, text="Input")
        self.button3 = Button(main, text="Input")
        self.button4 = Button(main, text="Input")
        self.button5 = Button(main, text="Input")
        self.button6 = Button(main, text="Input")
        self.button7 = Button(main, text="Input")
        self.button8 = Button(main, text="Input")
        self.button9 = Button(main, text="Input")

        self.label_answer0 = Label(main, font=15)
        self.label_answer1 = Label(main, font=15)
        self.label_answer2 = Label(main, font=15)
        self.label_answer3 = Label(main, font=15)
        self.label_answer4 = Label(main, font=15)
        self.label_answer5 = Label(main, font=15)
        self.label_answer6 = Label(main, font=15)
        self.label_answer7 = Label(main, font=15)
        self.label_answer8 = Label(main, font=15)
        self.label_answer9 = Label(main, font=15)

        self.entry_all = [self.entry0, self.entry1, self.entry2, self.entry3, self.entry4,
                          self.entry5, self.entry6, self.entry7, self.entry8, self.entry9]


        self.label_all = [self.label_answer0, self.label_answer1,
                          self.label_answer2, self.label_answer3, self.label_answer4,
                          self.label_answer5, self.label_answer6,
                          self.label_answer7, self.label_answer8, self.label_answer9]

        self.button_all = [self.button0, self.button1, self.button2, self.button3, self.button4,
                           self.button5, self.button6, self.button7, self.button8, self.button9]

        self.label_res = Label(main, font=15)
        self.button_res = Button(main, text="Result: ")

        for i in range(1, 11):
            self.entry_all[i-1].grid(row=i, column=0)
            self.button_all[i-1].grid(row=i, column=1)
            self.label_all[i-1].grid(row=i, column=2)

        self.button_res.grid(row=11, column=2)
        self.label_res.grid(row=11, column=3)

        for i in range(10):
            self.button_all[i].bind("<Button-1>", self.inp)

        self.button_res.bind('<Button-1>', self.calculate)

        self.entry_all_get = [self.entry0.get(), self.entry1.get(), self.entry2.get(),
                              self.entry3.get(), self.entry4.get(),
                              self.entry5.get(), self.entry6.get(),
                              self.entry7.get(), self.entry8.get(), self.entry9.get()]
    def inp(self, event):
        try:
            for i in range(len(self.entry_all_get)):
                self.help.append(float(self.entry_all_get[i]))
                self.a = i

        except ValueError:
            self.label_all[self.a] = "Error, please check your input"




    def calculate(self, event):

        K = 8.314472 * 0.001  # Gas constant in kJ/mol/K
        V = 1.66  # standard volume in nm^3

        T = self.help[0]  # Temperature in Kelvin
        r0 = self.help[1]  # Distance in nm
        thA = self.help[2]  # Angle in degrees
        thB = self.help[3]  # Angle in degrees

        K_r = self.help[4]  # force constant for distance (kJ/mol/nm^2)
        K_thA = self.help[5]  # force constant for angle (kJ/mol/rad^2)
        K_thB = self.help[6]  # force constant for angle (kJ/mol/rad^2)
        K_phiA = self.help[7]  # force constant for dihedral (kJ/mol/rad^2)
        K_phiB = self.help[8]  # force constant for dihedral (kJ/mol/rad^2)
        K_phiC = self.help[9]  # force constant for dihedral (kJ/mol/rad^2)

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
        
        if self.r_var == 0:
            dG = gG * 0.23885
            self.label_res['text'] = "dG_off = {:.3f} kCal/mol".format(dG), "dG_on  = {:.3f} kCal/mol".format(-dG)

        else:
            self.label_res['text'] = "dG_off = {:.3f} kJ/mol".format(dG), "dG_on  = {:.3f} kJ/mol".format(-dG)


def main():
    root = Tk()
    app = Restraints(root)
    root.mainloop()


if __name__ == '__main__':
    main()


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
