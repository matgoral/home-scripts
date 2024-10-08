import os
import zipfile
import time
import json

### Config File template
#{
#    "backup_dir": "/home/user/backup",
#    "source_dir": "/home/user/source"
#}


with open("wow_wtf_backup_config.json") as config_file:
    config = json.load(config_file)

# Define the source folder and destination path
source_folder = config['source_dir']
# Define the target folder where the ZIP will be moved
backup_folder = config['backup_dir']
timestr = time.strftime("%Y%m%d")
zip_file_name = "wtf_backup_" + timestr + ".zip"
zip_file_path = os.path.join(backup_folder, zip_file_name)

# Check if the destination folder exists, create it if not
if not os.path.exists(backup_folder):
    os.makedirs(backup_folder)

# Create the ZIP file
with zipfile.ZipFile(zip_file_path, 'w', zipfile.ZIP_DEFLATED) as zipf:
    for root, dirs, files in os.walk(source_folder):
        for file in files:
            file_path = os.path.join(root, file)
            # Write the file to the zip archive, removing the base folder from the path
            zipf.write(file_path, os.path.relpath(file_path, source_folder))


print(f"ZIP file has been created successfully.")
# Log to destination folder
log_file = os.path.join(backup_folder, "log.txt")
with open(log_file, 'a') as log:
    log.write(f"Backup created at {timestr}\n")
    log.write("\n")
    
