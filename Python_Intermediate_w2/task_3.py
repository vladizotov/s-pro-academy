def fib_generator(n):
    number_n, number_n_plus_1 = 0, 1

    counter = 0
    while counter < n:
        yield number_n
        number_n, number_n_plus_1 = number_n_plus_1, number_n + number_n_plus_1
        counter += 1

def fib_list(n):
    return list(fib_generator(n))