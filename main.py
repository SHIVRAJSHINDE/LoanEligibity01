import sys

from mlProject.pipeline.stage1_Data_Ingestion import dataIngestionPipeline
from mlProject.ExceptionLoggerAndUtils.exception import CustomException

STAGE_NAME = "Data Ingestion stage"
try:
   data_ingestion = dataIngestionPipeline()
   data_ingestion.dataIngestionMethod()
except Exception as e:
    raise CustomException(e,sys)