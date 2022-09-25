def fibonacci(n):
    assert int(n) == n and n >=0, 'The number must be positive and integer'
    if n in [0, 1]:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)

for i in range(10):
       print(fibonacci(i), end=', ')
