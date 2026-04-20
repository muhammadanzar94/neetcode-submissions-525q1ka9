class Solution:

    def performOperation(self, a: int, b: int, s: str) -> int:
        print(a, s, b)
        if(s == "+"):
            return a + b
        elif(s == "-"):
            return a - b
        elif(s == "*"):
            return a * b
        elif(s == "/"):
            return int(a / b)


    def evalRPN(self, tokens: List[str]) -> int:
        s = []
        operators = ["+", "-", "/", "*"]
        result = None
        result_first = False

        if(len(tokens)==1):
            return int(tokens[0])

        for token in tokens:
            if token not in operators:
                s.append(int(token))
            
            else:
                if s: 
                    b = s.pop()
                    a = s.pop()
                    result = self.performOperation(a, b, token)
                    s.append(result)

        return result

