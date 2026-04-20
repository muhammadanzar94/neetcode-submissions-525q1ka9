class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:

        time_to_finish = defaultdict()
        for index, value in enumerate(position):
            time_to_finish[value] = (target - value) / speed[index]
        
        position.sort()

        stack = []

        #loop from right to left
        for i in range(len(position) - 1, -1, -1):
            stack.append(time_to_finish[position[i]])
            if len(stack) >= 2 and stack[-1] <= stack[-2]:
                stack.pop()

        return len(stack)     
            