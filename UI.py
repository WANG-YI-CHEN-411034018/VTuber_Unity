from PyQt6 import QtCore, QtGui, QtWidgets
import sys
import Vtuber

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        self.V = Vtuber.vtuber()
        Dialog.setObjectName("Dialog")
        Dialog.resize(301, 110)
        font = QtGui.QFont()
        font.setFamily("Microsoft JhengHei")
        Dialog.setFont(font)
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(30, 20, 121, 31))
        font = QtGui.QFont()
        font.setBold(False)
        font.setUnderline(False)
        font.setWeight(50)
        font.setStrikeOut(False)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.checkBox = QtWidgets.QCheckBox(Dialog)
        self.checkBox.setGeometry(QtCore.QRect(30, 70, 131, 19))
        self.checkBox.setObjectName("checkBox")
        self.pushButton = QtWidgets.QPushButton(Dialog)
        self.pushButton.setGeometry(QtCore.QRect(170, 40, 93, 28))
        self.pushButton.setObjectName("pushButton")
        self.pushButton.clicked.connect(self.openV)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label.setText(_translate("Dialog", "Vtuber功能展示"))
        self.checkBox.setText(_translate("Dialog", "測試鏡頭"))
        self.pushButton.setText(_translate("Dialog", "開始"))
    
    def openV(self):
        self.V.main()


app = QtWidgets.QApplication(sys.argv)
Dialog = QtWidgets.QDialog()
ui = Ui_Dialog()
ui.setupUi(Dialog)



Dialog.show()
sys.exit(app.exec())
