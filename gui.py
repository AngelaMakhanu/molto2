import argparse, sys
import subprocess

from smartcard.System import readers
from PyQt5.QtWidgets import QApplication, QDialog, QTableWidgetItem
from ui_imagedialog import Ui_ImageDialog

app = QApplication(sys.argv)
window = QDialog()
ui = Ui_ImageDialog()
ui.setupUi(window)
window.show()

command = [sys.executable, "molto2.py", "--factoryreset"]


def connection():
    # subprocess.run(command, check=True)
    reader = next((reader for reader in readers()
                   if "TOKEN2".lower() in reader.name.lower()), None)
    try:
        connection = reader.createConnection()
        connection.connect()
        SELECT = [0x80, 0x41, 0x00, 0x00, 0x00]
        data, sw1, sw2 = connection.transmit(SELECT)
        info = bytes(data)
        serial_len = int(info[3])
        serial = info[4:4 + serial_len].decode("utf-8")
        ui.status.setText("      TOKEN2 Molto2 is connected")
        ui.status.setStyleSheet('background-color: green')
        ui.serial.setText(serial)
        ui.groupBox_2.setEnabled(True)
        ui.groupBox_4.setEnabled(True)
    except:
        ui.status.setText("      TOKEN2 Molto2 is disconnected")
        ui.status.setStyleSheet('background-color: red')
        ui.serial.setText("---------------")
        ui.groupBox_2.setEnabled(False)
        ui.groupBox_4.setEnabled(False)


def set_title():
    profilecombobox = ui.comboBox.currentText()
    titletextbox = ui.lineEdit_2.text()
    command_title = [sys.executable, "molto2.py", "--profile", profilecombobox, "--title", titletextbox]
    try:
        subprocess.run(command_title, check=True)
        write_log("Successful operation ")
    except subprocess.CalledProcessError as exc:
        write_log("Error")


def factory_reset():
    command_reset = [sys.executable, "molto2.py", "--factoryreset"]
    try:
        subprocess.run(command_reset, check=True)
        write_log("Successful operation ")
    except subprocess.CalledProcessError as exc:
        write_log("Error")


def write_seed_only():
    seedtextbox = ui.lineEdit.text()
    profilecombobox = ui.comboBox.currentText()
    if ui.checkBox.isChecked():
        command_write_seed_only = [sys.executable, "molto2.py", "--profile", profilecombobox, "--seed", seedtextbox]
    else:
        command_write_seed_only = [sys.executable, "molto2.py", "--profile", profilecombobox, "--seedbase32",
                                   seedtextbox]
    try:
        subprocess.run(command_write_seed_only, check=True)
        write_log("Successful operation ")
    except subprocess.CalledProcessError as exc:
        write_log("Error")


def provision_without_config():
    seedtextbox = ui.lineEdit.text()
    profilecombobox = ui.comboBox.currentText()
    titletextbox = ui.lineEdit_2.text()
    if ui.checkBox.isChecked():
        command_write_seed_only = [sys.executable, "molto2.py", "--profile", profilecombobox, "--seed", seedtextbox,
                                   "--title", titletextbox]
    else:
        command_write_seed_only = [sys.executable, "molto2.py", "--profile", profilecombobox, "--seedbase32",
                                   seedtextbox, "--title", titletextbox]
    try:
        subprocess.run(command_write_seed_only, check=True)
        write_log("Successful operation ")
    except subprocess.CalledProcessError as exc:
        write_log("Error")


def provision_with_config():
    # Timestep
    timestep = "1"
    algorithm = "1"
    display_timeout = "1"
    otp_length = "6"
    if ui.comboBox_2.currentText() == "30s":
        timestep = "1"
    elif ui.comboBox_2.currentText() == "60s":
        timestep = "2"
    # Algorithm
    if ui.comboBox_3.currentText() == "SHA1":
        algorithm = "1"
    elif ui.comboBox_3.currentText() == "SHA256":
        algorithm = "2"
    # DisplayTimeout
    if ui.comboBox_4.currentText() == "15s":
        display_timeout = "0"
    elif ui.comboBox_4.currentText() == "30s":
        display_timeout = "1"
    elif ui.comboBox_4.currentText() == "60s":
        display_timeout = "2"
    elif ui.comboBox_4.currentText() == "120s":
        display_timeout = "3"
    # OTP Length
    otp_length = ui.comboBox_5.currentText()

    seedtextbox = ui.lineEdit.text()
    profilecombobox = ui.comboBox.currentText()
    titletextbox = ui.lineEdit_2.text()
    if ui.checkBox.isChecked():
        if ui.checkBox_3.isChecked():
            command_write_seed_only = [sys.executable, "molto2.py", "--config", "--synctime", "--profile",
                                       profilecombobox, "--seed", seedtextbox, "--title", titletextbox,
                                       "--display_timeout", display_timeout, "--algorithm", algorithm, "--timestep",
                                       timestep, "--otpdigits", otp_length]
        else:
            command_write_seed_only = [sys.executable, "molto2.py", "--config", "--profile", profilecombobox, "--seed",
                                       seedtextbox, "--title", titletextbox, "--display_timeout", display_timeout,
                                       "--algorithm", algorithm, "--timestep", timestep, "--otpdigits", otp_length]
    else:
        if ui.checkBox_3.isChecked():
            command_write_seed_only = [sys.executable, "molto2.py", "--config", "--synctime", "--profile",
                                       profilecombobox, "--seedbase32", seedtextbox, "--title", titletextbox,
                                       "--display_timeout", display_timeout, "--algorithm", algorithm, "--timestep",
                                       timestep, "--otpdigits", otp_length]
        else:
            command_write_seed_only = [sys.executable, "molto2.py", "--config", "--profile", profilecombobox,
                                       "--seedbase32", seedtextbox, "--title", titletextbox, "--display_timeout",
                                       display_timeout, "--algorithm", algorithm, "--timestep", timestep, "--otpdigits",
                                       otp_length]
    try:
        subprocess.run(command_write_seed_only, check=True)
        write_log("Successful operation ")
    except subprocess.CalledProcessError as exc:
        write_log("Error")


def apply_only_config():
    # Timestep
    timestep = "1"
    algorithm = "1"
    display_timeout = "1"
    otp_length = "6"
    if ui.comboBox_2.currentText() == "30s":
        timestep = "1"
    elif ui.comboBox_2.currentText() == "60s":
        timestep = "2"
    # Algorithm
    if ui.comboBox_3.currentText() == "SHA1":
        algorithm = "1"
    elif ui.comboBox_3.currentText() == "SHA256":
        algorithm = "2"
    # DisplayTimeout
    if ui.comboBox_4.currentText() == "15s":
        display_timeout = "0"
    elif ui.comboBox_4.currentText() == "30s":
        display_timeout = "1"
    elif ui.comboBox_4.currentText() == "60s":
        display_timeout = "2"
    elif ui.comboBox_4.currentText() == "120s":
        display_timeout = "3"
    # OTP Length
    otp_length = ui.comboBox_5.currentText()
    profilecombobox = ui.comboBox.currentText()
    if ui.checkBox_3.isChecked():
        command_write_seed_only = [sys.executable, "molto2.py", "--config", "--synctime", "--profile", profilecombobox,
                                   "--display_timeout", display_timeout,
                                   "--algorithm", algorithm, "--timestep", timestep, "--otpdigits", otp_length]
    else:
        command_write_seed_only = [sys.executable, "molto2.py", "--config", "--profile", profilecombobox,
                                   "--display_timeout", display_timeout,
                                   "--algorithm", algorithm, "--timestep", timestep, "--otpdigits", otp_length]
    try:
        subprocess.run(command_write_seed_only, check=True)
        write_log("Successful operation ")
    except subprocess.CalledProcessError as exc:
        write_log("Error")


def provision():
    if ui.checkBox_2.isChecked():
        provision_with_config()
    else:
        provision_without_config()


def remove_seed():
    profilecombobox = ui.comboBox.currentText()
    zero = "AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA"
    command_remove_seed = [sys.executable, "molto2.py", "--profile", profilecombobox, "--seedbase32", zero]
    try:
        subprocess.run(command_remove_seed, check=True)
        write_log("Successful operation")
    except subprocess.CalledProcessError as exc:
        write_log("Error")


def clear_log():
    # ui.tableWidget.clear()
    ui.tableWidget.setRowCount(0)


def write_log(error):
    serial = ui.serial.text()
    rowcount = ui.tableWidget.rowCount()
    ui.tableWidget.insertRow(rowcount)
    ui.tableWidget.setItem(rowcount, 0, QTableWidgetItem(serial))
    ui.tableWidget.setItem(rowcount, 1, QTableWidgetItem(error))


def lock_device():
    command_lock_device = [sys.executable, "molto2.py", "--lock"]
    try:
        subprocess.run(command_lock_device, check=True)
        write_log("Successful operation")
    except subprocess.CalledProcessError as exc:
        write_log("Error")


def unlock_device():
    command_unlock_device = [sys.executable, "molto2.py", "--unlock"]
    try:
        subprocess.run(command_unlock_device, check=True)
        write_log("Successful operation")
    except subprocess.CalledProcessError as exc:
        write_log("Error")


ui.pushButton_9.clicked.connect(unlock_device)
ui.pushButton.clicked.connect(lock_device)
ui.pushButton_3.clicked.connect(set_title)
ui.pushButton_6.clicked.connect(factory_reset)
ui.pushButton_2.clicked.connect(write_seed_only)
ui.pushButton_7.clicked.connect(remove_seed)
ui.pushButton_8.clicked.connect(clear_log)
ui.pushButton_5.clicked.connect(provision)
ui.pushButton_4.clicked.connect(apply_only_config)
ui.timer.timeout.connect(connection)
ui.timer.start()
sys.exit(app.exec())
