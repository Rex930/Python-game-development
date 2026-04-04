students = {
    "S001":{ 
    "name": "Alex",
    "age":15,
    "class":"10th",
    "marks": {
        "math": 88,
        "science": 92,
        "english": 85
    }
},
"S002":{
 "name": "Immanuel",
 "age":14,
 "class":"9th",
 "marks": {
    "math": 82,
    "science": 83,
    "english": 85
}
},
"S003":{
 "name": "Bob",
 "age":13,
 "class":"8th",
 "marks": {
    "math": 78,
    "science": 81,
    "english": 89
}
},
"S004":{
 "name": "George",
 "age":15,
 "class":"8th",
 "marks": {
    "math": 87,
    "science": 90,
    "english": 95
}
},
"S005":{
 "name": "Kyle",
 "age":12,
 "class":"12th",
 "marks": {
    "math": 93,
    "science": 93,
    "english": 95
}
}
}
for student_id, student_data in students.items():
    print("\nStudent ID:", student_id)
    print("Name:", student_data["name"])
    print("Age:", student_data["age"])
    print("Class:", student_data["class"])
    print("Marks:")
    for subject, score in student_data["marks"].items():
       print(" ",subject,":", score)
for student_data in students.values():
    student_data["marks"]["math"] += 5
print("\nUpdated Math marks after Bonus:")
for student_id, student_data in students.items():
    print(student_id,"->", student_data["marks"]["math"])
