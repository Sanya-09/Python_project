import json

# Open the JSON file in read mode
fd = open('Record.json', 'r')
js = fd.read()
fd.close()

record = json.loads(js)  # Convert JSON string to dictionary

print("--------------------MENU---------------------")
for key in record.keys():
    print(key, record[key]['Name'], record[key]['Price'], record[key]['Qn'])
print("---------------------------------------------")
print('')
