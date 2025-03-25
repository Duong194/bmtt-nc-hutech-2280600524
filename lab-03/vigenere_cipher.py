import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox
from ui.vigenere import Ui_MainWindow  # Đổi từ caesar sang vigenere
import requests
import re  # Thêm thư viện regex để kiểm tra dữ liệu đầu vào

class VigenereApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.btn_encrypt.clicked.connect(self.call_api_encrypt)
        self.ui.btn_decrypt.clicked.connect(self.call_api_decrypt)
        
    def validate_input(self, text, key):
        """Hàm kiểm tra chỉ nhập chữ (không số, không ký tự đặc biệt)"""
        if not re.fullmatch(r"[A-Za-z]+", text):
            self.show_error("Plaintext chỉ được chứa chữ cái (A-Z, a-z)!")
            return False
        if not re.fullmatch(r"[A-Za-z]+", key):
            self.show_error("Key chỉ được chứa chữ cái (A-Z, a-z)!")
            return False
        return True

    def show_error(self, message):
        """Hiển thị thông báo lỗi"""
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Warning)
        msg.setText(message)
        msg.exec_()

    def call_api_encrypt(self):
        url = "http://127.0.0.1:5000/api/vigenere/encrypt"
        plain_text = self.ui.txt_plain_text.toPlainText().strip()
        key = self.ui.txt_key.toPlainText().strip()

        # Kiểm tra dữ liệu nhập vào
        if not self.validate_input(plain_text, key):
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
            print("Error:", e)
    
    def call_api_decrypt(self):
        url = "http://127.0.0.1:5000/api/vigenere/decrypt"
        cipher_text = self.ui.txt_cipher_text.toPlainText().strip()
        key = self.ui.txt_key.toPlainText().strip()

        # Kiểm tra dữ liệu nhập vào
        if not self.validate_input(cipher_text, key):
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
            print("Error:", e)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = VigenereApp()
    window.show()
    sys.exit(app.exec_())
