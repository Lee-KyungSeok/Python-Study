students = []

student1_info = {
    "first_name": "lee",
    "last_name": "seok",
    "student_no": 3498
}

student2_info = {
    "first_name": "lee",
    "last_name": "hyun",
    "student_no": 9145
}

student3_info = {
    "first_name": "shin",
    "last_name": "in",
    "student_no": 6341
}

students.append(student1_info);
students.append(student2_info);
students.append(student3_info);

def sort_help(d):
    return d['student_no']

# sorted 함수에 key를 넣어 key의 순서로 정렬 가능
sorted_students = sorted(students, key=sort_help) 
print(sorted_students)

# lambda 식 이용
sorted_students = sorted(students, key=lambda x: x['student_no']); 
print(sorted_students)