import csv
from collections import Counter
#import os

#filename = os.path.join('../PyPoll/raw_data', 'election_data_1.csv')
filename = '/Users/sonik/Desktop/BC/Homework/03-Python/Instructions/PyPoll/raw_data/election_data_2.csv'
newfile = '/Users/sonik/Desktop/BC/Homework/03-Python/Instructions/PyPoll/raw_data/PyRollResults.txt'

with open(filename, 'r', newline='', encoding='latin-1') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    header = next(csvreader) # Magic function - get rid of the first row in csv

    votesCount = Counter() # A nice library for counting. number of votes for each candidate
    candList = [] # Full list of candidates
    percentage = [] # For keeping the percentage of votes for each candidate
    answer = [] # Final answer to print out and export

    for row in csvreader: # Really slow
        #if row[0] != 'Voter ID': # Get rid of first row in csv
        candList.append(row[2])

    totalVotes = len(candList)

    for name in candList: # Create an object - Candidate: Votes number
        votesCount[name] += 1

    winner = max(zip(votesCount.values(), votesCount.keys())) # Defining a winner
    names = tuple(votesCount.keys())
    votes = tuple(votesCount.values())

    for x in votes:
        percentage.append((int(x)/totalVotes)*100) # Append % to the list
    
    answer.append('Election Results')
    answer.append('-----------------------')
    answer.append('Total Votes: ' + str(totalVotes))
    answer.append('-----------------------')
    for x in range(len(names)):
        answer.append(names[x] + ': ' + str(round(percentage[x],1)) + '% ' + '(' + str(votes[x]) + ')')
    answer.append('-----------------------')
    answer.append('Winner: ' + winner[1])
    answer.append('-----------------------')

    print("\n".join((answer)))

with open(newfile, 'w') as txtfile:
    txtfile.write('\n'.join(answer))
