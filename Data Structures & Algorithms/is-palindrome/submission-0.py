class Solution:
    def isPalindrome(self, s: str) -> bool:
        text = s
        cleaned = "".join(char.lower() for char in text if char.isalnum())
        reversetext = cleaned[::-1]
        return cleaned == reversetext