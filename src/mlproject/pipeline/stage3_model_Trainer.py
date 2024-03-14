from mlProject.ExceptionLoggerAndUtils.utils import save_object
from mlProject.components.model_Trainer import ModelTrainingClass
from mlProject.ExceptionLoggerAndUtils.exception import CustomException

from mlProject.components.data_Transformation import data_TransformationClass
import os
import sys
import pandas as pd

class trainingInitiatorClass():
    def __init__(self):
        self.modelTrainingClassObj = ModelTrainingClass()
        self.transformationFilePath = os.path.join('artifacts', "transformation.pkl")
        self.data_TransformationObj = data_TransformationClass()


    def trainingMethond(self):
        try:
            
            df = pd.read_csv("artifacts\cleanedDataFile.csv")
            X_train, X_test, y_train, y_test = self.data_TransformationObj.dataReadingAndSplitting(df)
            transformationOfData = self.data_TransformationObj.dataTransformation()

            X_train =transformationOfData.fit_transform(X_train)
            X_test = transformationOfData.transform(X_test)
            print(X_train)
            save_object(
            file_path= self.transformationFilePath,
            obj = transformationOfData
            )

            models, parameters = self.modelTrainingClassObj.models_to_train_and_parameters()

            model_report: dict = self.modelTrainingClassObj.evaluate_classification_models(
                X_train=X_train, y_train=y_train, X_test=X_test, y_test=y_test,models=models, param=parameters)



            self.modelTrainingClassObj.train_svc(X_train, y_train, C=0.5, kernel='linear')
            #self.modelTrainingClassObj.model_training_method(model_report,models)



            print(pd.DataFrame(X_train))


        except Exception as e:
            raise CustomException(e,sys)