def repeating_element(first):
    element_count = {}
    
    for num in first:
        element_count[num] = element_count.get(num, 0) + 1

    for num in first:
        if element_count[num] == 1:
            return num
    return None

input_list = [6,5,7,1,7,6,5]

result = repeating_element(input_list)

if result is not None:
    print(f"The first non-repeating element is: {result}")
else:
    print("No non-repeating element found in the list.")
