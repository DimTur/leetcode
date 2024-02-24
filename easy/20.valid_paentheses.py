# https://leetcode.com/problems/valid-parentheses/
def is_valid(s: str) -> bool:
    stack = []
    mapping = {")": "(", "}": "{", "]": "["}

    for b in s:  # итерируемся по каждому элементу
        if b in mapping:  # проверяем, если символ есть в словаре как ключ
            top_element = stack.pop() if stack else "#"  # то извлекаем и удаляем последний элемент из stack
            if mapping[b] != top_element:  # проверяем если значение по ключу закрывающей скобки не равно
                # последнему элементу в stack
                return False
        else:
            stack.append(b)  # если b нет в словаре mapping как ключа, то добавляем его в stack, т.е. добавляем
            # открывающие скобки в stack

    return not stack


s1 = "()"
# true
s2 = "()[]{}"
# true
s3 = "(]"
# false

is_valid(s1)
is_valid(s2)
is_valid(s3)
