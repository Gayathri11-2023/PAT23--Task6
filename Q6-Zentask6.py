def find_duplicates(list1, list2, list3):
    combined_list = list1 + list2 + list3
    element_count = {}
    duplicates = []
    for i in combined_list:
        if i in element_count:
            element_count[i] += 1
            if element_count[i] == 2:
                duplicates.append(i)
        else:
            element_count[i] = 1
    return duplicates
list1 = [2, 4, 5, 2, 3]
list2 = [4, 5, 6, 7, 8]
list3 = [7, 8, 9, 10, 11, 10]
result = find_duplicates(list1, list2, list3)
print(f"The duplicates in the three lists are: {result}")

