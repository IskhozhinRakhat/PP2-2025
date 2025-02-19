import re

pattern = re.compile(r"[A-Z]{1}[a-z]+")
print(pattern.findall("Rakhat Iskhozhin is back On Track"))