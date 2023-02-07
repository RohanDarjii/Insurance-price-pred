import os, sys
from insurance.logger import logging
from insurance.exception import InsuranceException
from insurance.utils import get_collection_as_dataframe
from insurance.entity.config_entity import DataIngestionConfig
from insurance.entity import config_entity

if __name__ == "__main__":
    try:
        #get_collection_as_dataframe(database_name="insurance", collection_name="insurance_data")
        traning_pipeline_config = config_entity.TraningPipelineConfig()
        data_ingestion_config = config_entity.DataIngestionConfig(traning_pipeline_config= traning_pipeline_config)
        print(data_ingestion_config.to_dict())
    except Exception as e:
        raise InsuranceException(e, sys)

