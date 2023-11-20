def distribute_mangoes(mangoes, students):
    # Sort the list of mangoes in ascending order
    sorted_mangoes = sorted(mangoes)

    # Calculate the differences between consecutive elements
    differences = [sorted_mangoes[i + 1] - sorted_mangoes[i] for i in range(len(sorted_mangoes) - 1)]

    # Select the minimum difference
    min_difference = min(differences)

    # Initialize a dictionary to store bags for each student
    student_bags = {i: [] for i in range(students)}

    # Distribute bags to students based on the minimum difference
    current_student = 0
    for mango in sorted_mangoes:
        student_bags[current_student].append(mango)
        current_student = (current_student + 1) % students

    return student_bags

# Example usage
mangoes_in_bag = [30,20,13,5,4,12]
num_students = 3

result = distribute_mangoes(mangoes_in_bag, num_students)

# Display the result
for student, bags in result.items():
    print(f"Student {student + 1}: {bags}")
