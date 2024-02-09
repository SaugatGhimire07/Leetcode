class Solution:
    def sortSentence(self, s: str) -> str:
        arr = []
        for i in s.split():
            new_word = i[-1] + i[:-1]
            arr.append(new_word)
        arr.sort()
        ans = ''
        for i in arr:
            ans += i[1:] + ' '
        return ans[:-1]