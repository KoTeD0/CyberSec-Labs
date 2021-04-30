from PyQt5 import QtCore, QtGui, QtWidgets
import sys
import random

from pass_form import *


class Prob(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_Password_Generator()
        self.ui.setupUi(self)

        self.ui.btn_generate_password.clicked.connect(self.GeneratePassword)
        self.ui.cbox_latin_up.clicked.connect(self._check_clicked)
        self.ui.cbox_latin_low.clicked.connect(self._check_clicked)
        self.ui.cbox_ru_up.clicked.connect(self._check_clicked)
        self.ui.cbox_ru_low.clicked.connect(self._check_clicked)
        self.ui.cbox_symbols.clicked.connect(self._check_clicked)
        self.ui.cbox_numbers.clicked.connect(self._check_clicked)

        self.alphabet = {
            'RU': 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя',
            'LAT': 'abcdefghijllmnopqrstuvwxyz',
            'NUM': '0123456789',
            'SYMBOL': '`~!@#$%^&*()_+-=[]{}"/.,<>\|№;',
        }

    def _CollectValues(self):
        P = float(self.ui.line_probability.text())
        V = int(self.ui.line_bruteforce_speed.text())
        T = int(self.ui.line_password_expiration_date.text())

        return [P, V, T]

    def _check_clicked(self):
        """ checkbox statement and return flags"""
        flags = {"RU_UP": False, "RU": False, "LAT_UP": False, "LAT": False, "NUM": False, "SYMBOL": False}

        if self.ui.cbox_latin_up.isChecked():
            flags["LAT_UP"] = True
        if self.ui.cbox_latin_low.isChecked():
            flags["LAT"] = True
        if self.ui.cbox_ru_up.isChecked():
            flags["RU_UP"] = True
        if self.ui.cbox_ru_low.isChecked():
            flags["RU"] = True
        if self.ui.cbox_symbols.isChecked():
            flags["SYMBOL"] = True
        if self.ui.cbox_numbers.isChecked():
            flags["NUM"] = True

        return flags

    def _CalculateStrength(self, A=26):
        CalcVal = self._CollectValues()
        LowLine = abs(int((CalcVal[1] * CalcVal[2]) / CalcVal[0]))      # S* = [V*T / P]
        L = 1

        while LowLine >= A ** L:
            L += 1

        ProbPassInTime = (CalcVal[1] * CalcVal[2]) / A ** L     # P = V*T / A^L

        return ProbPassInTime, LowLine, L

    def _AlphabetStuff(self):
        '''Here we take VALUES of KEYS that we got from checkboxes user match'''

        flags = self._check_clicked()
        listOfAllowed = []
        for key, value in flags.items():
            if value is True and key not in self.alphabet:
                if key == 'LAT_UP':
                    listOfAllowed += self.alphabet['LAT'].upper()
                elif key == 'RU_UP':
                    listOfAllowed += self.alphabet['RU'].upper()
            elif value is True:
                listOfAllowed += self.alphabet[key]

        return listOfAllowed

    def GeneratePassword(self):
        try:
            alphabet = self._AlphabetStuff() # here we got list of letters from which later we take random letters
            calculatedValues = self._CalculateStrength(len(alphabet)) # here calculated values
            password = ''

            for letter in range(calculatedValues[2]):
                password += random.choice(alphabet)

            self.ui.lbl_password_value.setText(str(password))
            self.ui.lbl_lower_limit_value.setText(str(calculatedValues[1]))
            self.ui.lbl_pass_strength_value.setText(str(len(alphabet)))
            self.ui.lbl_pass_len.setText(str(calculatedValues[2]))

        except Exception as Error:
            print(f"Got Error {Error}")


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    my_win = Prob()
    my_win.show()
    sys.exit(app.exec_())
