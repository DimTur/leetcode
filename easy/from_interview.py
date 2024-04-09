# Найдите символ с максимальным количеством последовательных вхождений в заданной строке.
# 'bbbaaaaccadd';

def max_count_char(s: str) -> str:
    res = None
    counter_1 = 0
    counter_2 = 0

    for i in range(1, len(s)):
        if s[i] == s[i - 1]:
            counter_1 += 1
        else:
            if counter_1 > counter_2:
                counter_2 = counter_1
                res = s[i - 1]
            counter_1 = 1

    if counter_1 > counter_2:
        counter_2 = counter_1
        res = s[-1]

    return res


s = "bbbaaaaccadd"
print(max_count_char(s))
