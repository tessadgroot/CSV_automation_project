from csv_tools.reader import Reader
from csv_tools.cleaner import Cleaner
import logging

logging.basicConfig(
filename="CSV_automation_project.log",
level=logging.DEBUG,
format="%(asctime)s - %(levelname)s - %(message)s"
)

sensor_files = Reader()

sensor_1 = sensor_files.read_file(r"sensor_01.csv")
sensor_2 = sensor_files.read_file(r"sensor_02.csv")
sensor_3 = sensor_files.read_file(r"sensor_dirty.csv")

combined_files = Cleaner()

sensors = combined_files.combine_files(sensor_1)
sensors = combined_files.combine_files(sensor_2)
sensors = combined_files.combine_files(sensor_3)

print(combined_files.clean_file())