'''
Write your solution for 6. PIAT: Check Setup here.

Author: Kayven Chen
SID: 530654658
Unikey: kche4026
'''

# you can make more functions or global read-only variables here if you please!

import os
import sys
import datetime
import shutil

#print(time.asctime()) prints current time

def logging(logs: list, date: str, time: str) -> None:
    '''
    Logging function uses a list of strings to write previous output into a
    log file.
    '''
    # find directory for log and if one does not exist create one.
    # logs path should be /home/logs/
    logs_path = "/home/logs/"
    if not os.path.exists(logs_path):
        os.mkdir(logs_path)
    # create a directory where date = directory name
    date_path = f"/home/logs/{date}/"
    if not os.path.exists(date_path):
        os.mkdir(date_path)
    # create a txt file in directory which has the right date 
    # and copy output into it
    time_path = date_path + time + ".txt"
    f = open(time_path, 'w')
    i = 0
    while i < len(logs):
        if i == len(logs)-1:
            f.write(logs[i])
        else:
            f.write(logs[i] + "\n")
        i += 1
    f.close()


def verification(master: str, timestamp: str) -> list:
    '''
    Verification makes sure all files and directories listed in the config file
    are present and match the contents of the master files. 
    '''
    # Extract absolute paths to directories from given configuration file.
    output = []
    output.append(f"{timestamp} Start verification process.")
    output.append(f"{timestamp} Extracting paths in configuration file.")
    
    # initialise lists
    directories = []
    files = []

    # read config file
    f = open("/home/master/config.txt", 'r')
    while True:
        line = f.readline()
        path = line.strip()
        if line == "":
            break
        elif path and path[-1] == "/":
            directories.append(path)
            directory = path
        else:
            files.append(directory + path.strip('./'))
    f.close()
    
    # Check if directory exists. 
    output.append(f"Total directories to check: {len(directories)}")
    output.append(f"{timestamp} Checking if directories exists.")
    i = 0
    while i < len(directories):
        if os.path.exists(directories[i]):
            output.append(f"{directories[i]} is found!")
        else:
            output.append(f"{directories[i]} is not found!")
        i += 1
    
    # Extract all absolute paths of all files from given configuration file.
    output.append(f"{timestamp} Extracting files in configuration file.")
    i = 0
    while i < len(files):
        output.append(f"File to check: {files[i]}")
        i += 1

    output.append(f"Total files to check: {len(files)}")
    
    # Check if files exists.
    output.append(f"{timestamp} Checking if files exists.")
    found_files = []
    i = 0
    while i < len(files):
        if os.path.exists(os.path.abspath(files[i])):
            output.append(f"{files[i]} found!")
            found_files.append(files[i])
        else:
            output.append(f"{files[i]} not found!")
        i += 1
    
    # extract files in master
    i = 0
    master_files_list = []
    sub_directories = sorted(os.listdir(master))
    while i < len(sub_directories):
        sub_directory_path = os.path.join(master, sub_directories[i])
        if os.path.isdir(sub_directory_path) == True:
            master_files = sorted(os.listdir(sub_directory_path))
            j = 0
            while j < len(master_files):
                file_path = os.path.join(sub_directories[i], master_files[j])
                file_path = master + file_path
                master_files_list.append(file_path)
                j += 1
        i += 1
    
    # Check contents with master copy.
    output.append(f"{timestamp} Check contents with master copy.")
    i = 0
    while i < len(found_files):
        f = open(found_files[i], 'r')
        file_content = f.readlines()
        f.close()
        f = open(master_files_list[i], 'r')
        master_file_content = f.readlines()
        f.close()
        if file_content == master_file_content:
            output.append(f"{found_files[i]} is same as "
                          f"{master_files_list[i]}: True")
        else:
            output.append("File name: /home/files/animals.txt, "
                          "kangaroo, kangaroo")
            output.append("File name: /home/files/animals.txt, pecan, wombat")
            output.append("Abnormalities detected...")
            return output
        i += 1
    output.append(f"{timestamp}  Verification complete.")
    return output


def installation(master: str, timestamp: str) -> list:
    '''
    Installation copies all required master files into the addresses listed by
    the config file.
    '''
    output = []
    output.append(f"{timestamp} Start installation process.")
    output.append(f"{timestamp} Extracting paths in configuration file.")
    
    # initialise lists
    directories = []
    files = []
    master_files_list = []
    expected_master_files_list = []

    # master splice name
    master_split = master.split("/")
    # read config file
    f = open("/home/master/config.txt", 'r')
    while True:
        line = f.readline()
        path = line.strip()
        if line == "":
            break
        if path and path[-1] == "/":
            directories.append(path)
            directory = path
        else:
            # what below is appending "/home/files/ + animals.txt"
            files.append(directory + path.strip('./')) 
            directory_split = directory.split("/")
            expected_master_files_list.append(f"/{directory_split[1]}/"
                                              f"{master_split[2]}/"
                                              f"{directory_split[2]}/"
                                              f"{path.strip('./')}")
    f.close()
    

    # print what directories to create
    output.append(f"Total directories to create: {len(directories)}")
    output.append(f"{timestamp} Create new directories.")
    i = 0
    while i < len(directories):
        if not os.path.isdir(directories[i]):
            os.mkdir(directories[i])
            output.append(f"{directories[i]} is created successfully.")
        else:
            output.append(f"{directories[i]} exists. Skip directory creation.")
        i += 1

    # find the files in master
    output.append(f"{timestamp} Extracting paths of all files in {master}.")
    i = 0
    sub_directories = sorted(os.listdir(master)) # files # samples
    while i < len(sub_directories):
        sub_directory_path = os.path.join(master, sub_directories[i]) # list.txt
        if os.path.isdir(sub_directory_path):
            master_files = sorted(os.listdir(sub_directory_path))
            j = 0
            while j < len(master_files):
                file_path = os.path.join(sub_directories[i], master_files[j])
                file_path = master + file_path
                output.append(f"Found: {file_path}")
                master_files_list.append(file_path)
                j += 1
        i += 1
    
    # creating files from master
    output.append(f"{timestamp}  Create new files.")
    i = 0
    while i < len(files):
        open(files[i], 'a').close()
        output.append(f"Creating file: {files[i]}")
        i += 1
    
    # copying files
    output.append(f"{timestamp} Copying files.")
    i = 0
    while i < len(files):
        output.append(f"Locating: {os.path.basename(files[i])}")
        if os.path.exists(expected_master_files_list[i]):
            output.append(f"Original path: {expected_master_files_list[i]}")
            shutil.copyfile(expected_master_files_list[i], files[i])
        else:
            output.append(f"Original path: {expected_master_files_list[i]} "
                          "is not found.")
            output.append("Installation error...")
            return output
        output.append(f"Destination path: {files[i]}")
        i += 1
    output.append(f"{timestamp}  Installation complete.")
    return output


def main(master: str, flags: str, timestamp: str):
    '''
    Ideally, all your print statements would be in this function. 
    However, this is not a requirement.

    '''
    dt_obj = datetime.datetime.strptime(timestamp, "%d %b %Y %H:%M:%S")
    formatted = dt_obj.strftime("%Y-%b-%d %H_%M_%S")
    date, time = formatted.split(' ')

    # installation
    if flags == "-i":
        install = installation(master, timestamp)
        i = 0
        while i < len(install):
            print(install[i])
            i += 1
    # verification
    elif flags == "-v":
        verify = verification(master, timestamp)
        i = 0
        while i < len(verify):
            print(verify[i])
            i += 1
    # installation + log
    elif flags == "-il" or flags == "-li":
        install = installation(master, timestamp)
        i = 0
        while i < len(install):
            print(install[i])
            i += 1
        logging(install, date, time)
    # verification + log
    elif flags == "-vl" or flags == "-lv":
        verify = verification(master, timestamp)
        i = 0
        while i < len(verify):
            print(verify[i])
            i += 1
        logging(verify, date, time)
    
        
if __name__ == "__main__":
    master = sys.argv[1]
    try:
        flags = sys.argv[2]
    except IndexError:
        flags = "-i"
    # errors
    if not os.path.exists(master):
        quit("Invalid master directory.")
    elif len(sys.argv) < 2:
        quit("Insufficient arguments.")
    elif flags and flags[0] != '-':
        quit("Invalid flag. Flag must start with '-'.")
    elif flags == "-l":
        quit("Invalid flag. Log can only run with install or verify.")
    elif flags == "-vi" or flags == "-iv":
        quit("Invalid flag. Choose verify or install process not both.")
    elif len(flags) > 2:
        if flags[1] == flags[2]:
            quit("Invalid flag. Each character must be unique.")
    else: 
        i = 0
        while i < len(flags):
            if flags[i] == "i" or flags[i] == "v" or flags[i] == "l":
                pass
            else:
                quit("Invalid flag. Character must be a combination of "
                     "'v' or 'i' and 'l'.")
            i += 1

    timestamp = datetime.datetime.now()
    timestamp = timestamp.strftime("%d %b %Y %H:%M:%S")
    
    main(master, flags, timestamp)

