# https://leetcode.com/problems/ugly-number/description/

def is_ugly(n: int) -> bool:
    dividers = [2, 3, 5]

    if n <= 0:
        return False

    for i in dividers:
        while n % i == 0:
            n //= i

    return n == 1


n1 = 6
n2 = 1
n3 = 14

print(is_ugly(n1))
print(is_ugly(n2))
print(is_ugly(n3))
