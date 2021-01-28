'''
    Factors using generators and iterators
'''
# typical way using functions no gens
def factors(n):
    results = []  # empty holder list
    for k in range(1,n+1):
        if n % k == 0:
            results.append(k)  # if divides evenly, k is factor
    return results  # return list


# using generators
def factors(n):
    for k in range(1,n+1):
        if n % k == 0:
            yield k  # yield this as next result

# in actual practice
def factors(n):
    k = 1
    while k * k < n: # while k < sqrt(n)
        if n % k == 0:
            yield k
            yield n // k
        k += 1
    if k * k == n: # n is a perfect square
        yield k
