# controller
# Lab 3 expanded and enhanced
# Calculator design inspired by iOS

import formulas
from PyQt6.QtWidgets import QMainWindow, QButtonGroup
from calc_gui import *

#This will help out in line 17
functions = ("add", "subtract", "multiply", "divide", "choose")

class Calculator(QMainWindow):
    def __init__(self):
        super(Calculator, self).__init__()
        self.CalcUI = Ui_iOScalculator()
        self.CalcUI.setupUi(self)

        self.areas = QButtonGroup(self)
        self.areas.addButton(self.radioButtonSqr, 1)
        self.areas.addButton(self.radioButtonRec, 2)
        self.areas.addButton(self.radioButtonCir, 3)
        self.areas.addButton(self.radioButtonTri, 4)

        area_formulas = {

        }

        self.user_TFA_option = int(self.areas.checkedId())
        self.area_selection = self.areas.get(self.user_TFA_option)
        self.



        self.pushButton9.clicked.connect()

    def addition(self):
        formulas.add


def main():
    if len() <= 1: #For when the user doesn't give an input

    elif len(arg) <= 3: #For when the user doesn't give enough values
        sys.exit("Need to provide at least two values")
    else:
        operation = arg[1].lower() #lower() will make the user's operation lowercase, which helps in line 18
        values = [float(x) for x in arg[2:]] #turns everything in the input after the operation into FPVs
        result = None

        if operation not in functions: #Uses the operation tuple (line 4) to determine if input operation is valid
            sys.exit(f"Valid operator names {functions}")
        #For when the operator is valid and at least 2 values are given
        elif operation == "add":
            result = formulas.add(values)
        elif operation == "subtract":
            result = formulas.subtract(values)
        elif operation == "multiply":
            result = formulas.multiply(values)
        elif operation == "divide":
            result = formulas.divide(values)
        elif operation == "choose":
            result = formulas.choose(values)

        if result is not None: #outputs the result of the user-requested function
            print(f"Answer = {result:.2f}")

if __name__ == "__main__":
    model =
    main(argument)