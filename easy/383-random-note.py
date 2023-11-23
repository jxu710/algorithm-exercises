class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        # Convert magazine and ransomNote strings to lists
        magazineArr = list(magazine)
        ransomArr = list(ransomNote)

        for char in ransomArr:
            if char in magazineArr:
                # If present, remove the character from magazineArr so we don't count it again in the loop
                magazineArr.remove(char)
            else:
                return False

        return True
