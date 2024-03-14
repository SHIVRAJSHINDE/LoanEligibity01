import os
import sys
from sklearn.ensemble import RandomForestClassifier
from sklearn.svm import SVC
from mlProject.ExceptionLoggerAndUtils.exception import CustomException
from mlProject.ExceptionLoggerAndUtils.utils import save_object
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score
from sklearn.model_selection import RandomizedSearchCV
from sklearn.ensemble import RandomForestClassifier
import mlflow
import mlflow.sklearn
from mlflow.models import infer_signature

from urllib.parse import urlparse
import joblib
import warnings
import pandas as pd

class ModelTrainingClass():
    def __init__(self):
        self.trained_model_file_path = os.path.join("artifacts", "model.joblib")



    def train_svc(self,X_train, X_test, y_train, y_test, C=1.0, kernel='rbf', degree=3, gamma='scale'):
        try:
        
            with mlflow.start_run():
                model = SVC(C=C, kernel=kernel, degree=degree, gamma=gamma)
                model.fit(X_train,y_train)
                predicted_qualities = model.predict(X_test)

                accuracy = accuracy_score(y_test, predicted_qualities)
                precision = precision_score(y_test, predicted_qualities)
                recall = recall_score(y_test, predicted_qualities)
                f1 = f1_score(y_test, predicted_qualities)
                print('accuracy,precision,recall,f1')

                print(accuracy,precision,recall,f1)
                mlflow.log_param("C",C)
                mlflow.log_param("degree",degree)
                print("Params Logged")

                mlflow.log_metric("accuracy", accuracy)
                print("accuracy Logged")
                mlflow.log_metric("precision", precision)
                print("precision Logged")
                mlflow.log_metric("recall", recall)
                print("recall Logged")
                mlflow.log_metric("f1", f1)
                print("f1 Logged")
                predictions = model.predict(X_train)
                signature = infer_signature(X_train, predictions)

                tracking_url_type_store = urlparse(mlflow.get_tracking_uri()).scheme

                # Model registry does not work with file store
                if tracking_url_type_store != "file":
                    # Register the model
                    # There are other ways to use the Model Registry, which depends on the use case,
                    # please refer to the doc for more information:
                    # https://mlflow.org/docs/latest/model-registry.html#api-workflow
                    mlflow.sklearn.log_model(
                        model, "model", registered_model_name="SVC", signature=signature
                    )
                else:
                    mlflow.sklearn.log_model(model, "model", signature=signature)

        except Exception as e:
            raise CustomException(e, sys)
        

 