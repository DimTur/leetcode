# https://leetcode.com/problems/power-of-two/description/

def is_power_of_two(n: int) -> bool:
    power = 1

    while power < n:
        power *= 2

    return power == n


n1 = 1
n2 = 16
n3 = 3

print(is_power_of_two(n1))
print(is_power_of_two(n2))
print(is_power_of_two(n3))
