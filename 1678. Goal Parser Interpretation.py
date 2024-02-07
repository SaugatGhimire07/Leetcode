"""Intuition
In addressing this question, I recognized the need for a dictionary, 'replacements', 
to map distinct substrings within the command to their corresponding replacement values. 
My approach was to iterate through the dictionary's key-value pairs and replace occurrences 
of each key with its associated value in the command string. 
This method aligns with the idea of interpreting or transforming a command by substituting 
certain patterns with predefined representations. By implementing this string replacement logic, 
I aimed to capture the essence of interpreting commands with specific patterns in a concise and structured manner.

Approach
In developing the approach for this code, my focus was on efficiently implementing 
the string replacement logic based on the predefined mappings. 
I started by defining a dictionary, 'replacements', which contained the substrings to be replaced as keys 
and their corresponding replacement values. Then, I iterated through each key-value pair in the dictionary and 
used the 'replace' method to substitute all occurrences of the key with its 
associated value in the 'command' string. This systematic approach allowed for a streamlined and 
effective transformation of the input command string. By leveraging string manipulation techniques and 
the provided mappings, I aimed to achieve a clear and concise interpretation of the command, ensuring that the 
replacements accurately reflected the desired output.

Complexity
Time complexity: O(n)
Space complexity: O(1)"""

class Solution:
    def interpret(self, command: str) -> str:
        replacements = {
            "()": "o",
            "(al)": "al"
        }
        for i,j in replacements.items():
            command = command.replace(i,j)
        return command