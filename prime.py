def is_prime(num):
    if num <= 1:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True

def primes_in_range(start, end):
    prime_list = []
    for number in range(start, end + 1):
        if is_prime(number):
            prime_list.append(number)
    return prime_list

start=int(input())
end=int(input())

print( primes_in_range(start, end))
