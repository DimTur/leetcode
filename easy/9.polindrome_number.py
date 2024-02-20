x = input()


def is_palindrome(x: int) -> bool:
    str_x = str(x)
    reversed_x = str_x[::-1]
    if reversed_x == str_x:
        print(f"{x}, reads as {reversed_x} from left to right and from right to left.")
        return True
    else:
        print(f"From left to right, it reads {x}. From right to left, it becomes {reversed_x}. "
              f"Therefore it is not a palindrome.")
        return False


is_palindrome(x)
