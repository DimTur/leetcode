# https://leetcode.com/problems/climbing-stairs/description/

def climb_stairs(n: int) -> int:
    one, two = 1, 1
    for i in range(n - 1):
        temp = one
        one = one + two
        two = temp
    return one


# n = 2
n = 3
climb_stairs(n)
