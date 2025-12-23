from csv_tools.reader import Reader
from csv_tools.cleaner import Cleaner
import logging
from database.init_db import init_db
from database.crud import SensorRepository
from database.crud import ReadRepository
from database.crud import UpdateRepository
from database.crud import DeleteRepository

init_db()

logging.basicConfig(
filename="CSV_automation_project.log",
level=logging.DEBUG,
format="%(asctime)s - %(levelname)s - %(message)s"
)

sensor_files = Reader()

sensor_1 = sensor_files.read_file(r"C:/Users/Tessa/OneDrive/Documenten/Python Scripts/Sensor Project/sensor_01.csv")
sensor_2 = sensor_files.read_file(r"C:/Users/Tessa/OneDrive/Documenten/Python Scripts/Sensor Project/sensor_02.csv")
sensor_3 = sensor_files.read_file(r"C:/Users/Tessa/OneDrive/Documenten/Python Scripts/Sensor Project/sensor_dirty.csv")

combined_files = Cleaner()

sensors = combined_files.combine_files(sensor_1)
sensors = combined_files.combine_files(sensor_2)
sensors = combined_files.combine_files(sensor_3)

df_combine_file = combined_files.clean_file()


Repository = SensorRepository()

Repository.add_df(df_combine_file)

Read_Repository = ReadRepository()
print(Read_Repository.Read_Repository())

Update_Repository = UpdateRepository()
Update_Repository.Update_Repository()

Delete_Repository = DeleteRepository()
Delete_Repository.Delete_Repository()
