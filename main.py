import os, sys
from insurance.logger import logging
from insurance.exception import InsuranceException
from insurance.utils import get_collection_as_dataframe
from insurance.entity.config_entity import DataIngestionConfig
from insurance.entity import config_entity
from insurance.components.dataIngestion import DataIngestion


if __name__ == "__main__":
    try:
        #get_collection_as_dataframe(database_name="insurance", collection_name="insurance_data")
        traning_pipeline_config = config_entity.TraningPipelineConfig()
        data_ingestion_config = config_entity.DataIngestionConfig(traning_pipeline_config= traning_pipeline_config)
        print(data_ingestion_config.to_dict())
        data_ingestion = DataIngestion(data_ingestion_config= data_ingestion_config)
        data_ingestion_artifact = data_ingestion.initiate_data_ingestion()
    except Exception as e:
        raise InsuranceException(e, sys)

