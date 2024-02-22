def roman_to_int(s: str) -> int:
    num_dict = {
        "I": 1,
        "V": 5,
        "X": 10,
        "L": 50,
        "C": 100,
        "D": 500,
        "M": 1000,
    }
    res = 0

    for i in range(len(s)):
        if i + 1 < len(s) and num_dict[s[i]] < num_dict[s[i+1]]:
            res -= num_dict[s[i]]

        else:
            res += num_dict[s[i]]

    return res


s = input()
roman_to_int(s)
print(roman_to_int(s))
