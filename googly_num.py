#write a program to check  it is googly number or not
def is_prime(n):
    if n <= 1:
        return False
    i = 2
    while i * i <= n:
        if n % i == 0:
            return False
        i += 1
    return True

def is_googly_number(num):
    original = num
    sum_of_squares = 0

    while num > 0:
        digit = num % 10
        sum_of_squares += digit * digit
        num = num // 10

    return is_prime(sum_of_squares)

number = int(input("Enter a number: "))
if is_googly_number(number):
    print(number, "is a Googly Number")
else:
    print(number, "is NOT a Googly Number")
