"""
Match Two
Create a regular expression that matches any word that starts with any character and is followed by two o's. 
Then use Python's re module to match boo and loo in the sentence "The ghost that says boo haunts the loo". Save the result in a variable and print it.
"""
import re

pattern = r"\b\wo{2}\b"
sentence = "The ghost that says boo haunts the loo"
matches = re.findall(pattern, sentence)
print(matches)