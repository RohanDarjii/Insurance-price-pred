import pymongo
import pandas as pd
import numpy as np
import os, sys
import json
from dataclasses import dataclass

@dataclass
class EnviromentVariable():
    mongo_url:str = os.getenv("MONGO_DB_URL")


env_var = EnviromentVariable()
client = pymongo.MongoClient(env_var.mongo_url)
TARGET_COL = "expenses"