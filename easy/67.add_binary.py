# https://leetcode.com/problems/add-binary/description/

def add_binary(a: str, b: str) -> str:
    output = int(a, 2) + int(b, 2)
    return "{:b}".format(output)


a = "11"
b = "1"

# a = "1010"
# b = "1011"

add_binary(a, b)
