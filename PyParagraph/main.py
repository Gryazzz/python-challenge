import os
from statistics import mean
import re

os.chdir('/Users/sonik/Desktop/BC/GitHub/Python/python-challenge/PyParagraph/raw_data')
filepath = os.path.join('paragraph_1.txt')

with open(filepath, 'r', encoding='latin-1') as txt:
    
    wordsLength = [] # List for keeping all word's length
    
    for line in txt: # Iterate through the line of text
        for word in line.split(): # Iterate through each word in a line
            wordsLength.append(len(word)) # Append word's length

    wordCount = len(wordsLength) # Number of items in a word list
    averageLetter = mean(wordsLength) # Average letter count

# At this point, I can't explain why, but the rest of the code works only if
# I open the original file one more time. May be some previous methods changed something.

with open(filepath, 'r', encoding='latin-1') as newtxt:
    content = newtxt.read() # Get the file content
    sentences = re.split(r'\.|\?|\!|', content) # Very weird and needs another RE
    sentCount = (len(sentences)) # Number of sentences
    sentLength = [] # List for keeping words number for each sentence
    for word in sentences:
        sentLength.append(len(word.split()))

    averageLength = mean(sentLength)

answer = [] # Answer list
answer.append('\nParagraph Analysis')
answer.append('-------------------')
answer.append('Approximate Word Count: ' + str(wordCount))
answer.append('Approximate Sentence Count: ' + str(sentCount))
answer.append('Average Letter Count: ' + str(round(averageLetter, 4)))
answer.append('Average Sentence Length: ' + str(round(averageLength, 4)))

print("\n".join((answer)))    
    
    
    