""" Write a function to find the longest common prefix string amongst an array of strings.

If there is no common prefix, return an empty string "".



Example 1:

Input: strs = ["flower","flow","flight"]
Output: "fl"

Example 2:

Input: strs = ["dog","racecar","car"]
Output: ""
Explanation: There is no common prefix among the input strings.



Constraints:

    1 <= strs.length <= 200
    0 <= strs[i].length <= 200
    strs[i] consists of only lowercase English letters.

"""


"""Leetcode gave base structure"""

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        pass

"""Here is solution for this problem"""

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        strs.sort(key = lambda x:len(x))      # Using lambda function for find x length and sorting
        prefix = strs[0]    # prefix get first item in ther strs list item
        for i in range(len(strs[0]),0,-1):      # for can chech from first letter to end of that and count length
            if all([prefix[:i] == strs[j][:i] for j in range(1,len(strs))]):   # All words value == i and == [j] [:i] and loop for ranging length of the strs list
                return(prefix[:i])
        return ""