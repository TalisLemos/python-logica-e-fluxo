# Parte 1 - Visão Geral do Projeto

O Gerenciador de Registros de Alunos gerencia dados de alunos usando dicionários e conjuntos. Cada registro de aluno inclui seu nome, idade, notas e cursos. As operações principais incluem adicionar alunos, atualizar notas, verificar a matrícula em cursos, calcular médias de notas, listar alunos por curso e filtrar os melhores alunos com base em limites de notas.

Inicialize um dicionário vazio chamado student_records para armazenar os detalhes de todos os alunos. Este dicionário servirá como a base para o projeto, onde o nome de cada aluno será uma chave, e seus detalhes (idade, notas e cursos) serão armazenados como um dicionário aninhado.

# Parte 2 - Adicionar Aluno

Crie uma função chamada add_student que recebe três argumentos: name (string), age (inteiro) e courses (uma lista de strings). A função deve:

Verificar se o nome do estudante já existe no dicionário student_records. Se existir, imprima "Student '<name>' already exists.".
Se o nome não existir, adicione-o ao student_records com age, um conjunto vazio para grades (este modelo assume que cada valor de nota é único) e um conjunto de courses.
Imprima "Student '<name>' added successfully.".
Adicione o seguinte bloco de código na parte inferior do seu código:

add_student("Alice", 20, ["Math", "Physics"])
add_student("Bob", 22, ["Biology", "Chemistry"])
print(student_records)

# Parte 3 - Adicionar nota

Crie uma função chamada add_grade que recebe dois argumentos: name (string) e grade (inteiro). A função deve:

Verificar se o nome do aluno existe no dicionário student_records.
Se não existir, imprimir "Student '<name>' not found.".
Se o nome existir, adicionar o grade ao conjunto (set) grades do aluno.
Imprimir "Grade <grade> added for student '<name>'.".
Adicione (substitua) o seguinte bloco de código na parte inferior do seu código:

add_student("Alice", 20, ["Math", "Physics"])
add_student("Bob", 22, ["Biology", "Chemistry"])
add_grade("Alice", 90)
add_grade("Alice", 85)
add_grade("Bob", 75)
add_grade("Charlie", 80)  # Non-existent student
print(student_records)

# Parte 4 - Está matriculado
Crie uma função chamada is_enrolled que recebe dois argumentos: name (string) e course (string). A função deve:

Verificar se o nome do estudante existe no dicionário student_records.
Se não existir, imprimir "Student '<name>' not found." e retornar False.
Se o nome existir, verificar se o course está no conjunto courses do estudante.
Se estiver, retornar True.
Se não, retornar False.
Adicione (substitua) o seguinte bloco de código na parte inferior do seu código:

add_student("Alice", 20, ["Math", "Physics"])
add_student("Bob", 22, ["Biology", "Chemistry"])
add_grade("Alice", 90)
add_grade("Alice", 85)
add_grade("Bob", 75)
add_grade("Charlie", 80)  # Non-existent student
print(is_enrolled("Alice", "Math"))  # Should return True
print(is_enrolled("Alice", "Biology"))  # Should return False
print(is_enrolled("Bob", "Biology"))  # Should return True
print(is_enrolled("Charlie", "Math"))  # Non-existent student, should print message and return False

#Parte 5 - Média de notas

Crie uma função chamada calculate_average_grade que recebe um argumento: name (string). A função deve:

Verifique se o nome do aluno existe no dicionário student_records.
Se não existir, imprima "Student '<name>' not found." e retorne None.
Se o nome existir, calcule a média das notas no conjunto grades do aluno.
Se o conjunto grades estiver vazio, retorne 0.
Caso contrário, calcule e retorne a nota média como um float.
Adicione (substitua) o seguinte bloco de código na parte inferior do seu código:

add_student("Alice", 20, ["Math", "Physics"])
add_student("Bob", 22, ["Biology", "Chemistry"])
add_grade("Alice", 90)
add_grade("Alice", 85)
add_grade("Bob", 75)
print(calculate_average_grade("Alice"))  # Deve retornar 87.5
print(calculate_average_grade("Bob"))  # Deve retornar 75.0
print(calculate_average_grade("Charlie"))  # Aluno inexistente, deve imprimir a mensagem e retornar None
print(calculate_average_grade("Alice"))  # Deve retornar 87.5 novamente

# Parte 6 - Listar por curso
Mantenha tudo o que você escreveu nas etapas anteriores deste projeto: o arquivo inteiro é executado, então student_records e add_student ainda devem estar presentes.

Crie uma função chamada list_students_by_course que receba um argumento: course (string). A função deve:

Iterar pelo dicionário student_records e encontrar todos os alunos matriculados no course especificado.
Retornar uma lista com os nomes dos alunos matriculados no curso.
Se nenhum aluno estiver matriculado no curso, retornar uma lista vazia.
Adicione (substitua pelo) seguinte bloco de código ao final do seu código:

add_student("Alice", 20, ["Math", "Physics"])
add_student("Bob", 22, ["Math", "Biology"])
add_student("Diana", 23, ["Chemistry", "Physics"])
print(list_students_by_course("Math"))  # Should return ["Alice", "Bob"]
print(list_students_by_course("Physics"))  # Should return ["Alice", "Diana"]
print(list_students_by_course("Biology"))  # Should return ["Bob"]
print(list_students_by_course("History"))  # Should return an empty list

# Parte 7 - Melhores alunos
Crie uma função chamada filter_top_students que recebe um argumento: threshold (float). A função deve:

Iterar pelo dicionário student_records e encontrar todos os alunos cuja nota média seja maior que o threshold especificado.
Usar a função calculate_average_grade para obter a nota média de cada aluno.
Retornar uma lista de nomes dos melhores alunos.
Se nenhum aluno atender aos critérios, retornar uma lista vazia.
Adicione (substitua) o seguinte bloco de código na parte inferior do seu código:

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
