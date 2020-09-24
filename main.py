import sys
from PySide2.QtWidgets import *
from ui import Ui_MainWindow

app = QApplication(sys.argv)

Dialog = QDialog()
ui = Ui_MainWindow()
ui.setupUi(Dialog)
Dialog.show()


def one():
    text = ui.lineEdit.text()
    ui.lineEdit.setText(text + "1")


def two():
    text = ui.lineEdit.text()
    ui.lineEdit.setText(text + "2")


def three():
    text = ui.lineEdit.text()
    ui.lineEdit.setText(text + "3")


def four():
    text = ui.lineEdit.text()
    ui.lineEdit.setText(text + "4")


def five():
    text = ui.lineEdit.text()
    ui.lineEdit.setText(text + "5")


def six():
    text = ui.lineEdit.text()
    ui.lineEdit.setText(text + "6")


def seven():
    text = ui.lineEdit.text()
    ui.lineEdit.setText(text + "7")


def eight():
    text = ui.lineEdit.text()
    ui.lineEdit.setText(text + "8")


def nine():
    text = ui.lineEdit.text()
    ui.lineEdit.setText(text + "9")


def zero():
    text = ui.lineEdit.text()
    ui.lineEdit.setText(text + "0")


def clean():
    ui.lineEdit.setText("")


def plus():
    text = ui.lineEdit.text()
    ui.lineEdit.setText(text + "+")


def minus():
    text = ui.lineEdit.text()
    ui.lineEdit.setText(text + "-")


def multiplication():
    text = ui.lineEdit.text()
    ui.lineEdit.setText(text + "*")


def division():
    text = ui.lineEdit.text()
    ui.lineEdit.setText(text + "/")


def IS():
    answer = ui.lineEdit.text()
    answer = answer.strip("' ")
    result = eval(answer)
    ui.lineEdit.setText(str(result))


ui.pushButton.clicked.connect(one)
ui.pushButton_2.clicked.connect(two)
ui.pushButton_3.clicked.connect(three)
ui.pushButton_4.clicked.connect(four)
ui.pushButton_5.clicked.connect(five)
ui.pushButton_6.clicked.connect(six)
ui.pushButton_7.clicked.connect(seven)
ui.pushButton_8.clicked.connect(eight)
ui.pushButton_9.clicked.connect(nine)
ui.pushButton_10.clicked.connect(zero)
ui.pushButton_11.clicked.connect(clean)
ui.pushButton_12.clicked.connect(IS)
ui.pushButton_13.clicked.connect(plus)
ui.pushButton_14.clicked.connect(minus)
ui.pushButton_15.clicked.connect(multiplication)
ui.pushButton_16.clicked.connect(division)

sys.exit(app.exec_())
