from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import QIcon, QColor
from PyQt5.QtWebEngineWidgets import *

class WebBrowser(QMainWindow):
    
    def __init__(self, *args, **kwargs):
        super(WebBrowser, self).__init__(*args, **kwargs)

        self.setWindowTitle("Safest Web Browser")
        self.setGeometry(600, 200, 1000, 600)
        self.setWindowIcon(QIcon("icon.png"))

        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)
        self.layout = QVBoxLayout(self.central_widget)

        self.horizontal = QHBoxLayout()

        self.url_bar = QLineEdit()
        self.url_bar.setPlaceholderText("Enter URL here...")
        self.url_bar.setMinimumHeight(30)

        self.go_btn = QPushButton("Go")
        self.go_btn.setMinimumHeight(30)
        self.back_btn = QPushButton("<")
        self.back_btn.setMinimumHeight(30)
        self.forward_btn = QPushButton(">")
        self.forward_btn.setMinimumHeight(30)

        self.dark_light_toggle = QPushButton("Switch to Dark Mode")
        self.dark_mode = False  # Default is Light Mode

        self.horizontal.addWidget(self.url_bar)
        self.horizontal.addWidget(self.go_btn)
        self.horizontal.addWidget(self.back_btn)
        self.horizontal.addWidget(self.forward_btn)
        self.horizontal.addWidget(self.dark_light_toggle)

        self.layout.addLayout(self.horizontal)

        self.browser = QWebEngineView()
        self.layout.addWidget(self.browser)

        self.browser.setUrl(QUrl("http://google.com"))

        self.go_btn.clicked.connect(self.navigate_to_url)
        self.back_btn.clicked.connect(self.browser.back)
        self.forward_btn.clicked.connect(self.browser.forward)
        self.url_bar.returnPressed.connect(self.navigate_to_url)
        self.dark_light_toggle.clicked.connect(self.toggle_dark_light_mode)

        self.browser.loadFinished.connect(self.check_for_errors)

    def navigate_to_url(self):
        url = self.url_bar.text()
        if not url.startswith("http"):
            url = "http://" + url
        self.browser.setUrl(QUrl(url))
        self.url_bar.setText(url)

    def check_for_errors(self, success):
        if not success:
            with open('error_page.html', 'r') as file:
                error_html = file.read()
            self.browser.setHtml(error_html)
            self.browser.urlChanged.connect(self.handle_url_change)

    def handle_url_change(self, url):
        if url.toString() == "back":
            self.browser.back()

    def toggle_dark_light_mode(self):
        if self.dark_mode:
            self.setStyleSheet("QWidget { background-color: white; color: black; }")
            self.url_bar.setStyleSheet("background-color: white; color: black;")
            self.go_btn.setStyleSheet("background-color: lightgray; color: black;")
            self.back_btn.setStyleSheet("background-color: lightgray; color: black;")
            self.forward_btn.setStyleSheet("background-color: lightgray; color: black;")
            self.dark_light_toggle.setText("Switch to Dark Mode")
            self.dark_mode = False
        else:
            self.setStyleSheet("QWidget { background-color: #2E2E2E; color: white; }")
            self.url_bar.setStyleSheet("background-color: #4E4E4E; color: white;")
            self.go_btn.setStyleSheet("background-color: #555555; color: white;")
            self.back_btn.setStyleSheet("background-color: #555555; color: white;")
            self.forward_btn.setStyleSheet("background-color: #555555; color: white;")
            self.dark_light_toggle.setText("Switch to Light Mode")
            self.dark_mode = True

app = QApplication([])
window = WebBrowser()
window.show()
app.exec_()
