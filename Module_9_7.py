def is_prime(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        if result > 1:
            for i in range(2, result):
                if (result % i) == 0:
                    print(f"Составное число {result}")
                    break
            else:
                print(f"Простое число {result}")
        else:
            print("Составное")
    return wrapper

@is_prime
def sum_three(a, b, c):
    return a + b + c

result = sum_three(2, 3, 6)
print(result)
