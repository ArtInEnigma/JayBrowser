import sys
from PyQt5.QtCore import QUrl, Qt
from PyQt5.QtGui import QIcon, QGuiApplication
from PyQt5.QtWebEngineWidgets import QWebEngineView
from PyQt5.QtWidgets import (QApplication, QHBoxLayout, QLineEdit, QVBoxLayout, QWidget,QToolButton, QTabWidget)

class Browser(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Web Browser")
        self.setGeometry(100, 100, 800, 600)

        # Create the search bar
        self.search_bar = QLineEdit(self)
        self.search_bar.setPlaceholderText("Search Google or type URL")
        self.search_bar.setFixedWidth(575)
        self.search_bar.setFixedHeight(30)
        self.search_bar.setStyleSheet("margin: 5px 3px; height: 35px; width: 120px color: #5c5c5c; border: none; background-color: #f2f2f; font-weight: bold; ")
        self.search_bar.setAlignment(Qt.AlignCenter)

        # Create the tab widget
        self.tab_widget = QTabWidget(self)
        self.tab_widget.setTabsClosable(True)
        self.tab_widget.tabCloseRequested.connect(self.close_tab)

        # Create the tool bar
        self.tool_bar = QHBoxLayout()

        # Create the back button
        self.back_button = QToolButton(self)
        self.back_button.setIcon(QIcon("back.png"))
        self.back_button.clicked.connect(self.go_back)
        self.tool_bar.addWidget(self.back_button)

        # Create the forward button
        self.forward_button = QToolButton(self)
        self.forward_button.setIcon(QIcon("forward.png"))
        self.forward_button.clicked.connect(self.go_forward)
        self.tool_bar.addWidget(self.forward_button)

        # Create the reload button
        self.reload_button = QToolButton(self)
        self.reload_button.setIcon(QIcon("reload.png"))
        self.reload_button.clicked.connect(self.reload_page)
        self.tool_bar.addWidget(self.reload_button)

        # Create the new tab button
        self.new_tab_button = QToolButton(self)
        self.new_tab_button.setIcon(QIcon("newtab.png"))
        self.new_tab_button.clicked.connect(self.new_tab)
        self.tool_bar.addWidget(self.new_tab_button)

        # Create the layout
        layout = QVBoxLayout(self)
        layout.addLayout(self.tool_bar)
        layout.addWidget(self.search_bar,0,Qt.AlignHCenter)
        layout.addWidget(self.tab_widget)

        # Connect the search bar to the web view
        self.search_bar.returnPressed.connect(self.load_url)

        # Create the initial web view and tab
        self.new_tab()

    def new_tab(self):
        web_view = QWebEngineView(self)
        index = self.tab_widget.addTab(web_view, "New Tab")
        self.tab_widget.setCurrentIndex(index)
        web_view.urlChanged.connect(self.update_tab_title)
        web_view.loadFinished.connect(self.update_tab_icon)

    def close_tab(self, index):
        self.tab_widget.removeTab(index)

    def update_tab_title(self, url):
        web_view = self.tab_widget.currentWidget()
        index = self.tab_widget.indexOf(web_view)
        self.tab_widget.setTabText(index, web_view.title())

    def update_tab_icon(self):
        web_view = self.tab_widget.currentWidget()
        index = self.tab_widget.indexOf(web_view)
        self.tab_widget.setTabIcon(index, web_view.icon())

    def load_url(self):
        url = self.search_bar.text()
        if not url.startswith("http"):
            url = "https://www.google.com/search?q=" + url
        web_view = self.tab_widget.currentWidget()
        web_view.setUrl(QUrl(url))

    def go_back(self):
        web_view = self.tab_widget.currentWidget()
        if web_view:
            web_view.back()
    def go_forward(self):
        web_view = self.tab_widget.currentWidget()
        if web_view:
            web_view.forward()
    def reload_page(self):
        web_view = self.tab_widget.currentWidget()
        if web_view:
            web_view.reload()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    browser = Browser()
    browser.show()
    sys.exit(app.exec_())
