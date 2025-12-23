from database.db import Session
import pandas as pd
from database.models import Sensordata
import sqlite3
from database.db import DB_PATH

# Class that is called to add sensors to the table.
class SensorRepository:
    def add_df(self, df: pd.DataFrame):
        session = Session()
        
        rows_to_insert = []

        for _, rows in df.iterrows():
            rows_to_insert.append(
                Sensordata(
                    value =rows['value'],
                    status = rows['status'],
                    timestamp = rows['timestamp']
                )
            )
        
        session.add_all(rows_to_insert)
        session.commit()
        session.close()

# Read the table 
class ReadRepository:
    def Read_Repository(self):
        conn = sqlite3.connect(DB_PATH)
        cursor = conn.cursor()

        select_query = "SELECT * FROM sensordata"

        cursor.execute(select_query)

        records = cursor.fetchall()
    
        print(records)
        conn.close()
        return records

# Updating the table from status broken to status error
class UpdateRepository:
    def Update_Repository(self):
        conn = sqlite3.connect(DB_PATH)
        cursor = conn.cursor()
    
        update_query = f"UPDATE sensordata SET status = 'ERROR' WHERE status = 'BROKEN'"

        cursor.execute(update_query)

        conn.commit()
        conn.close()

# Removing ERRORS from the table
class DeleteRepository:
    def Delete_Repository(self):
        conn = sqlite3.connect(DB_PATH)
        cursor = conn.cursor()

        delete_query = "DELETE FROM sensordata WHERE status = 'ERROR'"

        cursor.execute(delete_query)

        conn.commit()
        conn.close()