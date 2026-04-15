class Solution:
    def isValid(self, s: str) -> bool:
        stk = []
        n = len(s)

        for i in range(n):
            
            if(s[i] in ['(', '[', '{']):
                stk.append(s[i])    #push

            if(s[i] in [')', ']', '}']):
                if(not stk):
                    return False
                top = stk.pop()    #pop

                if(top == '(' and s[i] == ')' 
                or top == '[' and s[i] == ']' 
                or top == '{' and s[i] == '}'):
                    pass
                else:
                    return False
        
        if(len(stk) == 0):
            return True
        return False