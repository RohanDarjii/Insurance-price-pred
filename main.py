import os, sys
from insurance.logger import logging
from insurance.exception import InsuranceException

def test_logger_and_exception():
    try:
        logging.info("starting Test logging")
        result = 1 / 0
        print(result)
        logging.info("Ending Test logging")
    except Exception as e:
        logging.debug(str(e))
        raise InsuranceException(e, sys)

if __name__ == "__main__":
    try:
        test_logger_and_exception()
    except Exception as e:
        print(e)

