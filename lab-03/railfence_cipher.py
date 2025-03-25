import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox
from ui.railfence import Ui_MainWindow
import requests

class MyApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.btn_encrypt.clicked.connect(self.call_api_encrypt)
        self.ui.btn_decrypt.clicked.connect(self.call_api_decrypt)
        
    def validate_input(self, key):
        """Hàm kiểm tra key phải là số nguyên dương"""
        if not key.isdigit() or int(key) <= 0:
            self.show_error("Key phải là một số nguyên dương!")
            return False
        return True

    def show_error(self, message):
        """Hiển thị thông báo lỗi"""
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Warning)
        msg.setText(message)
        msg.exec_()

    def call_api_encrypt(self):
        url = "http://127.0.0.1:5000/api/railfence/encrypt"
        plain_text = self.ui.txt_plain_text.toPlainText().strip()
        key = self.ui.txt_key.toPlainText().strip()

        # Kiểm tra key hợp lệ
        if not self.validate_input(key):
            return
        
        payload = {"plain_text": plain_text, "key": key}
        
        try:
            response = requests.post(url, json=payload)
            if response.status_code == 200:
                data = response.json()
                self.ui.txt_cipher_text.setPlainText(data.get("encrypted_text", "Lỗi: Không có dữ liệu!"))

                msg = QMessageBox()
                msg.setIcon(QMessageBox.Information)
                msg.setText("Encrypted Successfully")
                msg.exec_()
            else:
                print("Error while calling API")
        except requests.exceptions.RequestException as e:
            print("Error:", str(e))
    
    def call_api_decrypt(self):
        url = "http://127.0.0.1:5000/api/railfence/decrypt"
        cipher_text = self.ui.txt_cipher_text.toPlainText().strip()
        key = self.ui.txt_key.toPlainText().strip()

        # Kiểm tra key hợp lệ
        if not self.validate_input(key):
            return
        
        payload = {"cipher_text": cipher_text, "key": key}
        
        try:
            response = requests.post(url, json=payload)
            if response.status_code == 200:
                data = response.json()
                self.ui.txt_plain_text.setPlainText(data.get("decrypted_text", "Lỗi: Không có dữ liệu!"))

                msg = QMessageBox()
                msg.setIcon(QMessageBox.Information)
                msg.setText("Decrypted Successfully")
                msg.exec_()
            else:
                print("Error while calling API")
        except requests.exceptions.RequestException as e:
            print("Error:", str(e))

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec_())
