
def happy_number(n, seen=set()):
    while n != 1 and n not in seen:
        seen.add(n)
        n = sum(int(digit) ** 2 for digit in str(n))
    return n == 1

given_list = [10, 501, 22, 37, 100, 999, 87, 351]

count_of_happy_numbers = sum(1 for num in given_list if happy_number(num))
print(f"Count of happy numbers: {count_of_happy_numbers}")
 