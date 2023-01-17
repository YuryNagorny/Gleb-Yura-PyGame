import sys
import traceback
from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QMainWindow, QInputDialog, QMessageBox, QLineEdit
from PyQt5 import QtCore, QtWidgets
from sqlBH import *


class Registration(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi(r'C:\Users\user\Desktop\pythonProject4\ui_registration', self)
        self.setWindowTitle('Bullet-Hell')
        self.reg_window.hide()

    def log_to_reg(self):  # переключение между окнами входа и регистрации
        self.to_reg_btn.clicked.connect(lambda: self.log_window.hide())
        self.to_reg_btn.clicked.connect(lambda: self.reg_window.show())

    def reg_to_log(self):  # переключение между окнами регистрации и входа
        self.to_log_btn.clicked.connect(lambda: self.reg_window.hide())
        self.to_log_btn.clicked.connect(lambda: self.log_window.show())

    def __reg(self):  # регистрация пользователя
        login = ex.login_reg.text()
        password1 = ex.password1.text()
        password2 = ex.password2.text()
        if len(login) < 3:
            ex.error_reg2.setText("Длина логина должна быть больше 3-ёх")
        else:
            ex.error_reg2.setText("")
        if len(password1) < 8:
            ex.error_reg3.setText("Длина пароля должна быть больше 8-ми")
        else:
            ex.error_reg3.setText("")
            if password1 == password2:
                ex.error_reg4.setText("")
                res = reg(login, password1)
                if res["status"]:
                    ex.reg_window.hide()
                    ex.account.show()
                    self.session["id"] = res["id"]
                    msg_box = QMessageBox(ex)
                    msg_box.setText(res["msg"])
                    msg_box.show()
                    self.Greeting.setText(f'Доброго времени суток, {login}!')
                    kills_res = return_kills(self.session["id"])
                    sec_res = return_seconds(self.session["id"])
                    kills_place = return_kills_place(self.session["id"])
                    sec_place = return_max_sec_place(self.session["id"])
                    self.log_flag = True
                else:
                    ex.error_reg1.setText("Такой логин занят!")
            else:
                ex.error_reg4.setText("Пароли должны совпадать!")

    def __log(self):  # вход пользователя в свой профиль
        login = ex.login_log.text()
        password = ex.password_log.text()
        res = log(login, password)
        if res["status"]:
            self.session["id"] = res["id"]
            ex.log_window.hide()
            ex.account.show()
            msg_box = QMessageBox(ex)
            msg_box.setText(res["msg"])
            msg_box.show()
            self.log_flag = True
            kills_res = return_kills(self.session["id"])
            sec_res = return_seconds(self.session["id"])
            kills_place = return_kills_place(self.session["id"])
            sec_place = return_max_sec_place(self.session["id"])
        else:
            ex.err_msg_log.setText(res["msg"])

    def __clear_log_and_reg(self):  # очистка окон регистрации и входа
        ex.login_log.setText("")
        ex.password_log.setText("")
        ex.login_reg.setText("")
        ex.password1.setText("")
        ex.password2.setText("")
        ex.error_log.setText("")
        ex.error_reg1.setText("")
        ex.error_reg2.setText("")
        ex.error_reg3.setText("")
        ex.error_reg4.setText("")

    def __leave_profile(self):  # обработка выхода пользователя из профиля
        self.__clear_log_and_reg()
        self.session.pop("id")
        ex.account.hide()
        ex.reg_window.hide()
        ex.log_window.show()
        self.log_flag = False

    def __del_profile(self):  # обработка удаления пользователем своего профиля
        password, ok = QInputDialog.getText(
            ex,
            "Внимание!",
            "Введите пароль:",
            QLineEdit.Password
        )
        if ok:
            password_res = check_password(self.session["id"], password)
            if password_res["status"]:
                del_res = del_profile(self.session["id"])
                self.__leave_profile()
                msg_box = QtWidgets.QMessageBox(ex)
                msg_box.setWindowTitle("Внимание!")
                msg_box.setText(del_res["msg"])
                msg_box.show()
                self.log_flag = False
            else:
                msg_box = QMessageBox(ex)
                msg_box.setWindowTitle("Внимание!")
                msg_box.setText("Неверный пароль!")
                msg_box.show()


def excepthook(exc_type, exc_value, exc_tb):
    tb = "".join(traceback.format_exception(exc_type, exc_value, exc_tb))
    print("Oбнаружена ошибка !:", tb)


if __name__ == '__main__':
    sys.excepthook = excepthook
    app = QApplication(sys.argv)
    ex = Registration()
    ex.reg_to_log()
    ex.log_to_reg()
    ex.show()
    sys.exit(app.exec_())