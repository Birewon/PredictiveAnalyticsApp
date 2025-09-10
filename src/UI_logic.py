import pandas as pd
from PyQt5 import QtWidgets, QtCore
from PyQt5.QtWidgets import QFileDialog

from data_processing import DataProcessing


# The class working with UI
class UICallbacks:
    """
    This class working with UI
    """
    def __init__(self, main_window_instance):
        self.main_window = main_window_instance
        self.data_processor = DataProcessing()

    def _populate_list_wiget(self, list_wiget: QtWidgets.QListWidget, columns: list[str]):
        """
        Supporting function for populate list wiget
        """
        for colum in columns:
            item_csv = QtWidgets.QListWidgetItem(colum)
            item_csv.setFlags(QtCore.Qt.ItemIsUserCheckable | QtCore.Qt.ItemIsEnabled)
            item_csv.setCheckState(QtCore.Qt.Unchecked)
            list_wiget.addItem(item_csv)

    def attach_file_1(self):
        dialog = QFileDialog(self.main_window)
        dialog.setFileMode(QFileDialog.FileMode.AnyFile)
        # dialog.setNameFilter("*.csv")
        if dialog.exec_():
            fileName = dialog.selectedFiles()
            if fileName:
                new_path = fileName # ["/home/file.csv"]
                new_df = self.data_processor.read_csv_file(new_path[0])
                try:
                    response = self.main_window.add_df(new_df.get("msg"))
                except Exception as ex:
                    self.main_window.update_response_text(f"[ERROR]: {ex}")
                    self.print_status_text()
                    return
                if response.get("status") == 1:
                    self.main_window.ui.path_text_1.setPlainText(new_path[0])
                    self.main_window.ui.listWidget_1.clear()
                    df = pd.read_csv(new_path[0],
                                    sep=',',
                                    header=0,
                                    na_values=['', 'N/A'])
                    csv_columns = list(df.columns)
                    self._populate_list_wiget(self.main_window.ui.listWidget_1, csv_columns)
                else:
                    self.main_window.ui.path_text_1.setPlainText(response.get("msg"))

    def attach_file_2(self):
        dialog = QFileDialog(self.main_window)
        dialog.setFileMode(QFileDialog.FileMode.AnyFile)
        # dialog.setNameFilter("*.csv")
        if dialog.exec_():
            fileName = dialog.selectedFiles()
            if fileName:
                new_path = fileName
                new_df = self.data_processor.read_csv_file(new_path[0])
                try:
                    response = self.main_window.add_df(new_df.get("msg"))
                except Exception as ex:
                    self.main_window.update_response_text(f"[ERROR]: {ex}")
                    self.print_status_text()
                    return
                if response.get("status") == 1:
                    self.main_window.ui.path_text_2.setPlainText(new_path[0])
                    self.main_window.ui.listWidget_2.clear()
                    df = pd.read_csv(new_path[0],
                                    sep=',',
                                    header=0,
                                    na_values=['', 'N/A'])
                    csv_columns = list(df.columns)
                    self._populate_list_wiget(self.main_window.ui.listWidget_2, csv_columns)
                else:
                    self.main_window.ui.path_text_2.setPlainText(response.get("msg"))

    def output_pth(self):
        dir_name = QFileDialog.getExistingDirectory(self.main_window, "Select a Directory")
        output_path = str(dir_name)
        if output_path:
            if len(self.main_window.dfs) == 2:
                self.main_window.ui.path_text_3.setPlainText(output_path)
                self.main_window.set_output_path(output_path)
                return
        self.main_window.ui.path_text_3.setPlainText("Error!")

    def concat(self):
        try:
            file_1 = self.main_window.dfs[0]
            file_2 = self.main_window.dfs[1]
            response = self.data_processor.concat_files(file_1, file_2, self.main_window.OUTPUT_PATH, self.main_window.ui.name_of_output_file_plain_text_1.toPlainText())
            self.main_window.update_response_text(response.get("msg"))
            self.print_status_text()
        except ValueError as ex:
            self.main_window.update_response_text(f"[ERROR]: {ex}")
            self.print_status_text()

    def print_status_text(self):
        self.main_window.ui.status_text.setPlainText(self.main_window.RESPONSE_TEXT)