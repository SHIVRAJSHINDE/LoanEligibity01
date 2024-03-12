import os
import sys
from sklearn.ensemble import RandomForestClassifier
from sklearn.svm import SVC
from mlProject.ExceptionLoggerAndUtils.exception import CustomException
from mlProject.ExceptionLoggerAndUtils.utils import save_object
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score
from sklearn.model_selection import RandomizedSearchCV
import warnings
import pandas as pd

class ModelTrainingClass():
    def __init__(self):
        self.trained_model_file_path = os.path.join("artifacts", "model.pkl")

    def models_to_train_and_parameters(self):
        try:
            models = {
                "Random Forest": RandomForestClassifier()
            }

            params = {
                "Random Forest": {
                    'n_estimators': [10, 50, 100, 200],  # Number of trees in the forest
                    'max_depth': [None, 10, 20, 30],   # Maximum depth of each tree
                    'min_samples_split': [2, 5, 10],  # Minimum samples required to split a node
                    'min_samples_leaf': [1, 2, 4],    # Minimum samples required in a leaf node
                    'max_features': ['auto', 'sqrt', 'log2'],  # Number of features to consider
                },

            }

            return models, params
        except Exception as e:
            raise CustomException(e, sys)

    def model_training_method(self, model_report, models):
        try:
            print('-------------------------model_report-------------------------')
            print(models)
            print(model_report)
            print(max(model_report['Accuracy']))
            print(model_report.keys())
            best_model_name = model_report['modelName'][0]
            best_model = models[best_model_name]

            print("Best model on both training and testing dataset:")
            print(best_model)

            save_object(
                file_path=self.trained_model_file_path,
                obj=best_model
            )

        except Exception as e:
            raise CustomException(e, sys)

    def evaluate_classification_models(self, X_train, y_train, X_test, y_test, models, param):
        try:
            model_scores = {'modelName': [],
                            'Accuracy': [],

                            }

            with warnings.catch_warnings():
                warnings.filterwarnings("ignore", category=UserWarning)  # Ignore the UserWarning

                for model_name, model in models.items():
                    param_list = param[model_name]
                    gs = RandomizedSearchCV(model, param_list)
                    gs.fit(X_train, y_train)

                    model.set_params(**gs.best_params_)
                    model.fit(X_train, y_train)

                    y_test_pred = model.predict(X_test)

                    accuracy = accuracy_score(y_test, y_test_pred)
                    precision = precision_score(y_test, y_test_pred)
                    recall = recall_score(y_test, y_test_pred)
                    f1 = f1_score(y_test, y_test_pred)

                    model_scores['modelName'].append(model_name)
                    model_scores['Accuracy'].append(accuracy)

            print(pd.DataFrame(model_scores))
            return model_scores

        except Exception as e:
            raise CustomException(e, sys)