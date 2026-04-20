class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        
        n = len(temperatures)
        indices = [0]*n
        s = []
        
        for i, temp in enumerate(temperatures):
                
            while s and temperatures[s[-1]] < temp:
                index = s.pop()
                indices[index] = i - index
            
            s.append(i)

        return indices
                
                    