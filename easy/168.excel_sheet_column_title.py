# https://leetcode.com/problems/excel-sheet-column-title/description/

def convert_to_title(column_number: int) -> str:
    result = ""

    while column_number > 0:
        column_number -= 1
        remainder = column_number % 26
        result = chr(ord("A") + remainder) + result
        column_number //= 26

    return result


column_number1 = 1
column_number2 = 28
column_number3 = 701


print(convert_to_title(column_number1))
print(convert_to_title(column_number2))
print(convert_to_title(column_number3))
