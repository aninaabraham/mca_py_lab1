people = [
    {"name": "John Doe", "age": 30, "bg": "A+"},
    {"name": "Jane Smith", "age": 25, "bg": "B-"},
    {"name": "Emily Dabis", "age": 40, "bg": "O+"},
    {"name": "Jane Smith", "age": 35, "bg": "AB-"},
    {"name": "Michael Brown", "age": 25, "bg": "B+"},
    {"name": "william Johnson", "age": 22, "bg": "B+"},
    {"name": "Emma Wilson", "age": 25, "bg": "B+"},
    {"name": "Oliver Martinez", "age": 33, "bg": "O-"},
    {"name": "James Thomas", "age": 45, "bg": "A+"},
    {"name": "Isabella Lee", "age": 38, "bg": "B-"},
   
]

def people_info(people):
    for person in people:
        print("Name: " + person['name'])
        print("Age: " + str(person['age']))
        print("Blood Group: " + person['bg'])
        print('-' * 20)

people_info(people)
