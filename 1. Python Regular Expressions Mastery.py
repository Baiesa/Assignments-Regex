'''
Task 1: Code Correction

Problem Statement:
You are given a piece of code that is intended to extract email addresses from a given text. 
However, the code contains errors and does not function as expected. 
Your task is to identify and correct these errors.
'''


# import re

# text = "Contact emails are: john.doe@example.com and jane.doe@example.com."
# emails = re.findall(r"[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}", text)
# print(emails)

'''
Expected Outcome:

Correctly reformat the date in each log entry.
Replace all instances of '@username' with '[ANONYMIZED USER]'.
Use re.sub() effectively to achieve the desired text manipulations.
'''

import re

text = "Log entry: User @username logged in at 10:00 AM."
formatted_text = re.sub(r'(\d{1,2}:\d{2} [AP]M)', r'\1 [UTC]', text)
final_text = re.sub(r'@username', '[ANONYMIZED USER]', formatted_text)

print(final_text)