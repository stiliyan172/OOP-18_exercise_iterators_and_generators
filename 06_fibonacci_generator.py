def fibonacci():
    fib0 = 0
    fib1 = 1

    yield fib0
    yield fib1

    while True:
        next_number = fib0 + fib1
        yield next_number
        fib0 = fib1
        fib1 = next_number


generator = fibonacci()
for i in range(10):
    print(next(generator))

# def fibonacci():
#     first = 0
#     second = 1
#     while True:
#         yield first
#         result = first + second
#         first = second
#         second = result
