import os, shutil

source_files = os.listdir('json_files_matches')

for i in range(len(source_files)):
    count = int(i / 10000) + 1
    source_file_path = os.path.join('json_files', source_files[i])
    dest_folder_path = os.path.join('json_files_' + str(count))
    shutil.copy(source_file_path, dest_folder_path)
    print(i)