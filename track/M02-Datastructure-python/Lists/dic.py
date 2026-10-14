#{key:value},mutable, key cannot be duplicate
student={
    'name': "Amit",
    "name": "Rahul",
    "age":  "21",
    "course" : "computer science",
    "Tech": ["computer scince", "python", "sql"]
}
student["age"] = 25
student.update({'cgpa' : 8.5})
print(student["age"])
print(student, type(student), len(student))
print(student.keys())
print(student.values())
print(student.items())
print(student.get("cgpa"))

print(student.pop("course"))
student.popitem()
student.clear()
del student

student = {
    "name":"rahul",
    "age" :23
    "Tech" : ["python", "sql"] 
}
student.setdefault("age", 22)
print(student)

keys=["name", "age", "course"]
y=0

student=dict.fromkeys(keys.y)
print(student)

my_dict=student.copy()
print(my_dict)
my_dict.update({'name' "Amit"})
print(my_dict)

student={
    "name":"rahul",
    "language": "jave"
    "marks": 88
}
for x in student:
    print(f"{x} => {student[x]}")

for x in student.items():
    print(x)

for x in student.keys():
    print(x)

for x in student.values():
    print(x)

student ={
    "stu1": {
        "name": "rahul",
        "age": 21,
        "course":"computer science"
        
    },
    "stu2": {
        "name": "amit",
        "age": 22,
        "course": "python"
    },
    "stu3": {
        "name": "sumit",
        "age": 23,
        "course": "sql"
    }
}


