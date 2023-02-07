import os , sys
from insurance.exception import InsuranceException
from insurance.logger import logging
from datetime import datetime

FILE_NAME = "insurance.csv"
TRAIN_FILE_NAME = "train.csv"
TEST_FILE_NAME = "test.csv"

class TraningPipelineConfig:
    def __init__(self):
        try:
            self.artifact_dir = os.path.join(os.getcwd(), 'artifact',f"{datetime.now().strftime('%m%d%y__%H%M%S')}")
        except  Exception as e:
            raise InsuranceException(e,sys)

class DataIngestionConfig:
    def __init__(self, traning_pipeline_config:TraningPipelineConfig):
        try:
            self.database_name = "insurance"
            self.collection_name = "insurance_data"
            self.data_ingestion_dir = os.path.join(traning_pipeline_config.artifact_dir, "data_ingestion")
            self.feature_store_file_path = os.path.join(self.data_ingestion_dir,"feature_store",FILE_NAME)
            self.train_file_path = os.path.join(self.data_ingestion_dir, "dataset",TRAIN_FILE_NAME)
            self.test_file_path = os.path.join(self.data_ingestion_dir, "dataset",TEST_FILE_NAME)
            self.test_size = 0.2
        except Exception as e:
            raise InsuranceException(e,sys)

    
    #Converting data into a dictionary to read

    def to_dict(self,)->dict:
        try:
            return self.__dict__
        except Exception as e:
            raise InsuranceException(e,sys)