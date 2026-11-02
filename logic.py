import csv, os
from PyQt6.QtWidgets import QMainWindow
from gui import Ui_Window1


class Logic(QMainWindow, Ui_Window1):
    # Variables
    budget = 0
    category = ""
    amount = 0
    percentage = 0
    amount_left = 0

    def __init__(self):
        super().__init__()
        self.setupUi(self)

        # connect buttons to functions
        self.enterBtn.clicked.connect(self.enter1)
        self.enterBtn_2.clicked.connect(self.enter2)

    # create function to handle the first enter button
    def enter1(self):
        # check to make sure that user input is a valid integer
        if not (self.budgetInput.text()).isdigit():
            self.errorLbl.setText("Please enter a numeric value")
        else:
            self.budget = int(self.budgetInput.text())

    # create function to handle the second enter button
    def enter2(self):
        # check if category and amount are valid values
        if not (self.categoryInput.text()).isalpha() or not (self.amtInput.text()).isdigit():
            self.errorLbl_2.setText("Please enter a string and a numeric value")
        else: # perform calculations and write to csv file
            category = str(self.categoryInput.text())
            self.amount = int(self.amtInput.text())

            self.percentage = self.amount / self.budget * 100
            self.amount_left = self.budget - self.amount

            # write to csv file
            with open("file.csv", "w", newline="") as file:
                # create csv writer methods
                writer = csv.writer(file)

                # write header
                if os.path.getsize("file.csv") == 0:
                    writer.writerow(["Category", "Budget", "Amount", "Percentage", "Amount Left"])

                writer.writerow([category, self.budget, self.amount, self.percentage, self.amount_left])