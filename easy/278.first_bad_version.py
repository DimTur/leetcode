# https://leetcode.com/problems/first-bad-version/description/

def first_bad_version(n: int) -> int:
    left = 0
    right = n

    while left < right:
        mid = (left + right) // 2
        if isBadVersion(mid):
            right = mid
        else:
            left = mid + 1

    return left


n1 = 5
n2 = 1
bad1 = 4
bad2 = 1

print(first_bad_version(n1))
print(first_bad_version(n2))
