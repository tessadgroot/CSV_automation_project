import pandas as pd 
import logging

logger = logging.getLogger(__name__)

class Reader:
    def read_file(self,file: str):
        # When called the files will be read.
        try:
            file_sensors = pd.read_csv(file)
            
            return file_sensors
        except FileNotFoundError:
            logger.error("File is not found. Please try again.")
            raise FileNotFoundError("File is not found. Please try again.")
        except Exception as e:
            logger.error("Failed for file to be read: %s",e)
            raise Exception("Failed for file to be read.")



