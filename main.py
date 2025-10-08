import webbrowser
import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtWebEngineWidgets import QWebEngineView
from PyQt5.QtCore import QUrl
from colorama import Fore

print(Fore.RED + """                                        
__  ________   _   ______  __________  ____  __ __
\ \/ /_  __/  / | / / __ \/ ____/ __ \/ __ \/ //_/   |
 \  / / /    /  |/ / / / / /   / / / / / / / ,<      | Github.com/egoodev 
 / / / /    / /|  / /_/ / /___/ /_/ / /_/ / /| |     |--------------------
/_/ /_/    /_/ |_/\____/\____/\____/\____/_/ |_|     |
Watch Youtube Video Without Ads and Cookies | By Ego |
      """)                      
yt = input("Enter YT Link: " + Fore.WHITE)
nocook = yt.replace("youtube", "yout-ube")
class Browser(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Youtube | TNC - YT No Cookies | By Ego")
        self.setGeometry(100, 100, 1000, 600)

        self.browser = QWebEngineView()
        self.browser.setUrl(QUrl(nocook))
        self.setCentralWidget(self.browser)

app = QApplication(sys.argv)
window = Browser()
window.show()
sys.exit(app.exec_())
