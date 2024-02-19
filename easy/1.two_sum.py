def two_sum(nums: list[int], target: int) -> list[int]:
    known_numbers = {}
    for idx, num in enumerate(nums):
        neutral = target - num
        if neutral in known_numbers:
            return [known_numbers[neutral], idx]
        known_numbers[num] = idx
