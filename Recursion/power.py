def power(base, exp):
    assert int(exp) == exp and exp >= 0, 'The Exponent value must be intefer and positive only.'
    if exp == 0:
        return 1
    if exp == 1:
        return base
    else:
        return base * power(base, exp - 1)
    
print(power(3, 3))
