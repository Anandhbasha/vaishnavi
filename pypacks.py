# # os
# import os

# print(os.getcwd())
# print(os.name)

# if os.path.exists("ne.txt"):
#     # print("File Found")
#     os.remove("filename")
# else:
#     print("File not found")

# json
import json 

data = {"name":"abc","age":20}
print(type(data))

NewJson = json.dumps(data)

print(type(NewJson))

newValue = json.loads(NewJson)

print(type(newValue))


# re
import re

text = "my mobile number 4515454545"
num = r'\d{10}'
match = re.search(num,text)
if match:
    print(match.group())