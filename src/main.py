from PyQt5 import QtWidgets, QtCore
from PyQt5.QtWidgets import QFileDialog
import sys
import os
import pandas as pd
from CSVeditor.AppSettings3 import Ui_MainWindow
import UI_func

# os.environ["QT_SCALE_FACTOR"] = "2"
os.environ["QT_AUTO_SCREEN_SCALE_FACTOR"] = "1"
# QApplication.setAttribute(Qt.AA_EnableHighDpiScaling)

class mywindow(QtWidgets.QMainWindow):
    def __init__(self):
        super(mywindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        # Signals

        self.ui.attach_btn_1.clicked.connect(self.attach_file_1)
        self.ui.attach_btn_2.clicked.connect(self.attach_file_2)
        self.ui.attach_btn_3.clicked.connect(self.output_pth)
        self.ui.result_button.clicked.connect(self.result)

    # Buttons

    def attach_file_1(self):
        dialog = QFileDialog(self)
        dialog.setFileMode(QFileDialog.FileMode.AnyFile)
        # dialog.setNameFilter("*.csv")
        if dialog.exec_():
            fileName = dialog.selectedFiles()
            if fileName:
                new_path = fileName
                response = UI_func.add_path(new_path)
                if response.get("status") == 1:
                    self.ui.path_text_1.setPlainText(response.get("new_path"))
                    self.ui.listWidget_1.clear()
                    df = pd.read_csv(new_path[0],
                                    sep=',',
                                    header=0,
                                    na_values=['', 'N/A'])
                    csv_columns = list(df.columns)

                    for i in range(0, len(csv_columns)):
                        item_csv = QtWidgets.QListWidgetItem()
                        item_csv.setText(csv_columns[i])
                        item_csv.setFlags(QtCore.Qt.ItemIsUserCheckable | QtCore.Qt.ItemIsEnabled)
                        item_csv.setCheckState(QtCore.Qt.Unchecked)
                        self.ui.listWidget_1.addItem(item_csv)
                else:
                    self.ui.path_text_1.setPlainText(response.get("msg"))


    def attach_file_2(self):
        dialog = QFileDialog(self)
        dialog.setFileMode(QFileDialog.FileMode.AnyFile)
        # dialog.setNameFilter("*.csv")
        if dialog.exec_():
            fileName = dialog.selectedFiles()
            if fileName:
                new_path = fileName
                response = UI_func.add_path(new_path)
                if response.get("status") == 1:
                    self.ui.path_text_2.setPlainText(response.get("new_path"))
                    self.ui.listWidget_2.clear()
                    df = pd.read_csv(new_path[0],
                                    sep=',',
                                    header=0,
                                    na_values=['', 'N/A'])
                    csv_columns = list(df.columns)
                    for i in range(0, len(csv_columns)):
                        item_csv = QtWidgets.QListWidgetItem()
                        item_csv.setText(csv_columns[i])
                        item_csv.setFlags(QtCore.Qt.ItemIsUserCheckable | QtCore.Qt.ItemIsEnabled)
                        item_csv.setCheckState(QtCore.Qt.Unchecked)
                        self.ui.listWidget_2.addItem(item_csv)
                else:
                    self.ui.path_text_2.setPlainText(response.get("msg"))


    def output_pth(self):
        dir_name = QFileDialog.getExistingDirectory(self, "Select a Directory")
        output_path = str(dir_name)
        if output_path:
            if len(UI_func.PATH) == 2:
                self.ui.path_text_3.setPlainText(output_path)
                UI_func.OUTPUT_PATH = output_path
                return
        self.ui.path_text_3.setPlainText("Error!")


    def result(self):
        try:
            file_1 = pd.read_csv(UI_func.PATH[0][0])
            file_2 = pd.read_csv(UI_func.PATH[1][0])
            new_file = pd.concat([file_1, file_2], axis=1) # ADD AXIS MODE
            new_name = [UI_func.OUTPUT_PATH, f"/{self.ui.name_of_output_file_plain_text_1.toPlainText()}.csv"]
            new_file.to_csv(''.join(new_name))
            UI_func.RESPONSE_TEXT += f"Successfully! The new file: {new_name[1][1:]}\n"
            self.ui.status_text.setPlainText(UI_func.RESPONSE_TEXT)
        except ValueError as er:
            UI_func.RESPONSE_TEXT += f"[ERROR]: {er}"
            self.ui.status_text.setPlainText(UI_func.RESPONSE_TEXT)



def main():
    app = QtWidgets.QApplication([])
    application = mywindow()
    application.show()

    sys.exit(app.exec())


if __name__ == "__main__":
    main()