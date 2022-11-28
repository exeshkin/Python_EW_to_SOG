from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(450, 300)
        MainWindow.setMinimumSize(QtCore.QSize(450, 300))
        MainWindow.setMaximumSize(QtCore.QSize(450, 300))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(11)
        MainWindow.setFont(font)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("icon.png"),
                       QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setStyleSheet("")
        MainWindow.setIconSize(QtCore.QSize(24, 24))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setMinimumSize(QtCore.QSize(450, 300))
        self.centralwidget.setMaximumSize(QtCore.QSize(450, 300))
        self.centralwidget.setStyleSheet("QWidget{\n"
                                         "background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(0, 0, 127, 255), stop:1 rgba(255, 255, 255, 255));\n"
                                         "}")
        self.centralwidget.setObjectName("centralwidget")
        self.btn_start = QtWidgets.QPushButton(self.centralwidget)
        self.btn_start.setGeometry(QtCore.QRect(290, 17, 130, 35))
        self.btn_start.setMinimumSize(QtCore.QSize(130, 35))
        self.btn_start.setMaximumSize(QtCore.QSize(130, 35))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(14)
        font.setBold(False)
        font.setWeight(50)
        self.btn_start.setFont(font)
        self.btn_start.setCursor(QtGui.QCursor(
            QtCore.Qt.CursorShape.PointingHandCursor))
        self.btn_start.setStyleSheet("QPushButton{\n"
                                     "background-color: rgb(170, 170, 255);\n"
                                     "border: 1px solid rgb(85, 170, 255);\n"
                                     "border-radius: 5;\n"
                                     "}\n"
                                     "\n"
                                     "QPushButton:hover{\n"
                                     "background-color: rgb(135, 137, 255);\n"
                                     "color: rgb(241, 241, 241);\n"
                                     "}\n"
                                     "\n"
                                     "QPushButton:pressed{\n"
                                     "background-color: rgb(76, 70, 255);\n"
                                     "}")
        self.btn_start.setObjectName("btn_start")
        self.progress_bar = QtWidgets.QProgressBar(self.centralwidget)
        self.progress_bar.setGeometry(QtCore.QRect(20, 67, 410, 20))
        self.progress_bar.setMinimumSize(QtCore.QSize(410, 20))
        self.progress_bar.setMaximumSize(QtCore.QSize(410, 20))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(10)
        self.progress_bar.setFont(font)
        self.progress_bar.setStyleSheet("QProgressBar{\n"
                                        "background-color: rgb(197, 197, 197);\n"
                                        "border: 1px solid rgb(85, 170, 255);\n"
                                        "border-radius: 3px;\n"
                                        "text-align: center;\n"
                                        "}\n"
                                        "\n"
                                        "QProgressBar::chunk{\n"
                                        "border-radius: 3px;\n"
                                        "background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(85, 122, 255, 255), stop:1 rgba(255, 255, 255, 255));\n"
                                        "}")
        self.progress_bar.setProperty("value", 0)
        self.progress_bar.setObjectName("progress_bar")
        self.log_field = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.log_field.setGeometry(QtCore.QRect(20, 100, 410, 150))
        self.log_field.setMinimumSize(QtCore.QSize(410, 150))
        self.log_field.setMaximumSize(QtCore.QSize(410, 150))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(10)
        self.log_field.setFont(font)
        self.log_field.setStyleSheet("QPlainTextEdit{\n"
                                     "background-color: rgb(197, 197, 197);\n"
                                     "border-radius: 5;\n"
                                     "padding: 7;\n"
                                     "border: 1px solid rgb(85, 170, 255);\n"
                                     "}")
        self.log_field.setReadOnly(True)
        self.log_field.setPlainText("")
        self.log_field.setObjectName("log_field")
        self.btn_info = QtWidgets.QPushButton(self.centralwidget)
        self.btn_info.setGeometry(QtCore.QRect(20, 260, 30, 30))
        self.btn_info.setMinimumSize(QtCore.QSize(30, 30))
        self.btn_info.setMaximumSize(QtCore.QSize(30, 30))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(14)
        font.setBold(False)
        font.setWeight(50)
        self.btn_info.setFont(font)
        self.btn_info.setCursor(QtGui.QCursor(
            QtCore.Qt.CursorShape.PointingHandCursor))
        self.btn_info.setStyleSheet("QPushButton{\n"
                                    "border:1px solid rgb(0, 85, 255);\n"
                                    "border-radius: 15;\n"
                                    "background-color: rgb(170, 170, 255);\n"
                                    "padding: 0;\n"
                                    "}\n"
                                    "\n"
                                    "QPushButton:hover{\n"
                                    "background-color: rgb(135, 137, 255);\n"
                                    "}\n"
                                    "\n"
                                    "QPushButton:pressed{\n"
                                    "border: 1px solid rgb(80, 80, 80);\n"
                                    "background-color: rgb(76, 70, 255);\n"
                                    "color: rgb(255, 255, 255);\n"
                                    "}")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/icons/info.png"),
                        QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.btn_info.setIcon(icon1)
        self.btn_info.setIconSize(QtCore.QSize(38, 38))
        self.btn_info.setObjectName("btn_info")
        self.btn_stop = QtWidgets.QPushButton(self.centralwidget)
        self.btn_stop.setGeometry(QtCore.QRect(320, 260, 100, 30))
        self.btn_stop.setMinimumSize(QtCore.QSize(100, 30))
        self.btn_stop.setMaximumSize(QtCore.QSize(100, 30))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(14)
        font.setBold(False)
        font.setWeight(50)
        self.btn_stop.setFont(font)
        self.btn_stop.setCursor(QtGui.QCursor(
            QtCore.Qt.CursorShape.PointingHandCursor))
        self.btn_stop.setStyleSheet("QPushButton{\n"
                                    "background-color: rgb(170, 170, 255);\n"
                                    "border:1px solid rgb(0, 85, 255);\n"
                                    "border-radius: 5;\n"
                                    "}\n"
                                    "\n"
                                    "QPushButton:hover{\n"
                                    "background-color: rgb(135, 137, 255);\n"
                                    "color: rgb(241, 241, 241);\n"
                                    "}\n"
                                    "\n"
                                    "QPushButton:pressed{\n"
                                    "background-color: rgb(76, 70, 255);\n"
                                    "}")
        self.btn_stop.setObjectName("btn_stop")
        self.branham_or_vin = QtWidgets.QComboBox(self.centralwidget)
        self.branham_or_vin.setGeometry(QtCore.QRect(30, 23, 210, 24))
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Policy.Preferred, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(210)
        sizePolicy.setVerticalStretch(24)
        sizePolicy.setHeightForWidth(
            self.branham_or_vin.sizePolicy().hasHeightForWidth())
        self.branham_or_vin.setSizePolicy(sizePolicy)
        self.branham_or_vin.setMinimumSize(QtCore.QSize(210, 24))
        self.branham_or_vin.setMaximumSize(QtCore.QSize(210, 24))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(11)
        self.branham_or_vin.setFont(font)
        self.branham_or_vin.setStyleSheet("QComboBox{\n"
                                          "background-color: rgb(170, 170, 255);\n"
                                          "}")
        self.branham_or_vin.setObjectName("branham_or_vin")
        self.branham_or_vin.addItem("")
        self.branham_or_vin.addItem("")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate(
            "MainWindow", "Eternal Words → Song of God"))
        self.btn_start.setText(_translate("MainWindow", "Создать *.sog"))
        self.btn_info.setText(_translate("MainWindow", "i"))
        self.btn_stop.setText(_translate("MainWindow", "Стоп"))
        self.branham_or_vin.setItemText(0, _translate(
            "MainWindow", "Уилльям Маррион Бранхам"))
        self.branham_or_vin.setItemText(
            1, _translate("MainWindow", "Вин Даял"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec())
