import csv
import glob
#import os

#filename = os.path.join('../PyPoll/raw_data', 'election_data_1.csv')
filename = '/Users/sonik/Desktop/BC/Homework/03-Python/Instructions/PyBoss/raw_data/employee_data1.csv'
#newfile = '/Users/sonik/Desktop/BC/Homework/03-Python/Instructions/PyPoll/raw_data/PyRollResults.txt'

#filepaths = glob.glob('/Users/sonik/Desktop/BC/Homework/03-Python/Instructions/PyBoss/raw_data/*.csv')
#for filename in filepaths:
    #add callback later
with open(filename, 'r', newline='', encoding='latin-1') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    header = next(csvreader)

    empid = []
    fullname = []
    dob = []
    ssn = []
    state = []

    for line in csvreader:
        empid.append(line[0])
        fullname.append(line[1].split(' ')) #find way to split in 2 arrays immediately
        dob.append(line[2])
        ssn.append(line[3])
        state.append(line[4])

    name = []
    lastName = []

    for i in fullname: #need to get rid of it
        name.append(i[0])
        lastName.append(i[1])
    


        # create 5 arrays from each row
        # change what necessary
        # zip in 1 and write line by line in new file