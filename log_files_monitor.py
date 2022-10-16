import os
import glob

local_log_dir = r"\\network\location\folder"
# folder where logs are
specific_file_name_string = "filename string"
# script will look only for files with that string in filename
specific_file_extension_string = ".txt"
# script will look only for text files
local_log_files_condition = rf"{local_log_dir}\*{specific_file_name_string}*{specific_file_extension_string}"
error_string = "Closing connection -1"
# script will look for this string in log files


error_string_list = []
# empty list of error strings

if len(os.listdir(local_log_dir)) != 0:
    # checks if there are files in the folder
    for condition in glob.glob(local_log_files_condition):
        # if the conditions are met then opens and reads log files
        log_path = str(condition)
        with open(log_path, "r") as f:
            content = f.read()
            if error_string in content:
                # append to the list
                error_string_list.append(log_path)
    if len(error_string_list) !=0:
        #check if error list is empty
        print("-2: Error in log file")
    else:
        print("1: All good")
else:
    print("0: No log files present")
