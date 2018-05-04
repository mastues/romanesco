#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Martina Stüssi
# 14-820-195
# Valentina Vogel
# 16-708-919

import sys
import csv
import re
path = "/Users/ms/Dropbox/STUDIUM/Computerlinguistik/18_FS_MT/uebungen/mastues_mt_uebung04/romanesco/cleaned_hm.csv"
csv_db = open(path)
outfile = open('happy_.txt','w')
#quotechar is v. important
spamreader = csv.reader(csv_db, delimiter=',', quotechar='"')
for row in spamreader:
    if row:
        if row[0].isdigit():
            try:
                if int(row[6]) == 1:
                    print(row[6])
                    sentence = re.sub(r'^\s*\"?', "", row[4], flags=re.UNICODE)
                    sentence_clean = re.sub(r'\"?\s*$', "", sentence, flags=re.UNICODE)
                    #if len(sentence_clean) < 12:
                    #   continue
                        #textfile.write((row[4].replace('"', '')))
                    outfile.write(sentence_clean)
                    outfile.write('\n')
                else:
                    continue
            except IndexError:
                continue
        else:
            continue
csv_db.close()
outfile.close()
