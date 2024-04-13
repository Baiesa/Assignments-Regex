'''
Objective:
The goal of this assignment is to harness the full potential of Python's Regular Expressions for advanced text processing. 
You'll tackle complex tasks involving data extraction, validation, and transformation, sharpening your skills in applying regex in 
various challenging scenarios.

Task 1: Advanced Data Extraction

Problem Statement:
Develop a script to extract specific information from a formatted text. 
The text contains data entries delimited by semicolons and formatted as 'Key: Value'. 
Extract the value corresponding to a specific key.
'''

import re

text = "Name: John Doe; Age: 30; Occupation: Engineer; Location: New York"
occupation_match = re.search(r'Occupation: (\w+)', text)
if occupation_match:
    occupation = occupation_match.group(1)
    print("Occupation:", occupation)
else:
    print("Occupation not found in the text.")