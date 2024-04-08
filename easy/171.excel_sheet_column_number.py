# https://leetcode.com/problems/excel-sheet-column-number/description/
import string


def title_to_number(column_title: str) -> int:
    result = 0

    for char in column_title:
        strs = ord(char) - ord("A") + 1
        result = result * 26 + strs

    return result


column_title1 = "A"
column_title2 = "AB"

print(title_to_number(column_title1))
print(title_to_number(column_title2))
