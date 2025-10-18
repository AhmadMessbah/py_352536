#  آرگومان a,b,c,d / پارامتر


def test(a, b, c=1, d=2):
    return a + b + c + d


# print(test(1, 2, 3, 4))

# print(test(1,2,3))

# print(test(1,2))

# print(test(1))

print(test(1,2,d=3))