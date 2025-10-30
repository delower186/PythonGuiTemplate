from PyQt6.QtWidgets import QMessageBox


def show_info_messagebox(text):
    msg = QMessageBox()
    msg.setIcon(QMessageBox.Icon.Information)
    msg.setText(text)
    msg.setWindowTitle("Information")
    msg.setStandardButtons(QMessageBox.StandardButton.Ok | QMessageBox.StandardButton.Cancel)
    retval = msg.exec()
    return retval  # if 'OK' button clicked 'retval' is 1024, if 'Cancel' button clicked 'retval' is 4194304

def show_warning_messagebox(text):
   msg = QMessageBox()
   msg.setIcon(QMessageBox.Icon.Warning)
   msg.setText(text)
   msg.setWindowTitle("Warning")
   msg.setStandardButtons(QMessageBox.StandardButton.Ok | QMessageBox.StandardButton.Cancel)
   retval = msg.exec()
   return retval # if 'OK' button clicked 'retval' is 1024, if 'Cancel' button clicked 'retval' is 4194304

def show_question_messagebox(text):
   msg = QMessageBox()
   msg.setIcon(QMessageBox.Icon.Question)
   msg.setText(text)
   msg.setWindowTitle("Question")
   msg.setStandardButtons(QMessageBox.StandardButton.Ok | QMessageBox.StandardButton.Cancel)
   retval = msg.exec()
   return retval # if 'OK' button clicked 'retval' is 1024, if 'Cancel' button clicked 'retval' is 4194304

def show_critical_messagebox(text):
   msg = QMessageBox()
   msg.setIcon(QMessageBox.Icon.Critical)
   msg.setText(text)
   msg.setWindowTitle("Critical")
   msg.setStandardButtons(QMessageBox.StandardButton.Ok | QMessageBox.StandardButton.Cancel)
   retval = msg.exec()
   return retval # if 'OK' button clicked 'retval' is 1024, if 'Cancel' button clicked 'retval' is 4194304