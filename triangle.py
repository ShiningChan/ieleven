from collections import Iterator


def triangle():
    N = [1]
    while True:
        yield N
        N.append(0)
        N = [N[i - 1] + N[i] for i in range(len(N))]

o = triangle()

print(next(o))
print(next(o))
print(next(o))

