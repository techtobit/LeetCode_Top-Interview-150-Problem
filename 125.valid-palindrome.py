#
# @lc app=leetcode id=125 lang=python3
#
# [125] Valid Palindrome
#

# @lc code=start
class Solution:
    def isPalindrome(self, s: str) -> bool:
        # newStr=re.sub(r'[^a-zA-Z0-9]', '', s).lower()
        # return newStr[::-1]==newStr
        l=0
        r=len(s)-1
        while l<r:
            if not s[l].isalnum():
                l+=1
            elif not s[r].isalnum():
                r-=1
            elif s[l].lower()==s[r].lower():
                l +=1
                r -=1
            else:
                return False
        return True
   
        
# @lc code=end

