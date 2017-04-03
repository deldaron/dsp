import csv
import re

input_data = open('faculty.csv', 'r')
e_mail_file = open('emails.csv', 'w')

data = csv.reader(input_data)

next(data)
for row in data:
    e_mail_file.write((row[3] + '\n'))
    
input_data.close()
e_mail_file.close()
