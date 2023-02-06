import pandas as pd

df_teacher = pd.DataFrame({
    "name": ["Pep Guardiola", "Jurgen Klopp", "Mikel Arteta", "Zinedine Zidane"], 
    "school": ["Manchester High School", "Liverpool High School", "Arsenal High", None], 
    "married": [True, True, False, True]
})

df_student = pd.DataFrame({
    "student": ["Roberto Firmino", "Andrew Robertson", "Dani Ceballos", "Bukayo Saka", "Gabriel Martinelli", "Thomas Partey"], 
    "teacher_name": ["Jurgen Klopp", "Jurgen Klopp", "Mikel Arteta", "Mikel Arteta", "Mikel Arteta", "Mikel Arteta"], 
    "age": [31.0, 28.6, 23.0, 21.0, 21.0, 29.0], 
    "height": [2.1, 2.1, 2.1, 2.1, 2.1, 2.1]
})

result = {
    "teachers": []
}

for index, row in df_teacher.iterrows():
    teacher = {
        "teacher": row["name"], 
        "school": row["school"], 
        "married": row["married"], 
        "students": []
    }
    
    students = df_student[df_student["teacher_name"] == row["name"]]
    students_list = students.to_dict("records")
    
    for student in students_list:
        teacher["students"].append({
            "student": student["student"], 
            "age": student["age"], 
            "height": student["height"]
        })
    
    result["teachers"].append(teacher)

print(result)

