import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from check_db import *
from login import *
from register import *
from pass_change import *


class Login(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.ui.btn_change_pass.clicked.connect(self.call_pass_change)
        self.ui.btn_register.clicked.connect(self.call_register)
        self.ui.btn_login.clicked.connect(self.authenticate)
        self.base_line_edit = [self.ui.line_name, self.ui.line_password]

        self.check_db = CheckThread()
        self.check_db.my_signal.connect(self.signal_handler)

    # Проверка правильности ввода
    def check_input(funct):
        def wrapper(self):
            for line_edit in self.base_line_edit:
                if len(line_edit.text()) == 0:
                    return
            funct(self)
        return wrapper

    # Обработчик сигналов
    def signal_handler(self, value):
        QtWidgets.QMessageBox.about(self, 'Оповещение', value)


    @check_input
    def authenticate(self):
        name = self.ui.line_name.text()
        password = self.ui.line_password.text()
        self.check_db.thread_login(name, password)

    def call_register(self):
        window = Register(self)
        window.show()

    def call_pass_change(self):
        pass_window = ChangePassword(self)
        pass_window.show()


class Register(QtWidgets.QWidget):
    def __init__(self, parent=Login):
        super().__init__(parent, QtCore.Qt.Window)
        self.reg = Ui_Form()
        self.reg.setupUi(self)
        self.setWindowModality(1)
        self.check_db = CheckThread()
        self.check_db.my_signal.connect(self.signal_handler)

        self.reg.btn_save.clicked.connect(self.register)
        self.reg_lines = [self.reg.line_login, self.reg.line_password, self.reg.line_name,
                          self.reg.line_last_name, self.reg.line_born_date, self.reg.line_born_place,
                          self.reg.line_phone]

    def signal_handler(self, value):
        QtWidgets.QMessageBox.about(self, 'Оповещение', value)

    def check_input_2(function):
        def wrapper(self):
            for line in self.reg_lines:
                if len(line.text()) == 0:
                    return
            function(self)
        return wrapper

    @check_input_2
    def register(self):
        login = self.reg.line_login.text()
        password = self.reg.line_password.text()
        name = self.reg.line_name.text()
        last_name = self.reg.line_last_name.text()
        born_date = self.reg.line_born_date.text()
        born_place = self.reg.line_born_place.text()
        phone = self.reg.line_phone.text()
        self.check_db.thread_register(login, password, name, last_name, born_date, born_place, phone)


class ChangePassword(QtWidgets.QWidget):
    def __init__(self, parent=Login):
        super().__init__(parent, QtCore.Qt.Window)
        self.psc = Password_Change()
        self.psc.setupUi(self)
        self.setWindowModality(1)
        self.psc.btn_save.clicked.connect(self.change_pass)
        self.check_db = CheckThread()
        self.check_db.my_signal.connect(self.signal_handler)

    def signal_handler(self, value):
        QtWidgets.QMessageBox.about(self, 'Оповещение', value)

    def change_pass(self):
        login = self.psc.line_login.text()
        current_password = self.psc.line_current_password.text()
        new_password = self.psc.line_new_pass.text()
        new_password_confirm = self.psc.line_new_pass_confirm.text()
        if int(new_password) != int(new_password_confirm):
            self.psc.lbl_error.setText('new passwords dont match')
        else:
            self.check_db.thread_change_pass(login, current_password, new_password)


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    mywin = Login()
    mywin.show()
    sys.exit(app.exec_())