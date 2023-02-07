import pandas as pd
import numpy as np
import os, sys
from insurance.exception import InsuranceException
from insurance.logger import logging
from insurance.config import client

def get_collection_as_dataframe(database_name:str, collection_name:str)->pd.DataFrame:
    try:
        logging.info(f"Reading data from database:{database_name} and collection_name:{collection_name}")
        df = pd.DataFrame(client[database_name][collection_name].find())
        logging.info(f"find columns: {df.columns}")
        if "_id" in df.columns:
            logging.info("Dropping column: _id")
            df = df.drop("_id", axis=1)
            logging.info(f"Rows and columns: {df.shape}")
        return df 


    except Exception as e:
        raise InsuranceException(e, sys)
