from PyQt5 import QtCore, QtGui, QtWidgets
from handler.db_handler import *


class CheckThread(QtCore.QThread):
    my_signal = QtCore.pyqtSignal(str)

    def thread_login(self, name, password):
        logon(name, password, self.my_signal)

    def thread_register(self, login, password, name, last_name, born_date, born_place, phone):
        register(login, password, name, last_name, born_date, born_place, phone, self.my_signal)

    def thread_change_pass(self, login, current_password, new_password):
        change_pass(login, current_password, new_password, self.my_signal)