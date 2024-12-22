# 
# getting file attributes
# 

# import os
# from datetime import datetime
# from time import time

# def get_date(timestamp):
#     return datetime.utcfromtimestamp(timestamp).strftime("%d/%m/%Y")

# # print(time())

# # print(datetime.fromtimestamp(time()).strftime("%d/%m/%Y"))

# def get_file_attrs(folder):
#     with os.scandir(folder) as dir:
#         # print(dir)
#         for f in dir:
#             if f.is_file:
#                 # print(f)
#                 inf = f.stat()
#                 # print(inf)
#                 print(f"Modified {get_date(inf.st_mtime)} {f.name}")

# get_file_attrs("./files/subfolder")


# 
# traversing directory
# 

# import os

# def traverse(folder):
#     for dirpath, dirnames, filenames in os.walk(folder):
#         print(f"Folder: {dirpath}")
#         for f in filenames:
#             print(F"\t{f}")

# traverse(("./files"))

# 
# copying files
# 

