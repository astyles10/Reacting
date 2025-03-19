import logging
import datetime as dt

logging.basicConfig(level="DEBUG")

from aixweather.project_class import ProjectClassDWDHistorical

project = ProjectClassDWDHistorical(
  start = dt.datetime(2022, 1, 1),
  end = dt.datetime(2023, 1, 1),
  station = 15000,
  #specify whether nan-values should be filled when exporting
  fillna=True,
  # define results path if desired
  abs_result_folder_path=None
)

project.import_data()
print(f"\nHow the imported data looks like:\n{project.imported_data.head()}\n")

project.data_2_core_data()
print(f"\nHow the core data looks like:\n{project.core_data.head()}\n")

project.core_2_csv()