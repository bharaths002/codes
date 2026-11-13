
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        res_set = set()
        res = 0
        l = 0

        for i in range(0, len(s)):
            while s[i] in res_set:
                res_set.remove(s[l])
                l += 1

            res_set.add(s[i])
            res = max(res, i - l + 1)

        return res


# Main program
# s = input("Enter a string: ")
s = "abcabcbb"  # Example input string
solution = Solution()
result = solution.lengthOfLongestSubstring(s)

print("Length of longest substring:", result)
