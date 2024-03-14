import sys

from mlProject.pipeline.stage0_data_ingestion import DataIngestionTrainingPipeline
from mlProject.pipeline.stage1_Data_Ingestion import dataIngestionPipeline
from mlProject.pipeline.stage2_Data_Transformation import dataTransformationInitiatorClass
from mlProject.ExceptionLoggerAndUtils.exception import CustomException
from mlProject.pipeline.stage3_model_Trainer import trainingInitiatorClass

STAGE_NAME = "Data Ingestion stage"


try:
   
   data_ingestion = dataIngestionPipeline()
   data_ingestion.dataIngestionMethod()
   
except Exception as e:
    raise CustomException(e,sys)

try:
   
   dataTransformationInitiator = dataTransformationInitiatorClass()
   dataTransformationInitiator.dataTransformationInitiatorMethod()
   
except Exception as e:
    raise CustomException(e,sys)
 
 
 
try:

   trainingInitiatorClassInitiator = trainingInitiatorClass()
   trainingInitiatorClassInitiator.trainingMethond()

except Exception as e:
    raise CustomException(e,sys)



