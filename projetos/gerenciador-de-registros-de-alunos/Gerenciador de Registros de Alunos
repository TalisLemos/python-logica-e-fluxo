student_records = {}

def add_student (name: str, age: int, courses: list[str]):

    courses_set = set(courses)
    grades = set()


    if name in student_records:
        print(f"Student '{name}' already exists.")
    else:
        student_records[name] = {"age": age, "grades": set(), "courses": set(courses)}
        print(f"Student '{name}' added successfully.")

#######################

def add_grade(name: str, grade: int):

    grades = set()

    if name in student_records:
        student_records[name]["grades"].add(grade)
        print(f"Grade {grade} added for student '{name}'.")
    else:
        print(f"Student '{name}' not found.")

#######################

def is_enrolled(name: str, course: str):

    if name in student_records:
        if course in student_records[name]["courses"]:
            return True
        else:
            return False
    else:
        print(f"Student '{name}' not found.")
        return False

#######################

def calculate_average_grade(name:str):

    if name in student_records:
        grades = student_records[name]["grades"]
        if not grades:
            return 0
        soma_das_notas = sum(grades)
        qnt_notas = len(grades)
        media_notas = soma_das_notas / qnt_notas
        return media_notas
    else:
        print(f"Student '{name}' not found.")
        return None
      
################

def list_students_by_course(course:str):

    alunos_matriculados = []

    for name in student_records:
        if course in student_records[name]["courses"]:
            alunos_matriculados.append(name)
    return alunos_matriculados
       
########################

def filter_top_students(threshold: float):

    melhores_alunos = []

    
    for name in student_records:
        calculate_average_grade(name)
        media_notas = calculate_average_grade(name)
        if media_notas > threshold:
            melhores_alunos.append(name)
    return melhores_alunos





#######################código na parte inferior do seu código:

add_student("Alice", 20, ["Math", "Physics"])
add_student("Bob", 22, ["Math", "Biology"])
add_student("Diana", 23, ["Chemistry", "Physics"])
add_grade("Alice", 90)
add_grade("Alice", 85)
add_grade("Bob", 75)
add_grade("Diana", 95)
print(filter_top_students(80))  # Deve retornar ["Alice", "Diana"]
print(filter_top_students(90))  # Deve retornar ["Diana"]
print(filter_top_students(100))  # Deve retornar uma lista vazia
