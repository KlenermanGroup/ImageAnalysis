#!/usr/bin/env python

import shutil
import os
from pathlib import Path

indexfile = "index.txt"
cwd = os.getcwd()

print("Making directories...")
with open(indexfile,'r') as idx:
    for line in idx:
        idx_line = line.strip()
        idx_split = idx_line.split(':')
        print(idx_split)
        well_num = idx_split[0].strip()
        sample = idx_split[1].strip()
        sample_esc = sample.replace(" ","\ ")
        if well_num in idx_line and idx_split[1]:
            dirname2 = idx_split[1].strip()
            dirname = dirname2.replace(" ","").strip()
            if not os.path.exists(dirname):
                os.makedirs(dirname)
                os.makedirs(dirname+ '/561')
                os.makedirs(dirname+ '/ThT')
            else:
                print("Sorting tif files...")
            for filename in os.listdir(cwd):
                if filename.endswith(".tif") and well_num in filename:
                    if well_num and '561' in filename:
                        shutil.move(cwd + "/" +filename, cwd + "/"+dirname+"/561/")
                    elif well_num and 'ThT' in filename:
                        shutil.move(cwd + "/"+ filename, cwd + "/"+dirname+"/ThT/")
                    else:
                        print("Something went wrong")
                else: 
                    continue
        else: 
            continue




        
