import csv
import re
import collections

input_data = open('faculty.csv', 'r')

data = csv.reader(input_data)
next(data)

faculty_dict = {}
professor_dict = {}

#Function for printing only three keys from dictionary
def print_three_keys(dictionary):
    count = 0
    for k,v in dictionary.items():
        if count < 3:
            print(k,v)
            count+=1


for row in data:
    #taking name data from the index of the last space
    key = row[0][(row[0]).rindex(' ')+1:]
    #check to see if this last name is already a key and either adding or appending accordingly
    if not key in faculty_dict:
        faculty_dict[key] = [row[1:]]
    else:
        faculty_dict[key].append([row[1:]])

input_data.seek(0)
next(data)

for row in data:
    key = (row[0][:(row[0]).index(' ')], row[0][(row[0]).rindex(' ')+1:])
    professor_dict[key] = row[1:]

sorted_dict = collections.OrderedDict(sorted(professor_dict.items()))
print_three_keys(faculty_dict)
print('\n')
print_three_keys(sorted_dict)
print('\n')
"""couldn't quite figure this one out, my original professor_dict was 
ordered alphabetically by last name, but only coincidentally, if the data
hadn't been ordered neither would the dict. when I tried sorted with lambda
I only got the keys back, so I just used those to print out the dict k/v pairs
"""
reordered_dict = sorted(sorted_dict, key = lambda x: x[1])
count = 0
for i in reordered_dict:
    if count < 3:
        print(i, professor_dict[i])
    count +=1


input_data.close()
