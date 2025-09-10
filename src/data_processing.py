import pandas as pd

    # The class working with DataFrames
class DataProcessing:
    """
    This class working with DataFrames
    """
    def read_csv_file(self, file_path: str):
            """
            Reading .csv file.
            Returns DataFrame or None
            """
            try:
                df = pd.read_csv(file_path, sep=',', header=0, na_values=['','N/A'])
                return {
                    "status": 1,
                    "msg": df
                }
            except FileNotFoundError as ex:
                return {
                    "status": 0,
                    "msg": f"[ERROR]: {ex}"
                }
            except Exception as ex:
                return {
                    "status": 0,
                    "msg": f"[ERROR]: {ex}"
                }

    def save_dataframe_to_csv(self, df: pd.DataFrame, output_full_path: str, index: bool | None = False):
            """
            Saving the DataFrame to .csv file to path
            """
            if df is None:
                return {
                    "status": 0,
                    "msg": "[ERROR]: The DataFrame is empty."
                }
            try:
                df.to_csv(output_full_path, index=index)
                file_name = output_full_path.split('/')[-1]
                return {
                    "status": 1,
                    "msg": f"Successfuly saving the new file: {file_name}"
                }
            except Exception as ex:
                return {
                    "status": 0,
                    "msg": f"[ERROR]: {ex}"
                }

    def concat_files(self, file1_df: pd.DataFrame, file2_df: pd.DataFrame, output_path: str,  filename: str | None = "new_file", axis: int | None = 1, index: bool | None = False):
            """
            Concating two files
            """
            try:
                new_file = pd.concat([file1_df, file2_df], axis=axis)
                full_output_path = output_path + "/" + filename + ".csv"
                raw_name = self.save_dataframe_to_csv(new_file, full_output_path, index=index)
                return {
                    "status": 1,
                    "msg": raw_name.get("msg")
                }
            except Exception as ex:
                 return {
                    "status": 0,
                    "msg": f"[ERROR]: {ex}"
                 }

    def get_file_columns(self, file_path: str) -> list:
            """
            Reading the csv file and return:
            Successfuly: the list of columns names
            Error: Error message
            """
            try:
                df = pd.read_csv(file_path, sep=',', header=0, na_values=['', 'N/A'])
                return {
                    "status": 1,
                    "response": list(df.columns())
                }
            except FileNotFoundError as ex:
                return {
                    "status": 0,
                    "msg": f"[ERROR]: {ex}"
                }