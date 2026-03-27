marks = {"math": 85, "science": 90, "english": 78}

max_subject = max(marks, key=marks.get)
print(max_subject, marks[max_subject])