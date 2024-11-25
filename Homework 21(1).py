import json
import threading

def create_json(file_name, name, age):
    data = {"Name": name, "Age": age}
    try:
        with open(file_name, 'w') as file:
            json.dump(data, file)
        print(f"Created {file_name} with data: {data}")
    except Exception as e:
        print(f"Error creating {file_name}: {e}")

def parse_json(file_name):
    try:
        with open(file_name, 'r') as file:
            data = json.load(file)
            print(f"File: {file_name}")
            print(f"Name: {data['Name']}, Age: {data['Age']}")
    except Exception as e:
        print(f"Error reading {file_name}: {e}")

json_data = [
    ('person1.json', 'Natia', 34),
    ('person2.json', 'Tatia', 32),
    ('person3.json', 'Nutsa', 9)
]

for file_name, name, age in json_data:
    create_json(file_name, name, age)

threads = []
for file_name, _, _ in json_data:
    thread = threading.Thread(target=parse_json, args=(file_name,))
    threads.append(thread)
    thread.start()

for thread in threads:
    thread.join()
