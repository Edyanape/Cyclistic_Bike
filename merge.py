
#Cyclistic Bike Share
# Yael Hernández
# 01/07/2023

#Imported libraries
import os
import re
import pandas as pd

#Path where is located csv files
dir = r"C:\Users\Yael\Documents\Cyclistic"

#List where it will be save files
all_dfs = []

#Code that search all folder and select only csv files with a date range of 2021 - 2022
for root,dirs,files in os.walk("."):
    for f_csv in files: 
        if re.search(r"^\d",f_csv):
            #print(f_csv)
            for f_file in os.listdir(dir):
                if re.search(r"^\d",f_file):    
                #print(f_file)
                    for filename in [os.path.join(dir+"\\"+f_file+"\\"+f_csv)]:
                        name = re.search(r"202(\d\d\d)-divvy-tripdata\\202(\d\d\d)-divvy-tripdata.csv",filename)
                        if name:
                            date_f = name.group(1)
                            date_s = name.group(2) 
                            if date_f == date_s:
                                pass
# Append and read of the all csv files
                                new_df = pd.read_csv(filename)    
                                all_dfs.append(new_df)

# Quantity of csv files stored in a list
len(all_dfs)
df = pd.concat(all_dfs)
# Extraction of data in a new csv file
df.to_csv("cyclistic_bike_share.csv")
                                
                                