from mlProject.ExceptionLoggerAndUtils.exception import CustomException
from mlProject.components.dataIngestion import dataIngestionClass
import sys


class dataIngestionPipeline():
    def __init__(self):
        try:
            self.dataIngestionClass = dataIngestionClass()
            self.File_Path = "D:\MLProjects\ZDatasets\LoanEligibilityTest\Churn_Modelling.csv"
            self.folder_path = "artifacts/"
        except Exception as e:
            raise CustomException(e,sys)

    
    def dataIngestionMethod(self):
        try:
            df = self.dataIngestionClass.readingDataSet(self.File_Path)
            self.dataIngestionClass.saveDataToFolder(df,self.folder_path)
        except Exception as e:
            raise CustomException(e,sys)