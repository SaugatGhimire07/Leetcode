class Solution:
    def countMatches(self, items: List[List[str]], ruleKey: str, ruleValue: str) -> int:
        count = 0

        for sublist in items:
            if ruleKey == "type" and sublist[0] == ruleValue:
                count += 1
            elif ruleKey == "color" and sublist[1] == ruleValue:
                count += 1
            elif ruleKey == "name" and sublist[2] == ruleValue:
                count += 1
            else:
                pass
        return count