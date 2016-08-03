#!/usr/bin/python
import os 

def rename_files():
    # (1) Scans a directory and prints the contents it has
    file_list = os.listdir("/home/maverick/Downloads/prank")
    print(file_list)
    saved_path = os.getcwd()
    print("Current Working Directory is " + saved_path)
    os.chdir("/home/maverick/Downloads/prank") 
    # (2) Read the file name and remove numbers it contains
    for file_name in file_list:
        os.rename(file_name,file_name.translate(None, "0123456789"))
       


rename_files()
