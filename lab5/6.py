import re

text = "Hello My name, is. Rakhat, but you can call me Rakha"
replacedText = re.sub(r'[ ,.]', ':', text)
print(replacedText)