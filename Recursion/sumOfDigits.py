def sumOfDigits(n):
    assert int(n) == n and n >=0, 'The number must be positive and integer'
    if n == 0:
        return 0
    return n % 10 + sumOfDigits(n // 10)

print(sumOfDigits(1234))
