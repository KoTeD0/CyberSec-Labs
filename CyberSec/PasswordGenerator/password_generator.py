# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'password_generator.ui'
#
# Created by: PyQt5 UI code generator 5.15.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_PasswordGenerator(object):
    def setupUi(self, PasswordGenerator):
        PasswordGenerator.setObjectName("PasswordGenerator")
        PasswordGenerator.resize(400, 380)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(PasswordGenerator.sizePolicy().hasHeightForWidth())
        PasswordGenerator.setSizePolicy(sizePolicy)
        PasswordGenerator.setMinimumSize(QtCore.QSize(400, 360))
        PasswordGenerator.setMaximumSize(QtCore.QSize(400, 380))
        self.centralwidget = QtWidgets.QWidget(PasswordGenerator)
        self.centralwidget.setObjectName("centralwidget")
        self.layoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.layoutWidget.setGeometry(QtCore.QRect(8, 12, 381, 361))
        self.layoutWidget.setObjectName("layoutWidget")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.layoutWidget)
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.lbl_main_text = QtWidgets.QLabel(self.layoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lbl_main_text.sizePolicy().hasHeightForWidth())
        self.lbl_main_text.setSizePolicy(sizePolicy)
        self.lbl_main_text.setMinimumSize(QtCore.QSize(379, 0))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.lbl_main_text.setFont(font)
        self.lbl_main_text.setAutoFillBackground(False)
        self.lbl_main_text.setObjectName("lbl_main_text")
        self.gridLayout_2.addWidget(self.lbl_main_text, 0, 0, 1, 2)
        self.box_params = QtWidgets.QGroupBox(self.layoutWidget)
        self.box_params.setObjectName("box_params")
        self.layoutWidget1 = QtWidgets.QWidget(self.box_params)
        self.layoutWidget1.setGeometry(QtCore.QRect(1, 13, 381, 241))
        self.layoutWidget1.setObjectName("layoutWidget1")
        self.gridLayout = QtWidgets.QGridLayout(self.layoutWidget1)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.box_russain = QtWidgets.QCheckBox(self.layoutWidget1)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.box_russain.setFont(font)
        self.box_russain.setObjectName("box_russain")
        self.gridLayout.addWidget(self.box_russain, 0, 0, 1, 1)
        self.box_latin = QtWidgets.QCheckBox(self.layoutWidget1)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.box_latin.setFont(font)
        self.box_latin.setObjectName("box_latin")
        self.gridLayout.addWidget(self.box_latin, 0, 1, 1, 1)
        self.box_uppercase = QtWidgets.QCheckBox(self.layoutWidget1)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.box_uppercase.setFont(font)
        self.box_uppercase.setObjectName("box_uppercase")
        self.gridLayout.addWidget(self.box_uppercase, 1, 0, 1, 1)
        self.box_numbers = QtWidgets.QCheckBox(self.layoutWidget1)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.box_numbers.setFont(font)
        self.box_numbers.setObjectName("box_numbers")
        self.gridLayout.addWidget(self.box_numbers, 1, 1, 1, 1)
        self.box_lowercase = QtWidgets.QCheckBox(self.layoutWidget1)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.box_lowercase.setFont(font)
        self.box_lowercase.setObjectName("box_lowercase")
        self.gridLayout.addWidget(self.box_lowercase, 2, 0, 1, 1)
        self.box_special_symbols = QtWidgets.QCheckBox(self.layoutWidget1)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.box_special_symbols.setFont(font)
        self.box_special_symbols.setObjectName("box_special_symbols")
        self.gridLayout.addWidget(self.box_special_symbols, 2, 1, 1, 1)
        self.lbl_pass_len = QtWidgets.QLabel(self.layoutWidget1)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.lbl_pass_len.setFont(font)
        self.lbl_pass_len.setObjectName("lbl_pass_len")
        self.gridLayout.addWidget(self.lbl_pass_len, 3, 0, 1, 1)
        self.line_pass_len = QtWidgets.QLineEdit(self.layoutWidget1)
        self.line_pass_len.setInputMethodHints(QtCore.Qt.ImhDigitsOnly)
        self.line_pass_len.setObjectName("line_pass_len")
        self.gridLayout.addWidget(self.line_pass_len, 3, 1, 1, 1)
        self.gridLayout_2.addWidget(self.box_params, 1, 0, 1, 2)
        self.lbl_generate_pass = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.lbl_generate_pass.setFont(font)
        self.lbl_generate_pass.setObjectName("lbl_generate_pass")
        self.gridLayout_2.addWidget(self.lbl_generate_pass, 2, 0, 1, 1)
        self.line_rdy_pass = QtWidgets.QLineEdit(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.line_rdy_pass.setFont(font)
        self.line_rdy_pass.setReadOnly(True)
        self.line_rdy_pass.setObjectName("line_rdy_pass")
        self.gridLayout_2.addWidget(self.line_rdy_pass, 2, 1, 1, 1)
        self.btn_generate_pass = QtWidgets.QPushButton(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.btn_generate_pass.setFont(font)
        self.btn_generate_pass.setObjectName("btn_generate_pass")
        self.gridLayout_2.addWidget(self.btn_generate_pass, 3, 0, 1, 1)
        self.btn_reset = QtWidgets.QPushButton(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.btn_reset.setFont(font)
        self.btn_reset.setObjectName("btn_reset")
        self.gridLayout_2.addWidget(self.btn_reset, 3, 1, 1, 1)
        PasswordGenerator.setCentralWidget(self.centralwidget)

        self.retranslateUi(PasswordGenerator)
        QtCore.QMetaObject.connectSlotsByName(PasswordGenerator)

    def retranslateUi(self, PasswordGenerator):
        _translate = QtCore.QCoreApplication.translate
        PasswordGenerator.setWindowTitle(_translate("PasswordGenerator", "Password Generator"))
        self.lbl_main_text.setText(_translate("PasswordGenerator", "<html><head/><body><p>Password Generator v.1.0 Stable</p></body></html>"))
        self.box_params.setTitle(_translate("PasswordGenerator", "Generating Password Options"))
        self.box_russain.setText(_translate("PasswordGenerator", "Russian Letters"))
        self.box_latin.setText(_translate("PasswordGenerator", "Latin Letters"))
        self.box_uppercase.setText(_translate("PasswordGenerator", "Uppercase"))
        self.box_numbers.setText(_translate("PasswordGenerator", "Numbers"))
        self.box_lowercase.setText(_translate("PasswordGenerator", "Lowercase"))
        self.box_special_symbols.setText(_translate("PasswordGenerator", "Special Sybmols"))
        self.lbl_pass_len.setText(_translate("PasswordGenerator", "Password Length"))
        self.line_pass_len.setPlaceholderText(_translate("PasswordGenerator", "default 12 characters"))
        self.lbl_generate_pass.setText(_translate("PasswordGenerator", "Generated Password"))
        self.btn_generate_pass.setText(_translate("PasswordGenerator", "Generate Password"))
        self.btn_reset.setText(_translate("PasswordGenerator", "Reset"))
