#() {} [] 를 포함하고 있는 문자열 s가 주어졌을 때, 괄호가 유효한지 아닌지 판별하시오.

class Solution:
    def isValid(self, s: str) ->bool:
        stack = []
        for p in s:
            if p == '(' :
                stack.append(')')
            elif p == '{' :
                stack.append('}')
            elif p == '[' :
                stack.append(']') 
            elif stack and stack[-1] == p : #stack이 존재하고 stack의 제일 마지막 요소가 p 와 같다면
                stack.pop()
            else:
                return False
        
        return not stack