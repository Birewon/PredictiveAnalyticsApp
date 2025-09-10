from PyQt5 import QtWidgets
import sys
import os
import pandas as pd
from CSVeditor.AppSettings3 import Ui_MainWindow
from UI_logic import UICallbacks

# os.environ["QT_SCALE_FACTOR"] = "2"
os.environ["QT_AUTO_SCREEN_SCALE_FACTOR"] = "1"
# QApplication.setAttribute(Qt.AA_EnableHighDpiScaling)

class mywindow(QtWidgets.QMainWindow):
    def __init__(self):
        super(mywindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.callbacks = UICallbacks(self)

        self.dfs = []
        self.OUTPUT_PATH = ""
        self.RESPONSE_TEXT = ""

        self.ui.attach_btn_1.clicked.connect(self.callbacks.attach_file_1)
        self.ui.attach_btn_2.clicked.connect(self.callbacks.attach_file_2)
        self.ui.attach_btn_3.clicked.connect(self.callbacks.output_pth)
        self.ui.result_button.clicked.connect(self.callbacks.concat)

    # Functions working with globals variables
    def add_df(self, new_df: pd.DataFrame):
            """
            Adding the df to the file to DFs list.
            Validating addition first and second files

            params:

            new_path: str -> New path for addition to DFs list
            """
            if len(self.dfs) == 2:
                self.dfs.clear()
                return {
                    "msg": "Error! Maximum files",
                    "status": 0
                }
            self.dfs.append(new_df)
            return {
                "new_df": new_df,
                "DFs": self.dfs,
                "status": 1
            }

    def set_output_path(self, output_path: str):
            """
            Saving output path
            """
            self.OUTPUT_PATH = output_path
            return self.OUTPUT_PATH

    def update_response_text(self, response_text: str):
            """
            Adding response text
            """
            self.RESPONSE_TEXT += response_text + "\n"
            return self.RESPONSE_TEXT


def main():
    app = QtWidgets.QApplication([])
    application = mywindow()
    application.show()

    sys.exit(app.exec())


if __name__ == "__main__":
    main()