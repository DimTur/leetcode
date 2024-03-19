# https://leetcode.com/problems/plus-one/description/

def plus_one(digits: list[int]) -> list[int]:
    digits_str = "".join(map(str, digits))
    new_num = str(int(digits_str) + 1)
    new_num_list = [int(num) for num in new_num]

    return new_num_list


# digits = [1,2,3]
digits = [4,3,2,1]
# digits = [9]

plus_one(digits)