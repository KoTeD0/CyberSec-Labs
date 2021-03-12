import sys
import random
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox
from password_generator import *


class PassGen(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_PasswordGenerator()
        self.ui.setupUi(self)

        self.error_message = QtWidgets.QErrorMessage()
        self.ui.btn_generate_pass.clicked.connect(self.generate_password)
        self.ui.btn_reset.clicked.connect(self.reset)

        self.ui.box_latin.clicked.connect(self.check_clicked)
        self.ui.box_russain.clicked.connect(self.check_clicked)
        self.ui.box_numbers.clicked.connect(self.check_clicked)
        self.ui.box_lowercase.clicked.connect(self.check_clicked)
        self.ui.box_uppercase.clicked.connect(self.check_clicked)
        self.ui.box_special_symbols.clicked.connect(self.check_clicked)

        self.alphabet = {
            'RU': 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя',
            'LAT': 'abcdefghijllmnopqrstuvwxyz',
            'NUM': '0123456789',
            'SYMBOL': '`~!@#$%^&*()_+-=[]{}"/.,<>\|№;',
        }

    def chance_to(self, symbol):
        if random.random() > 0.5:
            return symbol.upper()
        return symbol

    def generate_password(self):
        flags = self.check_clicked()
        list_of_allowed = []
        for key, value in flags.items():
            if key not in self.alphabet:
                continue
            elif value:
                list_of_allowed += self.alphabet[key]

        try:
            password = ''
            pass_len = self.ui.line_pass_len.text() or 12
            for i in range(int(pass_len)):
                if flags['uppercase'] and flags['lowercase']:
                    password += self.chance_to(random.choice(list_of_allowed))
                elif flags['uppercase']:
                    password += (random.choice(list_of_allowed)).upper()
                else:
                    password += random.choice(list_of_allowed)
            self.ui.line_rdy_pass.setText(password)
        except ValueError:
            self.show_error_window('Password Length must be INT')
        except IndexError:
            self.show_error_window('You must check at least one checkbox')

    def show_error_window(self, info):
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Critical)
        msg.setText("Critical Error")
        msg.setInformativeText(info)
        msg.setWindowTitle("Error")
        msg.exec_()

    def check_clicked(self):
        flags = {"RU": False, "LAT": False, "NUM": False, "SYMBOL": False, "uppercase": False, "lowercase": False}

        if self.ui.box_latin.isChecked():
            flags["LAT"] = True
        if self.ui.box_russain.isChecked():
            flags["RU"] = True
        if self.ui.box_numbers.isChecked():
            flags["NUM"] = True
        if self.ui.box_special_symbols.isChecked():
            flags["SYMBOL"] = True
        if self.ui.box_uppercase.isChecked():
            flags["uppercase"] = True
        if self.ui.box_lowercase.isChecked():
            flags["lowercase"] = True

        return flags

    def reset(self):
        self.ui.line_pass_len.clear()
        self.ui.line_rdy_pass.clear()
        self.ui.box_latin.setChecked(True)
        self.ui.box_russain.setChecked(False)
        self.ui.box_numbers.setChecked(False)
        self.ui.box_special_symbols.setChecked(False)
        self.ui.box_lowercase.setChecked(False)
        self.ui.box_uppercase.setChecked(False)


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    mywin = PassGen()
    mywin.show()
    sys.exit(app.exec_())
