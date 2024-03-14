

from mlProject.components.data_Transformation import data_TransformationClass
import pandas as pd


class dataTransformationInitiatorClass():
    def __init__(self):
        self.data_TransformationObj = data_TransformationClass()
        self.cleaned_DataFile_Path = "artifacts/cleanedDataFile.csv"

    def dataTransformationInitiatorMethod(self):
        listOfColumns = ['RowNumber', 'Loan_ID', 'CustomerId','Surname','Credit_History']
        print("-------------------------------------------------------")
        df = pd.read_csv("D:/MLProjects/Finance Projects/LoanEligibilityStatus01/artifacts/rawDataSet.csv")
        print("-------------------------------------------------------")
        
        print(df)
        df =  self.data_TransformationObj.DropColumns(listOfColumns,df)
        df =  self.data_TransformationObj.ReplaceWithCorrectValue(colName='Dependents',valuesToReplace={'3+':3},df=df)
        df =  self.data_TransformationObj.ReplaceWithCorrectValue(colName='Loan_Status',valuesToReplace={'Y':1,'N':0},df=df)
        df =  self.data_TransformationObj.ReplaceWithCorrectValue(colName='Designation',valuesToReplace={'Assistant Vice President':'AVP','Ma nager': 'Manager'},df=df)
        df =  self.data_TransformationObj.ReplaceWithCorrectValue(colName='Married',valuesToReplace={'No':'Single'},df=df)
        columnName = ['Self_Employed','Married','Dependents']
        df = self.data_TransformationObj.replaceWithMode(columnName,df)
        # Replacing the 'Self_Employed','Married' with mode  
        columnName1 = ['LoanAmount']
        df = self.data_TransformationObj.replaceWithMean(columnName1,df)
        df = self.data_TransformationObj.removeOutlier(colName='ApplicantIncome',df=df,LowerQuantile=.20,HigherQuantile=.80)
        df = self.data_TransformationObj.removeOutlier(colName='NumOfProducts',df=df,LowerQuantile=.10,HigherQuantile=.90)
        
        df.to_csv(self.cleaned_DataFile_Path, index=False)  # Save as CSV without index
        print(df)