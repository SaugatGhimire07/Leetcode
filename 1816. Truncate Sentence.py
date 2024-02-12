class Solution:
    def truncateSentence(self, s: str, k: int) -> str:
        arr = s.split()
        while k < len(arr):
            arr.pop(k)
            
        return " ".join(arr)