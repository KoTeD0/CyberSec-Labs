# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '.\pass_form.ui'
#
# Created by: PyQt5 UI code generator 5.15.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Password_Generator(object):
    def setupUi(self, Password_Generator):
        Password_Generator.setObjectName("Password_Generator")
        Password_Generator.resize(500, 385)
        Password_Generator.setMinimumSize(QtCore.QSize(500, 385))
        Password_Generator.setMaximumSize(QtCore.QSize(500, 385))
        self.centralwidget = QtWidgets.QWidget(Password_Generator)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.centralwidget)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.mainFrame = QtWidgets.QFrame(self.centralwidget)
        self.mainFrame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.mainFrame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.mainFrame.setObjectName("mainFrame")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.mainFrame)
        self.verticalLayout.setObjectName("verticalLayout")
        self.frame_2 = QtWidgets.QFrame(self.mainFrame)
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.frame_2)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.groupBox_2 = QtWidgets.QGroupBox(self.frame_2)
        self.groupBox_2.setObjectName("groupBox_2")
        self.layoutWidget_2 = QtWidgets.QWidget(self.groupBox_2)
        self.layoutWidget_2.setGeometry(QtCore.QRect(10, 20, 281, 191))
        self.layoutWidget_2.setObjectName("layoutWidget_2")
        self.gridLayout = QtWidgets.QGridLayout(self.layoutWidget_2)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.lbl_Probability = QtWidgets.QLabel(self.layoutWidget_2)
        self.lbl_Probability.setMaximumSize(QtCore.QSize(16777215, 25))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.lbl_Probability.setFont(font)
        self.lbl_Probability.setObjectName("lbl_Probability")
        self.gridLayout.addWidget(self.lbl_Probability, 0, 0, 1, 1)
        self.line_probability = QtWidgets.QLineEdit(self.layoutWidget_2)
        self.line_probability.setObjectName("line_probability")
        self.gridLayout.addWidget(self.line_probability, 0, 1, 1, 1)
        self.lbl_bruteforce_speed = QtWidgets.QLabel(self.layoutWidget_2)
        self.lbl_bruteforce_speed.setMaximumSize(QtCore.QSize(16777215, 25))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.lbl_bruteforce_speed.setFont(font)
        self.lbl_bruteforce_speed.setObjectName("lbl_bruteforce_speed")
        self.gridLayout.addWidget(self.lbl_bruteforce_speed, 1, 0, 1, 1)
        self.line_bruteforce_speed = QtWidgets.QLineEdit(self.layoutWidget_2)
        self.line_bruteforce_speed.setObjectName("line_bruteforce_speed")
        self.gridLayout.addWidget(self.line_bruteforce_speed, 1, 1, 1, 1)
        self.lbl_password_expiratio_date = QtWidgets.QLabel(self.layoutWidget_2)
        self.lbl_password_expiratio_date.setMaximumSize(QtCore.QSize(16777215, 25))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.lbl_password_expiratio_date.setFont(font)
        self.lbl_password_expiratio_date.setObjectName("lbl_password_expiratio_date")
        self.gridLayout.addWidget(self.lbl_password_expiratio_date, 2, 0, 1, 1)
        self.line_password_expiration_date = QtWidgets.QLineEdit(self.layoutWidget_2)
        self.line_password_expiration_date.setObjectName("line_password_expiration_date")
        self.gridLayout.addWidget(self.line_password_expiration_date, 2, 1, 1, 1)
        self.label_5 = QtWidgets.QLabel(self.layoutWidget_2)
        self.label_5.setMaximumSize(QtCore.QSize(16777215, 25))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.gridLayout.addWidget(self.label_5, 3, 0, 1, 1)
        self.lbl_lower_limit_value = QtWidgets.QLabel(self.layoutWidget_2)
        self.lbl_lower_limit_value.setMaximumSize(QtCore.QSize(16777215, 25))
        self.lbl_lower_limit_value.setObjectName("lbl_lower_limit_value")
        self.gridLayout.addWidget(self.lbl_lower_limit_value, 3, 1, 1, 1)
        self.label_6 = QtWidgets.QLabel(self.layoutWidget_2)
        self.label_6.setMaximumSize(QtCore.QSize(16777215, 25))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.gridLayout.addWidget(self.label_6, 4, 0, 1, 1)
        self.lbl_pass_strength_value = QtWidgets.QLabel(self.layoutWidget_2)
        self.lbl_pass_strength_value.setObjectName("lbl_pass_strength_value")
        self.gridLayout.addWidget(self.lbl_pass_strength_value, 4, 1, 1, 1)
        self.label_7 = QtWidgets.QLabel(self.layoutWidget_2)
        self.label_7.setMaximumSize(QtCore.QSize(16777215, 25))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.label_7.setFont(font)
        self.label_7.setObjectName("label_7")
        self.gridLayout.addWidget(self.label_7, 5, 0, 1, 1)
        self.lbl_pass_len = QtWidgets.QLabel(self.layoutWidget_2)
        self.lbl_pass_len.setText("")
        self.lbl_pass_len.setObjectName("lbl_pass_len")
        self.gridLayout.addWidget(self.lbl_pass_len, 5, 1, 1, 1)
        self.horizontalLayout.addWidget(self.groupBox_2)
        self.groupBox = QtWidgets.QGroupBox(self.frame_2)
        self.groupBox.setMaximumSize(QtCore.QSize(140, 16777215))
        self.groupBox.setObjectName("groupBox")
        self.layoutWidget_3 = QtWidgets.QWidget(self.groupBox)
        self.layoutWidget_3.setGeometry(QtCore.QRect(10, 20, 121, 191))
        self.layoutWidget_3.setObjectName("layoutWidget_3")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.layoutWidget_3)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.cbox_latin_up = QtWidgets.QCheckBox(self.layoutWidget_3)
        self.cbox_latin_up.setObjectName("cbox_latin_up")
        self.verticalLayout_2.addWidget(self.cbox_latin_up)
        self.cbox_latin_low = QtWidgets.QCheckBox(self.layoutWidget_3)
        self.cbox_latin_low.setObjectName("cbox_latin_low")
        self.verticalLayout_2.addWidget(self.cbox_latin_low)
        self.cbox_ru_up = QtWidgets.QCheckBox(self.layoutWidget_3)
        self.cbox_ru_up.setObjectName("cbox_ru_up")
        self.verticalLayout_2.addWidget(self.cbox_ru_up)
        self.cbox_ru_low = QtWidgets.QCheckBox(self.layoutWidget_3)
        self.cbox_ru_low.setObjectName("cbox_ru_low")
        self.verticalLayout_2.addWidget(self.cbox_ru_low)
        self.cbox_symbols = QtWidgets.QCheckBox(self.layoutWidget_3)
        self.cbox_symbols.setObjectName("cbox_symbols")
        self.verticalLayout_2.addWidget(self.cbox_symbols)
        self.cbox_numbers = QtWidgets.QCheckBox(self.layoutWidget_3)
        self.cbox_numbers.setObjectName("cbox_numbers")
        self.verticalLayout_2.addWidget(self.cbox_numbers)
        self.horizontalLayout.addWidget(self.groupBox)
        self.verticalLayout.addWidget(self.frame_2)
        self.frame = QtWidgets.QFrame(self.mainFrame)
        self.frame.setMaximumSize(QtCore.QSize(16777215, 100))
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.frame)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.groupBox_3 = QtWidgets.QGroupBox(self.frame)
        self.groupBox_3.setObjectName("groupBox_3")
        self.layoutWidget = QtWidgets.QWidget(self.groupBox_3)
        self.layoutWidget.setGeometry(QtCore.QRect(10, 10, 431, 61))
        self.layoutWidget.setObjectName("layoutWidget")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.layoutWidget)
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.lbl_password_1 = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(9)
        self.lbl_password_1.setFont(font)
        self.lbl_password_1.setObjectName("lbl_password_1")
        self.gridLayout_2.addWidget(self.lbl_password_1, 0, 0, 1, 1)
        self.lbl_password_value = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(9)
        self.lbl_password_value.setFont(font)
        self.lbl_password_value.setText("")
        self.lbl_password_value.setObjectName("lbl_password_value")
        self.gridLayout_2.addWidget(self.lbl_password_value, 0, 1, 1, 1)
        self.btn_generate_password = QtWidgets.QPushButton(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(9)
        self.btn_generate_password.setFont(font)
        self.btn_generate_password.setObjectName("btn_generate_password")
        self.gridLayout_2.addWidget(self.btn_generate_password, 1, 0, 1, 2)
        self.verticalLayout_4.addWidget(self.groupBox_3)
        self.verticalLayout.addWidget(self.frame)
        self.horizontalLayout_2.addWidget(self.mainFrame)
        Password_Generator.setCentralWidget(self.centralwidget)

        self.retranslateUi(Password_Generator)
        QtCore.QMetaObject.connectSlotsByName(Password_Generator)

    def retranslateUi(self, Password_Generator):
        _translate = QtCore.QCoreApplication.translate
        Password_Generator.setWindowTitle(_translate("Password_Generator", "Password Generator v1"))
        self.groupBox_2.setTitle(_translate("Password_Generator", "Main"))
        self.lbl_Probability.setText(_translate("Password_Generator", "P(Probability)"))
        self.lbl_bruteforce_speed.setText(_translate("Password_Generator", "V(Bruteforce speed)"))
        self.lbl_password_expiratio_date.setText(_translate("Password_Generator", "Password expiration date"))
        self.label_5.setText(_translate("Password_Generator", "S* (Lower Password limit)"))
        self.lbl_lower_limit_value.setText(_translate("Password_Generator", "None"))
        self.label_6.setText(_translate("Password_Generator", "A (Password Strength)"))
        self.lbl_pass_strength_value.setText(_translate("Password_Generator", "None"))
        self.label_7.setText(_translate("Password_Generator", "L (Password Length)"))
        self.groupBox.setTitle(_translate("Password_Generator", "Options"))
        self.cbox_latin_up.setText(_translate("Password_Generator", "Latin Uppercase"))
        self.cbox_latin_low.setText(_translate("Password_Generator", "Latin lowercase"))
        self.cbox_ru_up.setText(_translate("Password_Generator", "Russian Uppercase"))
        self.cbox_ru_low.setText(_translate("Password_Generator", "Russian lowercase"))
        self.cbox_symbols.setText(_translate("Password_Generator", "Symbols"))
        self.cbox_numbers.setText(_translate("Password_Generator", "Numbers"))
        self.groupBox_3.setTitle(_translate("Password_Generator", "Password"))
        self.lbl_password_1.setText(_translate("Password_Generator", "Password: "))
        self.btn_generate_password.setText(_translate("Password_Generator", "Generate password"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Password_Generator = QtWidgets.QMainWindow()
    ui = Ui_Password_Generator()
    ui.setupUi(Password_Generator)
    Password_Generator.show()
    sys.exit(app.exec_())