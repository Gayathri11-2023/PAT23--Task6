
given_list = [10, 501, 22, 37, 100, 999, 87, 351]
even_numbers = []
odd_numbers = []
for number in given_list:
    if number % 2 == 0:
        even_numbers.append(number)
    else:
        odd_numbers.append(number)
print("Given list", given_list)
print("Even number List :" , even_numbers)
print("Odd number List:" ,odd_numbers)
    

