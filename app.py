import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QPushButton, QVBoxLayout, QMessageBox, QPlainTextEdit

class PasswordManager(QWidget):
    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        self.setWindowTitle('Password Manager')

        label = QLabel('Enter your password to access the password manager:')
        self.password_input = QLineEdit(self)
        self.password_input.setEchoMode(QLineEdit.Password)
        button = QPushButton('Enter', self)

        layout = QVBoxLayout()
        layout.addWidget(label)
        layout.addWidget(self.password_input)
        layout.addWidget(button)
        self.setLayout(layout)

        button.clicked.connect(self.check_password)
        self.password_input.returnPressed.connect(self.check_password)

    def check_password(self):
        if self.password_input.text() == 'yourpassword':
            self.password_storage = PasswordStorage()
            self.password_storage.show()
        else:
            QMessageBox.critical(self, 'Error', 'Incorrect password')

class PasswordStorage(QWidget):
    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        self.setWindowTitle('Password Storage')

        self.plain_text_edit = QPlainTextEdit(self)
        texts = ["Text1", "Text2", "Text3", "Text4", "Text5", "Text6", "Text7", "Text8", "Text9", "Text10", "Text11", "Text12", "Text13", "Text14", "Text15"]
        for text in texts:
            self.plain_text_edit.appendPlainText(text)

        layout = QVBoxLayout()
        layout.addWidget(self.plain_text_edit)
        self.setLayout(layout)


if __name__ == '__main__':
    app = QApplication(sys.argv)

    pm = PasswordManager()
    pm.show()

    sys.exit(app.exec_())
