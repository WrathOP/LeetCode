class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []
        
        phone_map = {
            '2': 'abc',
            '3': 'def',
            '4': 'ghi',
            '5': 'jkl',
            '6': 'mno',
            '7': 'pqrs',
            '8': 'tuv',
            '9': 'wxyz'
        }

        def recursion(combination,digits):
            if len(digits)==0:
                output.append(combination)
            else:
                for c in phone_map[digits[0]]:
                    recursion(combination+c,digits[1:])
        
        output = []
        recursion("",digits)
        return output