import time

from PyQt6.QtWidgets import QProgressBar

class ProgressBar(QProgressBar):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setMaximum(100)
        self.changeColor('#999999')
        self.setTextVisible(True)
        self._active = False

    def updateBar(self, i):
        while True:
            time.sleep(0.01)
            value= self.value() + i
            self.setValue(value)
            self.setFormat("Loggin in ........... %p%")
            if value >= 20:
                self.changeColor('#2a91d8')
                self.setFormat("Logged in ........... %p%")
            if value >= 40:
                self.changeColor('#f2bb46')
                self.setFormat("Connecting ........... %p%")
            if value >= 60:
                self.changeColor('#ca5952')
                self.setFormat("Connected ........... %p%")
            if value >= 80:
                self.changeColor('#59a84b')
                self.setFormat("Ready ........... %p%")

            if value >= self.maximum() or self._active:
                self.setValue(100)
                break
            elif value >= self.maximum() or not self._active:
                break

    def changeColor(self, color):
        css = """
            ::chunk {{
                background: {0};
            }}
        """.format(color)
        self.setStyleSheet(css)