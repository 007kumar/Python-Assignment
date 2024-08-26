
# To Backup files from (D:\Source\files_backup\logs) to (D:\Destination\CopiedBackup)

import os
import shutil
from datetime import datetime

backup_datetime = datetime.now() .strftime(('%d.%m.%Y %H.%M.%S'))

# Source directroy path and destination directory
source_path = r"D:\Source\files_backup"
destination_path = r"D:\Destination\CopiedBackup" + '\\' + backup_datetime

# to make new directory 
os.makedirs(backup_datetime, exist_ok=True)

for folder in os.listdir(source_path):
    shutil.copytree(source_path + '/' + folder, destination_path)