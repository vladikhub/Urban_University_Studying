def is_prime(func):
    def wrapper(*args):

        res = func(*args)
        for i in range(2, int(res**0.5)+1):
            if res % i == 0:
                print("Составное")
                return res
        print("Простое")
        return res
    return wrapper


@is_prime
def sum_three(a, b, c):
    return a + b + c


print(sum_three(1, 3, 3))
