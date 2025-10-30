import sys
from PyQt6.QtGui import QIcon
from PyQt6.QtWidgets import QApplication, QWidget, QLineEdit, QPushButton, QTextEdit, QVBoxLayout, QLabel

class window(QWidget):

   def __init__(self, parent = None):
      super(window, self).__init__(parent)
      self.resize(600,200)
      self.setWindowIcon(QIcon('window.png'))
      self.setWindowTitle("Python GUI Template")
      # Initialize layout
      layout = QVBoxLayout()
      self.setLayout(layout)
      # widgets
      self.inputField = QLineEdit()
      button = QPushButton('&Say Hello', clicked=self.sayHello)
      # button.clicked.connect(self.sayHello)
      self.output = QTextEdit()
      # add widgets to layout
      layout.addWidget(self.inputField)
      layout.addWidget(button)
      layout.addWidget(self.output)

   def sayHello(self):
       inputText = self.inputField.text()
       self.output.setText('Hello {0}'.format(inputText))
       # self.output.setText(f'Hello {inputText}')

def main():
   app = QApplication(sys.argv)
   app.setStyleSheet('''
        QWidget {
            font-size: 25px;
        }
        
        QPushButton {
            font-size: 20px;
        }
   ''')
   myApp = window()
   myApp.show()
   sys.exit(app.exec())

if __name__ == '__main__':
   main()
