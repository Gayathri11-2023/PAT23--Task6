def distribute_mangoes(mangoes, students):
    sorted_mangoes = sorted(mangoes)
    diff = [sorted_mangoes[i + 1] - sorted_mangoes[i] for i in range(len(sorted_mangoes) - 1)]
    min_difference = min(diff)
    student_bags = {i: [] for i in range(students)}
    current_student = 0
    for mango in sorted_mangoes:
        student_bags[current_student].append(mango)
        current_student = (current_student + 1) % students
     return student_bags
mangoes_in_bag = [30,20,13,5,4,12]
num_students = 3
result = distribute_mangoes(mangoes_in_bag, num_students)
for student, bags in result.items():
    print(f"Student {student + 1}: {bags}")
