# https://leetcode.com/problems/longest-common-prefix/
def longest_common_prefix(strs: list[str]) -> str:
    ans = ""

    for idx, s in enumerate(strs[0]):
        for word in strs[1:]:
            if len(word) < idx + 1 or word[idx] != s:
                return ans

        ans += s

    return ans


# strs = ["flower", "flow", "flight"]
# longest_common_prefix(strs)

strs = ["dog", "racecar", "car"]
longest_common_prefix(strs)