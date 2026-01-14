from PyQt5.QtWidgets import QDialog, QMessageBox
from ui.label_new import Ui_Dialog

class LabelNewDialog(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        self.result_action = "cancel"
        self.new_name = ""

        self.setWindowTitle("Add New Label")
        self.ui.lineEdit.setFocus()
        self.ui.buttonBox.accepted.disconnect()
        self.ui.buttonBox.accepted.connect(self.on_accept)

    def on_accept(self):
        new_name = self.ui.lineEdit.text().strip()
        if not new_name:
            QMessageBox.warning(self, "Invalid Name", "Label name cannot be empty.")
            return
        self.new_name = new_name
        self.result_action = "accept"
        self.accept()

    def get_result(self):
        return self.result_action, self.new_name
