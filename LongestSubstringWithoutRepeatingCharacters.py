# Given a string s, find the length of the longest substring without repeating characters.
# Input: s = "abcabcbb"
# Output: 3
# Explanation: The answer is "abc", with the length of 3.


# Sliding technique using dictionary

def lengthOfLongestSubstring(s: str) -> int:
    if len(s) == 0:
        return 0
    map = {}
    max_length = start = 0
    for i in range(len(s)):
        if s[i] in map and start <= map[s[i]]:
            start = map[s[i]] + 1
            
        else:
            max_length = max(max_length, i-start+1)
        map[s[i]] = i
    print (max_length)


lengthOfLongestSubstring(s="abcabccbb")
