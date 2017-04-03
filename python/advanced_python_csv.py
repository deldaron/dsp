import csv
import re

data = csv.DictReader(open("faculty.csv"))

#empty lists for pulling data
degrees = []
titles = []
e_mails = []
#Fill lists with appropriate data
for row in data:
    degrees.append(row[' degree'])
    titles.append(row[' title'])
    e_mails.append(row[' email'])
    
#Q1
#manually identified patterns in degrees and created unified readable forms
degree_dict = {
        r"\s?sc\.?d": "ScD ",
        r"\s?m\.?s\.?": "MS ",
        r"\s?m\.?p\.?h\.?": "MPH ",
        r"\s?b\.?s\.?e\.?d\.?": "BS Ed ",
        r"\s?ph\.?d?": "PhD ",
        r"\s?j\.?d\.?": "JD ",
        r"\s?m\.?a\.?": "MA ",
        r"\s?m\.?d\.?": "MD ",
        }
#Empty dict for tallying instances of degrees
degree_count = {}
#Pulling thevalues from degree_dictionary 
for i in degree_dict:
    degree_count.update({degree_dict[i]:0})


#iterating over degree dictionary and degrees to find frequencies
for key, value in degree_dict.items():
    for k in range(len(degrees)):
        pattern = re.compile(key, re.I)
        if re.search(pattern, degrees[k]):
            degree_count[value]+=1
            degrees[k] = re.sub(pattern, value, degrees[k])
#Print Answer to Console
for k, v in degree_count.items():
    if v > 1:
        print("There are " + str(v) + " instances of the " + k + "degree.")
    else:
        print("There is " + str(v) + " instance of the " + k + "degree.")
print('\n')
#Result:
#There are 6 instances of the ScD degree.
#There are 2 instances of the MS degree.
#There are 2 instances of the MPH degree.
#There are 1 instances of the BS Ed degree.
#There are 31 instances of the PhD degree.
#There are 1 instances of the JD degree.
#There are 1 instances of the MA degree.
#There are 1 instances of the MD degree.
#iterating over degree dictionary and degrees to find frequencies

#Q2
#Dictionary for counting and list for iterating over dictionary using int
title_dic = {
        'Professor': 0,
        'Associate Professor' : 0,
        'Assistant Professor' : 0
        }
title_dic_keys = ['Professor', 'Associate Professor', 'Assistant Professor']

#Pattern comparing all the of the letters up until the first space
pattern = re.compile('([^\s]+)', re.I)
#Iterating over titles list and dictionary to sum up total instances for each title
for i in range(len(titles)):
    if re.match(pattern, titles[i]):
        for n in range(len(title_dic)):
            if titles[i][0:(titles[i].index(' '))] == title_dic_keys[n][0:(titles[i].index(' '))]:
                title_dic[title_dic_keys[n]] += 1
#Print answers to console
for k,v in title_dic.items():
    if v > 1:
        print("There are " + str(v) + " instances of the " + k + " title.")
    else:
        print("There is " + str(v) + " instance of the " + k + " title.")
print('\n')
#Result:
#There are 13 instances of the Professor title.
#There are 12 instances of the Associate Professor title.
#There are 12 instances of the Assistant Professor title.

#Q3
print(e_mails)
print('\n')
    
#Q4
#find the index of the longest email extension
e_mail_extensions = []

for i in e_mails:
    e_mail_extensions.append(i[i.index('@'):])
e_mail_extensions = list(set(e_mail_extensions))

print(e_mail_extensions) 




