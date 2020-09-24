from PySide2.QtCore import *
from PySide2.QtWidgets import *


class Ui_MainWindow(object):
    def setupUi(self, Window):
        if not Window.objectName():
            Window.setObjectName(u"Window")
        Window.resize(346, 395)
        Window.setStyleSheet(u"QPushButton {\n"
                             "	background-color: #c0c0c0;\n"
                             "	width: 75px;	\n"
                             "	height: 50px;\n"
                             "	font-size: 14px;\n"
                             "	border: none;\n"
                             "	font-weight: bold;\n"
                             "	text-align: center;\n"
                             "}\n"
                             "QPushButton:hover {\n"
                             "	background-color: #a9a9a9;\n"
                             "}\n"
                             "QPushButton:pressed {\n"
                             "	background-color: #808080;\n"
                             "}")
        self.centralwidget = QWidget(Window)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayoutWidget = QWidget(self.centralwidget)
        self.gridLayoutWidget.setObjectName(u"gridLayoutWidget")
        self.gridLayoutWidget.setGeometry(QRect(10, 80, 326, 276))
        self.gridLayout = QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setHorizontalSpacing(6)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)

        # кнопки
        self.pushButton = QPushButton(self.gridLayoutWidget)
        self.pushButton.setObjectName(u"1")
        self.gridLayout.addWidget(self.pushButton, 0, 1, 1, 1)

        self.pushButton_2 = QPushButton(self.gridLayoutWidget)
        self.pushButton_2.setObjectName(u"2")
        self.gridLayout.addWidget(self.pushButton_2, 0, 2, 1, 1)

        self.pushButton_3 = QPushButton(self.gridLayoutWidget)
        self.pushButton_3.setObjectName(u"3")
        self.gridLayout.addWidget(self.pushButton_3, 0, 3, 1, 1)

        self.pushButton_4 = QPushButton(self.gridLayoutWidget)
        self.pushButton_4.setObjectName(u"4")
        self.gridLayout.addWidget(self.pushButton_4, 1, 1, 1, 1)

        self.pushButton_5 = QPushButton(self.gridLayoutWidget)
        self.pushButton_5.setObjectName(u"5")
        self.gridLayout.addWidget(self.pushButton_5, 1, 2, 1, 1)

        self.pushButton_6 = QPushButton(self.gridLayoutWidget)
        self.pushButton_6.setObjectName(u"6")
        self.gridLayout.addWidget(self.pushButton_6, 1, 3, 1, 1)

        self.pushButton_7 = QPushButton(self.gridLayoutWidget)
        self.pushButton_7.setObjectName(u"7")
        self.gridLayout.addWidget(self.pushButton_7, 2, 1, 1, 1)

        self.pushButton_8 = QPushButton(self.gridLayoutWidget)
        self.pushButton_8.setObjectName(u"8")
        self.gridLayout.addWidget(self.pushButton_8, 2, 2, 1, 1)

        self.pushButton_9 = QPushButton(self.gridLayoutWidget)
        self.pushButton_9.setObjectName(u"9")
        self.gridLayout.addWidget(self.pushButton_9, 2, 3, 1, 1)

        self.pushButton_10 = QPushButton(self.gridLayoutWidget)
        self.pushButton_10.setObjectName(u"0")
        self.gridLayout.addWidget(self.pushButton_10, 4, 2, 1, 1)

        self.pushButton_11 = QPushButton(self.gridLayoutWidget)
        self.pushButton_11.setObjectName(u"C")
        self.gridLayout.addWidget(self.pushButton_11, 4, 1, 1, 1)

        self.pushButton_12 = QPushButton(self.gridLayoutWidget)
        self.pushButton_12.setObjectName(u"IS")
        self.gridLayout.addWidget(self.pushButton_12, 4, 3, 1, 1)

        self.pushButton_13 = QPushButton(self.gridLayoutWidget)
        self.pushButton_13.setObjectName(u"plus")
        self.gridLayout.addWidget(self.pushButton_13, 0, 4, 1, 1)

        self.pushButton_14 = QPushButton(self.gridLayoutWidget)
        self.pushButton_14.setObjectName(u"minus")
        self.gridLayout.addWidget(self.pushButton_14, 1, 4, 1, 1)

        self.pushButton_15 = QPushButton(self.gridLayoutWidget)
        self.pushButton_15.setObjectName(u"multiplication")
        self.gridLayout.addWidget(self.pushButton_15, 2, 4, 1, 1)

        self.pushButton_16 = QPushButton(self.gridLayoutWidget)
        self.pushButton_16.setObjectName(u"division")
        self.gridLayout.addWidget(self.pushButton_16, 4, 4, 1, 1)

        self.lineEdit = QLineEdit(self.centralwidget)
        self.lineEdit.setObjectName(u"lineEdit")
        self.lineEdit.setGeometry(QRect(10, 19, 321, 41))
        self.lineEdit.setStyleSheet(u"background-color: #dcdcdc;")
        self.retranslateUi(Window)

        QMetaObject.connectSlotsByName(Window)


    def retranslateUi(self, Window):
        Window.setWindowTitle(QCoreApplication.translate("Window", u"Window", None))
        self.pushButton.setText(QCoreApplication.translate("Window", u"1", None))
        self.pushButton_2.setText(QCoreApplication.translate("Window", u"2", None))
        self.pushButton_3.setText(QCoreApplication.translate("Window", u"3", None))
        self.pushButton_4.setText(QCoreApplication.translate("Window", u"4", None))
        self.pushButton_5.setText(QCoreApplication.translate("Window", u"5", None))
        self.pushButton_6.setText(QCoreApplication.translate("Window", u"6", None))
        self.pushButton_7.setText(QCoreApplication.translate("Window", u"7", None))
        self.pushButton_8.setText(QCoreApplication.translate("Window", u"8", None))
        self.pushButton_9.setText(QCoreApplication.translate("Window", u"9", None))
        self.pushButton_10.setText(QCoreApplication.translate("Window", u"0", None))
        self.pushButton_11.setText(QCoreApplication.translate("Window", u"C", None))
        self.pushButton_12.setText(QCoreApplication.translate("Window", u"=", None))
        self.pushButton_13.setText(QCoreApplication.translate("Window", u"+", None))
        self.pushButton_14.setText(QCoreApplication.translate("Window", u"-", None))
        self.pushButton_15.setText(QCoreApplication.translate("Window", u"*", None))
        self.pushButton_16.setText(QCoreApplication.translate("Window", u"/", None))
        self.lineEdit.setText("")
