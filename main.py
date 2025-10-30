import sys
from PyQt6.QtGui import QIcon
from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QApplication, QWidget, QLineEdit, QPushButton, QGridLayout, QLabel, QFileDialog, \
    QTableWidget, QTableWidgetItem
from ProgressBar import ProgressBar
import pandas as pd
from Alerts import show_info_messagebox

class Window(QWidget):

   def __init__(self, parent = None):
      super(Window, self).__init__(parent)
      self.resize(800,400)
      self.setWindowIcon(QIcon('window.png'))
      self.setWindowTitle("Python GUI Template")
      # Initialize layout
      layout = QGridLayout()
      self.setLayout(layout)
      # Progress bar -------------------
      self.progressBar = ProgressBar()
      layout.addWidget(self.progressBar, 1, 0, 1, 2)

      self.button = QPushButton('Check Status', clicked=self.update_progress_bar)
      layout.addWidget(self.button, 2, 0, 1, 2)
      # Worksheet Name -------------------
      self.worksheet_input = QLineEdit()
      self.worksheet_input.setPlaceholderText("Worksheet Name")
      layout.addWidget(self.worksheet_input, 3, 0, 1, 2)
      # File Upload Button -------------------
      self.upload_button = QPushButton("Load Data", clicked=self.open_file_dialog)
      layout.addWidget(self.upload_button, 4, 0,
                         alignment=Qt.AlignmentFlag.AlignRight)
      # Data Reset Button -------------
      self.reset_button = QPushButton('Reset', clicked=self.reset_data)
      layout.addWidget(self.reset_button, 4, 1,
                         alignment=Qt.AlignmentFlag.AlignLeft)
      # File Status ------------------
      self.file_label = QLabel("No file selected.")
      layout.addWidget(self.file_label, 5, 0, 1, 2)
      # Load data from excel ----------
      self.table = QTableWidget()
      layout.addWidget(self.table, 6, 0, 1, 2)
      # -------------------------------

   def reset_data(self):
       self.table.setRowCount(0)
       self.table.setColumnCount(0)
       self.file_label.setText("No file selected.")
       show_info_messagebox("Data removed successfully.")

   def load_excel_data(self, excel_file_path):

       worksheet = self.worksheet_input.text()
       try:

           if worksheet == "":
               df = pd.read_excel(excel_file_path)
           else:
               df = pd.read_excel(excel_file_path, worksheet)

           if df.empty:
               print("Empty rows")
               return

           self.table.setRowCount(df.shape[0])
           self.table.setColumnCount(df.shape[1])
           self.table.setHorizontalHeaderLabels(df.columns)

           df.fillna('', inplace=True)
           for row_index, (_, row_values) in enumerate(df.iterrows()):
               for col_index, value in enumerate(row_values):
                   if isinstance(value, (float, int)):
                       value = f"{value:,.0f}"
                   item = QTableWidgetItem(str(value))
                   self.table.setItem(row_index, col_index, item)

           show_info_messagebox("Excel data loaded successfully.")

       except Exception as e:
           import traceback
           print("Error loading Excel file:", e)
           traceback.print_exc()

   def open_file_dialog(self):
        file_path, _ = QFileDialog.getOpenFileName(self, "Select File", "", "All Files (*);;Text Files (*.txt);;Images (*.png *.jpg)")
        if file_path:
            # path = file_path.replace("/", "\\")
            self.file_label.setText(f"Selected file: {file_path}")
            # Load Excel file
            self.load_excel_data(file_path)

        else:
            self.file_label.setText("No file selected.")

   def update_progress_bar(self):
       i = 10
       self.progressBar.updateBar(i)


def main():
   app = QApplication(sys.argv)
   my_app = Window()
   my_app.show()
   sys.exit(app.exec())

if __name__ == '__main__':
   main()
