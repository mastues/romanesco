# Martina Stüssi
# 14-820-195
import csv
path = "/Users/ms/Dropbox/STUDIUM/Computerlinguistik/18_FS_MT/uebungen/mastues_mt_uebung04/romanesco/cleaned_hm.csv"
csv_db = open(path)
outfile = open('onlyhappy.txt','w')
reader = csv.reader(csv_db, delimiter=",")
for element in reader:
    if element[0].isdigit() and element[3] != '':
        element[3] = element[3].replace('"','')
        #print (element[3])
        outfile.write(element[3])
csv_db.close()
outfile.close()
