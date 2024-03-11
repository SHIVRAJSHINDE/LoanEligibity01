import pandas as pd
import os
import sys
import json
from mlProject.ExceptionLoggerAndUtils.exception import CustomException


class dataIngestionClass():
    """ This class shall be used to read the Data.
        Written By: Shivraj Shinde//Version: 1.0//Revisions: None
    """

    def __init__(self):
        pass

    def readingDataSet(self,File_Path):
        try:
            df = pd.read_csv(File_Path)
            print(df.head())
            return df
        except Exception as e:
            raise CustomException(e,sys)


    def saveDataToFolder(self,df,folder_path):
        try:
            print(df.head())
            if not os.path.exists(folder_path):
                os.makedirs(folder_path)
            file_name = "rawDataSet.csv"  # Name of the CSV file
            file_path = os.path.join(folder_path, file_name)  # Full file path
            df.to_csv(file_path, index=False)  # Save the DataFrame as a CSV file
            print(f"CSV file saved to {file_path}")
        except Exception as e:
            raise CustomException(e,sys)

