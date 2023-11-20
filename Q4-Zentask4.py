def sum_digit(number):
     number_str = str(number)
     first_digit = int(number_str[0])
     last_digit = int(number_str[-1])
     sum = first_digit + last_digit
     return sum

input_number = int(input())
result = sum_digit(input_number)
print("Sum of first and last digit is :", result )