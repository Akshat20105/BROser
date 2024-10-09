from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import QIcon
from PyQt5.QtWebEngineWidgets import *

class WebBrowser(QMainWindow):
    
    def __init__(self, *args, **kwargs):
        super(WebBrowser, self).__init__(*args, **kwargs)

        self.setWindowTitle("bARowser")
        self.setGeometry(600, 200, 1000, 600)
        self.setWindowIcon(QIcon("icon.png"))

        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)

        self.layout = QVBoxLayout(self.central_widget)

        self.url_bar = QLineEdit()
        self.url_bar.setPlaceholderText("Enter URL or Search here...")
        self.url_bar.setMinimumHeight(40)
        self.url_bar.setStyleSheet("""
            QLineEdit {
                border: 2px solid #007BFF; 
                border-radius: 15px; 
                padding: 5px;
            }
        """)

        self.horizontal = QHBoxLayout()
        
        self.reload_btn = QPushButton("⟲")  # Reload button with emoji
        self.reload_btn.setMinimumSize(40, 40)
        self.reload_btn.setStyleSheet("""
            QPushButton {
                background-color: #FFFFFF; 
                color: Blue; 
                border: none; 
                border-radius: 20px; 
                font-size: 24px; 
            }
            QPushButton:hover {
                background-color: #BBBBBB;
            }
        """)
        
        self.back_btn = QPushButton("◀")
        self.back_btn.setMinimumSize(40, 40)
        self.back_btn.setStyleSheet("""
            QPushButton {
                background-color: #007BFF; 
                color: white; 
                border: none; 
                border-radius: 20px; 
                font-size: 32px; 
            }
            QPushButton:hover {
                background-color: #0056b3;
            }
        """)

        self.go_btn = QPushButton("Go")
        self.go_btn.setMinimumSize(40, 40)
        self.go_btn.setStyleSheet("""
            QPushButton {
                background-color: #007BFF; 
                color: white; 
                border: none; 
                border-radius: 20px; 
                font-size: 20px; 
            }
            QPushButton:hover {
                background-color: #0056b3;
            }
        """)

        self.forward_btn = QPushButton("▶")
        self.forward_btn.setMinimumSize(40, 40)
        self.forward_btn.setStyleSheet("""
            QPushButton {
                background-color: #007BFF; 
                color: white; 
                border: none; 
                border-radius: 20px; 
                font-size: 32px; 
            }
            QPushButton:hover {
                background-color: #0056b3;
            }
        """)

        self.horizontal.addWidget(self.back_btn)
        self.horizontal.addWidget(self.go_btn)
        self.horizontal.addWidget(self.forward_btn)
        self.horizontal.addWidget(self.url_bar)    
        self.horizontal.addWidget(self.reload_btn)

        self.layout.addLayout(self.horizontal)

        # Create the QWebEngineView and set up media playback
        self.browser = QWebEngineView()
        self.browser.setUrl(QUrl("http://google.com"))
        
        # Enable media playback
        self.browser.settings().setAttribute(QWebEngineSettings.AutoLoadImages, True)
        self.browser.settings().setAttribute(QWebEngineSettings.JavascriptEnabled, True)
        self.browser.settings().setAttribute(QWebEngineSettings.FullScreenSupportEnabled, True)
        self.browser.settings().setAttribute(QWebEngineSettings.AllowRunningInsecureContent, True)
        self.browser.settings().setAttribute(QWebEngineSettings.LocalStorageEnabled, True)
        self.browser.settings().setAttribute(QWebEngineSettings.PlaybackRequiresUserGesture, False)  # Allow autoplay
        
        self.layout.addWidget(self.browser)

        # Connect button actions
        self.back_btn.clicked.connect(self.browser.back)
        self.forward_btn.clicked.connect(self.browser.forward)
        self.reload_btn.clicked.connect(self.browser.reload)
        self.go_btn.clicked.connect(self.navigate_to_url)
        self.url_bar.returnPressed.connect(self.navigate_to_url)

        # Error handling
        self.browser.loadFinished.connect(self.check_for_errors)

    def navigate_to_url(self):
        url = self.url_bar.text()
        if not url.startswith("http"):
            url = "https://www.google.com/search?q=" + url
        self.browser.setUrl(QUrl(url))
        self.url_bar.setText(url)

    def check_for_errors(self, success):
        if not success:
            with open('error_page.html', 'r') as file:
                error_html = file.read()
            self.browser.setHtml(error_html)

if __name__ == "__main__":
    app = QApplication([])
    window = WebBrowser()
    window.show()
    app.exec_()
