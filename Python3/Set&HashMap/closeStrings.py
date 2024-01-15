'''
1657. Determine if Two Strings Are Close
Two strings are considered close if you can attain one from the other using the following operations:

Operation 1: Swap any two existing characters.
For example, abcde -> aecdb
Operation 2: Transform every occurrence of one existing character into another existing character, and do the same with the other character.
For example, aacabb -> bbcbaa (all a's turn into b's, and all b's turn into a's)
You can use the operations on either string as many times as necessary.

Given two strings, word1 and word2, return true if word1 and word2 are close, and false otherwise.

Example 1:
Input: word1 = "abc", word2 = "bca"
Output: true
Explanation: You can attain word2 from word1 in 2 operations.
Apply Operation 1: "abc" -> "acb"
Apply Operation 1: "acb" -> "bca"
'''
from collections import Counter
class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:

        if len(word1) != len(word2): return False

        if len(word1) == 0: return True

        if word1 == word2: return True

        w1 = Counter(word1)
        w2 = Counter(word2)

        if w1.keys() != w2.keys(): return False

        v1, v2 = list(w1.values()), list(w2.values())

        v1.sort()
        v2.sort()

        return v1 == v2


'''
class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        # The frequencies matters in our case! 
        # We have to check the two conditions:
            # frequencies of the characters are the same
            # Unique characters are the same
        if set(word1) != set(word2):
            return False
        counter1 = collections.Counter(word1).values()
        counter2 = collections.Counter(word2).values()
        return list(sorted(counter1)) == list(sorted(counter2))
'''