def check_prime(number):
    if number < 2:
        return False
    for i in range(2, int(number**0.5)+1):
        if number % i == 0:
            return False
    return True
    

    
given_list = [10, 501, 22, 37, 100, 999, 87, 351]
prime_list = [num for num in given_list if check_prime(num)]
count_prime = len(prime_list)

print("prime numbers is in given list: ", prime_list)
print("count of prime numbers is in given list:", count_prime)

