import os
import csv
from csv import reader
import json


c=0
c1=0
c2=0
c3=0
nline=0
all_list=[]
data = {}
data['comment'] = []

for root, dirs, files in os.walk('C:/Users/ostina/Documents/ES/fianl/funcom_processed/dump/new/'):
    for file in files:
        filename, extension = os.path.splitext(file)
        link1=(os.path.abspath(os.path.join(root, file)))
        if extension == '.py':
            a_file = open(link1, "r",encoding="utf8")
            list_of_lists = []
            for line in a_file:
                nline=nline+1
                stripped_line = line. strip()
                line_list = stripped_line. split()
                list_of_lists. append(line_list)
            a_file. close()
            c=c+1
            nline=nline-2
            file = open(link1, encoding="utf8")
            with file as files:
                c2=0
                for i in files:
                    c2=c2+1
                    if "#" in i:
                        c1=c1+1
                        if c2<nline:
                            
                            if len(list_of_lists[c2])>0 and list_of_lists[c2][0]== 'def':
                                c3=c3+1
                                data['comment'].append({
                                    'Comment': list_of_lists[c2-1],
                                    'Function':list_of_lists[c2]
                                })
                        else:
                            break
                        
            nline=0            
print(c,c1,c3)
print(all_list)

   
    
with open('data.json','w', encoding="utf8") as outfile:

    json.dump(data, outfile)