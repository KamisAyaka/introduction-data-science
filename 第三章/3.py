import re

n = input()
list = re.findall("(^\d{15}$)|(^\d{18}$)|(^\d{17}(\d|X|x)$)",n)
print(type(list))
if not list :
    print("error")
else :
    print(list)