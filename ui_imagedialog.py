# Form implementation generated from reading ui file '.\Ui_ImageDialog.ui'
#
# Created by: PyQt6 UI code generator 6.5.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_ImageDialog(object):
    def setupUi(self, ImageDialog):
        ImageDialog.setObjectName("ImageDialog")
        ImageDialog.resize(602, 623)
        self.timer = QtCore.QTimer()
        self.timer.setInterval(100)
        self.groupBox = QtWidgets.QGroupBox(parent=ImageDialog)
        self.groupBox.setGeometry(QtCore.QRect(20, 10, 381, 71))
        self.groupBox.setTitle("")
        self.groupBox.setFlat(False)
        self.groupBox.setObjectName("groupBox")
        self.status = QtWidgets.QLabel(parent=self.groupBox)
        self.status.setGeometry(QtCore.QRect(20, 30, 211, 20))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.status.setFont(font)
        self.status.setAcceptDrops(False)
        self.status.setText("")
        self.status.setObjectName("status")
        self.serial = QtWidgets.QLabel(parent=self.groupBox)
        self.serial.setGeometry(QtCore.QRect(240, 30, 131, 20))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.serial.setFont(font)
        self.serial.setText("")
        self.serial.setObjectName("serial")
        self.groupBox_2 = QtWidgets.QGroupBox(parent=ImageDialog)
        self.groupBox_2.setEnabled(False)
        self.groupBox_2.setGeometry(QtCore.QRect(10, 90, 561, 371))
        self.groupBox_2.setTitle("")
        self.groupBox_2.setFlat(False)
        self.groupBox_2.setObjectName("groupBox_2")
        self.comboBox = QtWidgets.QComboBox(parent=self.groupBox_2)
        self.comboBox.setGeometry(QtCore.QRect(70, 50, 69, 22))
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.label = QtWidgets.QLabel(parent=self.groupBox_2)
        self.label.setGeometry(QtCore.QRect(10, 50, 47, 20))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(parent=self.groupBox_2)
        self.label_2.setGeometry(QtCore.QRect(150, 50, 281, 21))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(parent=self.groupBox_2)
        self.label_3.setGeometry(QtCore.QRect(10, 80, 91, 41))
        self.label_3.setTextFormat(QtCore.Qt.TextFormat.AutoText)
        self.label_3.setWordWrap(True)
        self.label_3.setObjectName("label_3")
        self.lineEdit = QtWidgets.QLineEdit(parent=self.groupBox_2)
        self.lineEdit.setGeometry(QtCore.QRect(110, 90, 291, 20))
        self.lineEdit.setObjectName("lineEdit")
        self.label_4 = QtWidgets.QLabel(parent=self.groupBox_2)
        self.label_4.setGeometry(QtCore.QRect(10, 130, 81, 20))
        self.label_4.setObjectName("label_4")
        self.lineEdit_2 = QtWidgets.QLineEdit(parent=self.groupBox_2)
        self.lineEdit_2.setGeometry(QtCore.QRect(100, 130, 161, 20))
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.label_5 = QtWidgets.QLabel(parent=self.groupBox_2)
        self.label_5.setGeometry(QtCore.QRect(270, 130, 141, 20))
        font = QtGui.QFont()
        font.setPointSize(7)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.pushButton_2 = QtWidgets.QPushButton(parent=self.groupBox_2)
        self.pushButton_2.setGeometry(QtCore.QRect(420, 90, 121, 31))
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_3 = QtWidgets.QPushButton(parent=self.groupBox_2)
        self.pushButton_3.setGeometry(QtCore.QRect(440, 130, 101, 31))
        self.pushButton_3.setObjectName("pushButton_3")
        self.groupBox_3 = QtWidgets.QGroupBox(parent=self.groupBox_2)
        self.groupBox_3.setGeometry(QtCore.QRect(30, 170, 501, 141))
        self.groupBox_3.setObjectName("groupBox_3")
        self.label_6 = QtWidgets.QLabel(parent=self.groupBox_3)
        self.label_6.setGeometry(QtCore.QRect(20, 30, 71, 16))
        self.label_6.setObjectName("label_6")
        self.label_7 = QtWidgets.QLabel(parent=self.groupBox_3)
        self.label_7.setGeometry(QtCore.QRect(20, 70, 61, 16))
        self.label_7.setObjectName("label_7")
        self.comboBox_2 = QtWidgets.QComboBox(parent=self.groupBox_3)
        self.comboBox_2.setGeometry(QtCore.QRect(100, 30, 69, 22))
        self.comboBox_2.setObjectName("comboBox_2")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_3 = QtWidgets.QComboBox(parent=self.groupBox_3)
        self.comboBox_3.setGeometry(QtCore.QRect(100, 70, 69, 22))
        self.comboBox_3.setObjectName("comboBox_3")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.label_8 = QtWidgets.QLabel(parent=self.groupBox_3)
        self.label_8.setGeometry(QtCore.QRect(230, 30, 101, 20))
        self.label_8.setObjectName("label_8")
        self.comboBox_4 = QtWidgets.QComboBox(parent=self.groupBox_3)
        self.comboBox_4.setGeometry(QtCore.QRect(340, 30, 69, 22))
        self.comboBox_4.setObjectName("comboBox_4")
        self.comboBox_4.addItem("")
        self.comboBox_4.addItem("")
        self.comboBox_4.addItem("")
        self.comboBox_4.addItem("")
        self.label_9 = QtWidgets.QLabel(parent=self.groupBox_3)
        self.label_9.setGeometry(QtCore.QRect(230, 70, 101, 20))
        self.label_9.setObjectName("label_9")
        self.comboBox_5 = QtWidgets.QComboBox(parent=self.groupBox_3)
        self.comboBox_5.setGeometry(QtCore.QRect(340, 70, 69, 22))
        self.comboBox_5.setObjectName("comboBox_5")
        self.comboBox_5.addItem("")
        self.comboBox_5.addItem("")
        self.comboBox_5.addItem("")
        self.comboBox_5.addItem("")
        self.pushButton_4 = QtWidgets.QPushButton(parent=self.groupBox_3)
        self.pushButton_4.setGeometry(QtCore.QRect(360, 100, 131, 31))
        self.pushButton_4.setObjectName("pushButton_4")
        self.checkBox_3 = QtWidgets.QCheckBox(parent=self.groupBox_3)
        self.checkBox_3.setGeometry(QtCore.QRect(20, 100, 121, 16))
        self.checkBox_3.setObjectName("checkBox_3")
        self.pushButton_5 = QtWidgets.QPushButton(parent=self.groupBox_2)
        self.pushButton_5.setGeometry(QtCore.QRect(260, 320, 261, 41))
        self.pushButton_5.setObjectName("pushButton_5")
        self.checkBox = QtWidgets.QCheckBox(parent=self.groupBox_2)
        self.checkBox.setGeometry(QtCore.QRect(350, 70, 51, 17))
        self.checkBox.setObjectName("checkBox")
        self.pushButton_7 = QtWidgets.QPushButton(parent=self.groupBox_2)
        self.pushButton_7.setGeometry(QtCore.QRect(440, 50, 101, 31))
        self.pushButton_7.setObjectName("pushButton_7")
        self.checkBox_2 = QtWidgets.QCheckBox(parent=self.groupBox_2)
        self.checkBox_2.setGeometry(QtCore.QRect(30, 330, 211, 17))
        self.checkBox_2.setObjectName("checkBox_2")
        self.groupBox_4 = QtWidgets.QGroupBox(parent=ImageDialog)
        self.groupBox_4.setEnabled(False)
        self.groupBox_4.setGeometry(QtCore.QRect(420, 10, 120, 71))
        self.groupBox_4.setTitle("")
        self.groupBox_4.setFlat(False)
        self.groupBox_4.setObjectName("groupBox_4")
        self.pushButton_6 = QtWidgets.QPushButton(parent=self.groupBox_4)
        self.pushButton_6.setGeometry(QtCore.QRect(10, 20, 101, 31))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.pushButton_6.setFont(font)
        self.pushButton_6.setObjectName("pushButton_6")
        self.tableWidget = QtWidgets.QTableWidget(parent=ImageDialog)
        self.tableWidget.setGeometry(QtCore.QRect(130, 490, 441, 111))
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(2)
        self.tableWidget.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        self.pushButton_8 = QtWidgets.QPushButton(parent=ImageDialog)
        self.pushButton_8.setGeometry(QtCore.QRect(450, 470, 111, 21))
        self.pushButton_8.setObjectName("pushButton_8")
        self.groupBox_5 = QtWidgets.QGroupBox(parent=ImageDialog)
        self.groupBox_5.setGeometry(QtCore.QRect(10, 490, 111, 101))
        self.groupBox_5.setObjectName("groupBox_5")
        self.pushButton = QtWidgets.QPushButton(parent=self.groupBox_5)
        self.pushButton.setGeometry(QtCore.QRect(20, 30, 71, 23))
        self.pushButton.setObjectName("pushButton")
        self.pushButton_9 = QtWidgets.QPushButton(parent=self.groupBox_5)
        self.pushButton_9.setGeometry(QtCore.QRect(20, 60, 71, 23))
        self.pushButton_9.setObjectName("pushButton_9")
        self.groupBox_2.raise_()
        self.groupBox.raise_()
        self.groupBox_4.raise_()
        self.tableWidget.raise_()
        self.pushButton_8.raise_()
        self.groupBox_5.raise_()

        self.retranslateUi(ImageDialog)
        QtCore.QMetaObject.connectSlotsByName(ImageDialog)

    def retranslateUi(self, ImageDialog):
        _translate = QtCore.QCoreApplication.translate
        ImageDialog.setWindowTitle(_translate("ImageDialog", "Molto2(GUI)"))
        self.comboBox.setCurrentText(_translate("ImageDialog", "0"))
        self.comboBox.setItemText(0, _translate("ImageDialog", "0"))
        self.comboBox.setItemText(1, _translate("ImageDialog", "1"))
        self.comboBox.setItemText(2, _translate("ImageDialog", "2"))
        self.comboBox.setItemText(3, _translate("ImageDialog", "3"))
        self.comboBox.setItemText(4, _translate("ImageDialog", "4"))
        self.comboBox.setItemText(5, _translate("ImageDialog", "5"))
        self.comboBox.setItemText(6, _translate("ImageDialog", "6"))
        self.comboBox.setItemText(7, _translate("ImageDialog", "7"))
        self.comboBox.setItemText(8, _translate("ImageDialog", "8"))
        self.comboBox.setItemText(9, _translate("ImageDialog", "9"))
        self.comboBox.setItemText(10, _translate("ImageDialog", "10"))
        self.comboBox.setItemText(11, _translate("ImageDialog", "11"))
        self.comboBox.setItemText(12, _translate("ImageDialog", "12"))
        self.comboBox.setItemText(13, _translate("ImageDialog", "13"))
        self.comboBox.setItemText(14, _translate("ImageDialog", "14"))
        self.comboBox.setItemText(15, _translate("ImageDialog", "15"))
        self.comboBox.setItemText(16, _translate("ImageDialog", "16"))
        self.comboBox.setItemText(17, _translate("ImageDialog", "17"))
        self.comboBox.setItemText(18, _translate("ImageDialog", "18"))
        self.comboBox.setItemText(19, _translate("ImageDialog", "19"))
        self.comboBox.setItemText(20, _translate("ImageDialog", "20"))
        self.comboBox.setItemText(21, _translate("ImageDialog", "21"))
        self.comboBox.setItemText(22, _translate("ImageDialog", "22"))
        self.comboBox.setItemText(23, _translate("ImageDialog", "23"))
        self.comboBox.setItemText(24, _translate("ImageDialog", "24"))
        self.comboBox.setItemText(25, _translate("ImageDialog", "25"))
        self.comboBox.setItemText(26, _translate("ImageDialog", "26"))
        self.comboBox.setItemText(27, _translate("ImageDialog", "27"))
        self.comboBox.setItemText(28, _translate("ImageDialog", "28"))
        self.comboBox.setItemText(29, _translate("ImageDialog", "29"))
        self.comboBox.setItemText(30, _translate("ImageDialog", "30"))
        self.comboBox.setItemText(31, _translate("ImageDialog", "31"))
        self.comboBox.setItemText(32, _translate("ImageDialog", "32"))
        self.comboBox.setItemText(33, _translate("ImageDialog", "33"))
        self.comboBox.setItemText(34, _translate("ImageDialog", "34"))
        self.comboBox.setItemText(35, _translate("ImageDialog", "35"))
        self.comboBox.setItemText(36, _translate("ImageDialog", "36"))
        self.comboBox.setItemText(37, _translate("ImageDialog", "37"))
        self.comboBox.setItemText(38, _translate("ImageDialog", "38"))
        self.comboBox.setItemText(39, _translate("ImageDialog", "39"))
        self.comboBox.setItemText(40, _translate("ImageDialog", "40"))
        self.comboBox.setItemText(41, _translate("ImageDialog", "41"))
        self.comboBox.setItemText(42, _translate("ImageDialog", "42"))
        self.comboBox.setItemText(43, _translate("ImageDialog", "43"))
        self.comboBox.setItemText(44, _translate("ImageDialog", "44"))
        self.comboBox.setItemText(45, _translate("ImageDialog", "45"))
        self.comboBox.setItemText(46, _translate("ImageDialog", "46"))
        self.comboBox.setItemText(47, _translate("ImageDialog", "47"))
        self.comboBox.setItemText(48, _translate("ImageDialog", "48"))
        self.comboBox.setItemText(49, _translate("ImageDialog", "49"))
        self.comboBox.setItemText(50, _translate("ImageDialog", "50"))
        self.comboBox.setItemText(51, _translate("ImageDialog", "51"))
        self.comboBox.setItemText(52, _translate("ImageDialog", "52"))
        self.comboBox.setItemText(53, _translate("ImageDialog", "53"))
        self.comboBox.setItemText(54, _translate("ImageDialog", "54"))
        self.comboBox.setItemText(55, _translate("ImageDialog", "55"))
        self.comboBox.setItemText(56, _translate("ImageDialog", "56"))
        self.comboBox.setItemText(57, _translate("ImageDialog", "57"))
        self.comboBox.setItemText(58, _translate("ImageDialog", "58"))
        self.comboBox.setItemText(59, _translate("ImageDialog", "59"))
        self.comboBox.setItemText(60, _translate("ImageDialog", "60"))
        self.comboBox.setItemText(61, _translate("ImageDialog", "61"))
        self.comboBox.setItemText(62, _translate("ImageDialog", "62"))
        self.comboBox.setItemText(63, _translate("ImageDialog", "63"))
        self.comboBox.setItemText(64, _translate("ImageDialog", "64"))
        self.comboBox.setItemText(65, _translate("ImageDialog", "65"))
        self.comboBox.setItemText(66, _translate("ImageDialog", "66"))
        self.comboBox.setItemText(67, _translate("ImageDialog", "67"))
        self.comboBox.setItemText(68, _translate("ImageDialog", "68"))
        self.comboBox.setItemText(69, _translate("ImageDialog", "69"))
        self.comboBox.setItemText(70, _translate("ImageDialog", "70"))
        self.comboBox.setItemText(71, _translate("ImageDialog", "71"))
        self.comboBox.setItemText(72, _translate("ImageDialog", "72"))
        self.comboBox.setItemText(73, _translate("ImageDialog", "73"))
        self.comboBox.setItemText(74, _translate("ImageDialog", "74"))
        self.comboBox.setItemText(75, _translate("ImageDialog", "75"))
        self.comboBox.setItemText(76, _translate("ImageDialog", "76"))
        self.comboBox.setItemText(77, _translate("ImageDialog", "77"))
        self.comboBox.setItemText(78, _translate("ImageDialog", "78"))
        self.comboBox.setItemText(79, _translate("ImageDialog", "79"))
        self.comboBox.setItemText(80, _translate("ImageDialog", "80"))
        self.comboBox.setItemText(81, _translate("ImageDialog", "81"))
        self.comboBox.setItemText(82, _translate("ImageDialog", "82"))
        self.comboBox.setItemText(83, _translate("ImageDialog", "83"))
        self.comboBox.setItemText(84, _translate("ImageDialog", "84"))
        self.comboBox.setItemText(85, _translate("ImageDialog", "85"))
        self.comboBox.setItemText(86, _translate("ImageDialog", "86"))
        self.comboBox.setItemText(87, _translate("ImageDialog", "87"))
        self.comboBox.setItemText(88, _translate("ImageDialog", "88"))
        self.comboBox.setItemText(89, _translate("ImageDialog", "89"))
        self.comboBox.setItemText(90, _translate("ImageDialog", "90"))
        self.comboBox.setItemText(91, _translate("ImageDialog", "91"))
        self.comboBox.setItemText(92, _translate("ImageDialog", "92"))
        self.comboBox.setItemText(93, _translate("ImageDialog", "93"))
        self.comboBox.setItemText(94, _translate("ImageDialog", "94"))
        self.comboBox.setItemText(95, _translate("ImageDialog", "95"))
        self.comboBox.setItemText(96, _translate("ImageDialog", "96"))
        self.comboBox.setItemText(97, _translate("ImageDialog", "97"))
        self.comboBox.setItemText(98, _translate("ImageDialog", "98"))
        self.comboBox.setItemText(99, _translate("ImageDialog", "99"))
        self.label.setText(_translate("ImageDialog", "Profile: "))
        self.label_2.setText(_translate("ImageDialog", "Molto-2 v2 supports 100 profiles (0-99)"))
        self.label_3.setText(_translate("ImageDialog", "Seed (base32 or hex):"))
        self.label_4.setText(_translate("ImageDialog", "Profile title:"))
        self.label_5.setText(_translate("ImageDialog", "12 chars max, ASCII only"))
        self.pushButton_2.setText(_translate("ImageDialog", "write seed only"))
        self.pushButton_3.setText(_translate("ImageDialog", "set title only"))
        self.groupBox_3.setTitle(_translate("ImageDialog", "config"))
        self.label_6.setText(_translate("ImageDialog", "Time Step:"))
        self.label_7.setText(_translate("ImageDialog", "Algorithm:"))
        self.comboBox_2.setItemText(0, _translate("ImageDialog", "30s"))
        self.comboBox_2.setItemText(1, _translate("ImageDialog", "60s"))
        self.comboBox_3.setItemText(0, _translate("ImageDialog", "SHA1"))
        self.comboBox_3.setItemText(1, _translate("ImageDialog", "SHA256"))
        self.label_8.setText(_translate("ImageDialog", "Display timeout"))
        self.comboBox_4.setItemText(0, _translate("ImageDialog", "30s"))
        self.comboBox_4.setItemText(1, _translate("ImageDialog", "15s"))
        self.comboBox_4.setItemText(2, _translate("ImageDialog", "60s"))
        self.comboBox_4.setItemText(3, _translate("ImageDialog", "120s"))
        self.label_9.setText(_translate("ImageDialog", "OTP Length"))
        self.comboBox_5.setItemText(0, _translate("ImageDialog", "6"))
        self.comboBox_5.setItemText(1, _translate("ImageDialog", "4"))
        self.comboBox_5.setItemText(2, _translate("ImageDialog", "8"))
        self.comboBox_5.setItemText(3, _translate("ImageDialog", "10"))
        self.pushButton_4.setText(_translate("ImageDialog", "Apply config only"))
        self.checkBox_3.setText(_translate("ImageDialog", "Auto time"))
        self.pushButton_5.setText(_translate("ImageDialog", "provision profile"))
        self.checkBox.setText(_translate("ImageDialog", "hex"))
        self.pushButton_7.setText(_translate("ImageDialog", "remove seed"))
        self.checkBox_2.setText(_translate("ImageDialog", "config parameters  required"))
        self.pushButton_6.setText(_translate("ImageDialog", "Factory reset"))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("ImageDialog", "Serial Number"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("ImageDialog", "State"))
        self.pushButton_8.setText(_translate("ImageDialog", "Clear log"))
        self.groupBox_5.setTitle(_translate("ImageDialog", "Screen lock"))
        self.pushButton.setText(_translate("ImageDialog", "lock"))
        self.pushButton_9.setText(_translate("ImageDialog", "unlock"))
