from insurance.exception import InsuranceException
from insurance.logger import logging
from insurance.entity import config_entity
from insurance.entity import artifact_entity
from insurance import utils
from sklearn.model_selection import train_test_split
import numpy as np
import os ,sys
import json
import pandas as pd


class DataIngestion: # data divided into train test & validate 
    def __init__(self, data_ingestion_config: config_entity.DataIngestionConfig):
        try:
            self.data_ingestion_config = data_ingestion_config
        except Exception as e:
            InsuranceException(e,sys)
    

    def initiate_data_ingestion(self)->artifact_entity.DataIngestionArtifact:
        try:
            logging.info("Collecting data as dataframe from database...")
            df:pd.DataFrame = utils.get_collection_as_dataframe(
                database_name= self.data_ingestion_config.database_name,
                collection_name= self.data_ingestion_config.collection_name)
            logging.info("save data in feature store")
            
            #Replace na by NAN value
            df.replace(to_replace="na", value=np.NAN, inplace=True)

            #save data in feature store
            logging.info("Creating feature store folder if it doesn't exist")
            feature_store_dir = os.path.dirname(self.data_ingestion_config.feature_store_file_path)
            os.makedirs(feature_store_dir, exist_ok=True)

            logging.info("Save df to feature store folder")
            df.to_csv(path_or_buf=self.data_ingestion_config.feature_store_file_path, index= True, header=True)

            logging.info("Training and splitting data")
            train_df, test_df = train_test_split(df,test_size=self.data_ingestion_config.test_size, random_state=1)
            
            logging.info("Creating dataset directory if it doesn't exist")
            dataset_dir = os.path.dirname(self.data_ingestion_config.train_file_path)
            os.makedirs(dataset_dir, exist_ok=True)

            logging.info("save training and testing data to dataset directory")
            train_df.to_csv(path_or_buf=self.data_ingestion_config.train_file_path, index= False, header= True)
            test_df.to_csv(path_or_buf=self.data_ingestion_config.test_file_path , index= False, header= True)
            logging.info("data saved successfully")

            #Preparing the artifacts folder
            data_ingestion_artifact = artifact_entity.DataIngestionArtifact(
                feature_store_file_path= self.data_ingestion_config.feature_store_file_path,
                train_file_path= self.data_ingestion_config.train_file_path,
                test_file_path= self.data_ingestion_config.test_file_path,
            )
            
            logging.info(f"Data ingestion artifact: {data_ingestion_artifact}")
            return data_ingestion_artifact

        except Exception as e:
            InsuranceException(e,sys)

