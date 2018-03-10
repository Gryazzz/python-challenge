import csv
import glob
import os
import datetime

# Read all .csv files in a folder
# Each * means one folder from root dir to current. Don't know how to make it flexible
filepaths = glob.glob('/*/*/*/*/*/*/python-challenge/PyBoss/raw_data/*.csv')
#filepaths = glob.glob('~/python-challenge/PyBoss/raw_data/*.csv')
#filepaths = glob.glob(os.path.abspath('/raw_data/*.csv'))
x = 1
print(filepaths)

# Iterate through each file
for filename in filepaths:
    # In a separate folder create a new file for answer with unique name
    # Wanted to add the name of the original file, but failed
    outputpath = os.path.join('answers', 'answer_for_file_' + str(x) + '.csv')
    x += 1
    
    with open(filename, 'r', newline='', encoding='latin-1') as csvfile, open(outputpath, 'w', newline='') as matched:
        csvreader = csv.reader(csvfile, delimiter=',')
        csvwriter = csv.writer(matched, delimiter=',')
        
        # Move the first row from original file to csvwriter
        #csvwriter.writerow(next(csvreader)) # Unfortunately we need another headings, but I want to keep this solution
        
        header = next(csvreader) # Consume the first line in csvreader (to get rid of headings)

        us_state = {
            'Alabama': 'AL',
            'Alaska': 'AK',
            'Arizona': 'AZ',
            'Arkansas': 'AR',
            'California': 'CA',
            'Colorado': 'CO',
            'Connecticut': 'CT',
            'Delaware': 'DE',
            'Florida': 'FL',
            'Georgia': 'GA',
            'Hawaii': 'HI',
            'Idaho': 'ID',
            'Illinois': 'IL',
            'Indiana': 'IN',
            'Iowa': 'IA',
            'Kansas': 'KS',
            'Kentucky': 'KY',
            'Louisiana': 'LA',
            'Maine': 'ME',
            'Maryland': 'MD',
            'Massachusetts': 'MA',
            'Michigan': 'MI',
            'Minnesota': 'MN',
            'Mississippi': 'MS',
            'Missouri': 'MO',
            'Montana': 'MT',
            'Nebraska': 'NE',
            'Nevada': 'NV',
            'New Hampshire': 'NH',
            'New Jersey': 'NJ',
            'New Mexico': 'NM',
            'New York': 'NY',
            'North Carolina': 'NC',
            'North Dakota': 'ND',
            'Ohio': 'OH',
            'Oklahoma': 'OK',
            'Oregon': 'OR',
            'Pennsylvania': 'PA',
            'Rhode Island': 'RI',
            'South Carolina': 'SC',
            'South Dakota': 'SD',
            'Tennessee': 'TN',
            'Texas': 'TX',
            'Utah': 'UT',
            'Vermont': 'VT',
            'Virginia': 'VA',
            'Washington': 'WA',
            'West Virginia': 'WV',
            'Wisconsin': 'WI',
            'Wyoming': 'WY',
        } # Many thanks for Ahmed Haque for creating this dictionary

        empID = [] # a list for keeping ID numbers from column 1
        firstName = [] # first names will be stored here
        lastName = [] # last names will be stored here
        dateOfBirth = [] # same for DOB's
        ssn = [] # same for SSN's
        state = [] # same for states

        for line in csvreader:

            empID.append(line[0]) # Simply add all ID's in one list

            fullName = line[1].split(' ') # Create a list of lists with [FirstName, LastName]
            firstName.append(fullName[0]) # Add first name which is [0]
            lastName.append(fullName[1]) # And second name [1]

            # Change a date format and append it to a list
            date = datetime.datetime.strptime(line[2], '%Y-%m-%d').strftime('%d/%m/%Y')
            dateOfBirth.append(date)

            # I don't like this, planning to rework
            numb = line[3]
            ssn.append('***-**-' + str(numb[-4:]))
            
            statename = line[4]
            if statename in us_state: # Check if state is in our dictionary
                state.append(us_state[statename]) # If yes, append the value
            else: # If not.. just not. We need to add anything anyway.
                state.append('This is not yet the US state')

        answer = zip(empID, firstName, lastName, dateOfBirth, ssn, state)

        csvwriter.writerow(['Emp ID', 'First Name', 'Last Name', 'DOB', 'SSN', 'State'])
        csvwriter.writerows(answer)
    
print('Finished')

        