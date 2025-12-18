from csv_tools.reader import Reader
import pandas as pd
import logging

logger = logging.getLogger(__name__)

class Cleaner:
    def __init__(self):
        self.combined_data = pd.DataFrame()
        logger.info('Cleaner started.')

    def combine_files(self, Reader: Reader):
        
        # Combine multiple DataFrames to one.
        
        try:
            self.data = Reader

            if not isinstance(self.data, pd.DataFrame):
                logger.error('file that needs to be combined is not a DataFrame')

            if self.combined_data.empty:
                self.combined_data = self.data
            else:
                self.combined_data = pd.concat(
                     [self.combined_data, self.data],
                     axis=0,
                     ignore_index=True
                )

        except Exception as e:
            logger.error("Failed to add DataFrame: %s", e)

        return self.combined_data 
    
    def clean_file(self):
        
        # Cleans the combined DataFrame

        df = self.combined_data

        if df.empty:
            return df

        # Making sure all column headers are able to be used in code.
        df.columns = (
        df.columns
        .str.lower()
        .str.strip()
        .str.replace(" ", "_")
        )
        
        # Removing all empty rows and columns.
        df_clean = df.dropna(how='all')

        # Removing the values that are incorrect
        df['value'] = pd.to_numeric(df['value'], errors="coerce")
        df_clean = df.dropna(axis='rows')
        df_rows_removed = len(df['value']) - len(df_clean['value'])
        logger.info('There were %s rows removed.',df_rows_removed)
                
        # Filling out the date and time for wrong value on timestamp.
        df_clean['timestamp'] = pd.to_datetime(df_clean['timestamp'], format='%Y-%m-%d %H:%M:%S', errors='coerce')
        df_clean["timestamp"] = df_clean["timestamp"].fillna(pd.Timestamp.now())
        logger.info('The date and time was filled out on %s.',pd.Timestamp.now())    

        df_clean.to_excel("Sensor_clean_data.xlsx")
