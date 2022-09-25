def fact(n):
    assert n >= 0  and int(n) == n, 'The number must be positive and integer only'
    if n == 0 or n == 1:
        return  1
    else:
         return n *  fact(n - 1)

print(fact(5))
