import sys, ctypes, threading
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QLabel, QPushButton, QLineEdit, QRadioButton, QButtonGroup
from PyQt5.QtGui import QIcon, QFont
from PyQt5.QtCore import Qt

# TODO:
# - Add the encrypt and decrypt functions

# App ID for the taskpar icon (Windows)
app_id = 'File Encrypter'
if sys.platform == 'win32':
    ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID(app_id)

# Window class
class MainWindow(QMainWindow):

    # Constructor
    def __init__(self):
        super().__init__()
        self.setWindowTitle("File Encrypter")
        self.setGeometry(100, 100, 400, 200)
        self.setFixedSize(self.width(), self.height())
        self.setWindowIcon(QIcon('./assets/icon.png'))
        self.setStyleSheet("background-image: url(./assets/main_bg.jpg);")

        self.initUI()

    # Initialize the UI
    def initUI(self):
        
        # Label for the delay
        delay_label = QLabel("Path to file:", self)
        delay_label.setFont(QFont('Arial', 12))
        delay_label.setGeometry(50, 15, 100, 30)
        delay_label.setStyleSheet("color: white;"
                                  "padding: 5px;")
        
        # Input field for the delay
        self.delay_input = QLineEdit(self)
        self.delay_input.setGeometry(150, 15, 200, 30)
        self.delay_input.setStyleSheet("color: white;"
                                       "padding: 5px;"
                                       "border: 1px solid white;"
                                       "font-size: 12px;")
        
        # Encrypt button
        encrypt_button = QPushButton("Encrypt", self)
        encrypt_button.setGeometry(150, 50, 100, 30)
        encrypt_button.setStyleSheet("color: white;"
                                     "padding: 5px;")
       # encrypt_button.clicked.connect(self.encrypt)

        # Decrypt button
        decrypt_button = QPushButton("Decrypt", self)
        decrypt_button.setGeometry(250, 50, 100, 30)
        decrypt_button.setStyleSheet("color: white;"
                                     "padding: 5px;")
       # decrypt_button.clicked.connect(self.decrypt)

def Main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    Main()