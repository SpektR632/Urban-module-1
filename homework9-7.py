def is_prime(func):
    def wrapper(*args):
        result = func(*args)
        if all(result % i for i in range(2, result//2+1)):
            print('Простое')
        else:
            print('Составное')
        return result
    return wrapper

@is_prime
def sum_three(*args):
    return sum(args)

result = sum_three(2, 3, 6)
print(result)

result = sum_three(2, 3, 23)
print(result)
