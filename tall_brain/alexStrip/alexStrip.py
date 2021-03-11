###########################################################################
#                                                                         #
#                              alexStrip 1.0                              #
#                                                                         #
###########################################################################

"""
    Harper Scott
    March 5th, 2021
    Colin Reilly School of Brogramming
"""

def sexyStrip(dataFile):
    """
    Function that strips trailing tabs and maintains newlines.
    Place incorrect.txt in directory with alexStrip.py and run the script.

    Keyword arguments:
    dataFile -- Input raw text file which is in desperate need of trailing tab removal.
    """
    correct = open('correct.txt', 'w+')
    for line in dataFile:
        stripLines = line.rstrip()
        fixedLines = stripLines + "\n"
        correct.write(fixedLines)
    correct.close()



# Opens the initial text file.
rawData = open('incorrect.txt', 'r')

# Calls the function
sexyStrip(rawData)
