import re

text = "MyNameIsRakhat"

words = re.findall(r'[A-Z][^A-Z]*', text)
print(words)