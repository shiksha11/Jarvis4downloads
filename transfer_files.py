

import os
import json
import time


cwd = os.getcwd()
o=cwd.split(os.sep)
os.chdir(os.sep+ o[1] + os.sep + o[2] + os.sep)
p=os.getcwd()
os.chdir(p+os.sep + 'Downloads' + os.sep)
json_file =open(os.sep + o[1] + os.sep + o[2] + os.sep+ "config.txt","r")
data =  json.load(json_file)
json_file.close()
for f in os.listdir():
    f_name,f_ext = os.path.splitext(f)
    f_ext= f_ext.strip()
    if(any( x== f_ext for x in data['videos'])):
        today= os.sep + o[1] + os.sep + o[2] + os.sep + 'Desktop' + os.sep + 'videos' + os.sep + time.strftime('%Y%m%d')
        if not os.path.exists(today):
            os.makedirs(today)
        os.rename(f, today + os.sep + f_name+f_ext)
    if(any(x== f_ext for x in data['pictures'])):
        today= os.sep + o[1] + os.sep + o[2] + os.sep + 'Desktop' + os.sep + 'pictures' + os.sep + time.strftime('%Y%m%d')
        if not os.path.exists(today):
            os.makedirs(today)
        os.rename(f, today + os.sep + f_name + f_ext)
    if(any( x== f_ext for x in data['documents'])):
        today= os.sep + o[1] + os.sep + o[2] + os.sep + 'Desktop' + os.sep + 'documents' + os.sep + time.strftime('%Y%m%d')
        if not os.path.exists(today):
            os.makedirs(today)
        os.rename(f, today + os.sep + f_name + f_ext)
    else:
        today= os.sep + o[1] + os.sep + o[2] + os.sep + 'Desktop' + os.sep + 'projects' + os.sep + time.strftime('%Y%m%d')
        if not os.path.exists(today):
            os.makedirs(today)
        os.rename(f, today + os.sep + f_name + f_ext)
