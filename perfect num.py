def is_perfect_number(n):
    if n <= 0:
        return False

    sum_of_divisors = 0

    for i in range(1, n):
        if n % i == 0:
            sum_of_divisors += i

    return sum_of_divisors == n

num = int(input("Enter a number: "))

if is_perfect_number(num):
    print(f"{num} is a Perfect Number.")
else:
    print(f"{num} is not a Perfect Number.")
