class Solution:
    def getAllAdjacents(self, c: int, heights: List[int]) -> int:        
        n = len(heights)
        bigger_lefts = []
        bigger_rights = []

        i = c-1
        while(i>=0):
            if(heights[i]>=heights[c]):
                bigger_lefts.append(heights[i])
            else:
                break
            i-=1

        i = c+1
        while(i < n):
            if(heights[i]>=heights[c]):
                bigger_rights.append(heights[i])
            else:
                break
            i+=1
        return [len(bigger_lefts), len(bigger_rights)]


    def largestRectangleArea(self, heights: List[int]) -> int:
        
        n = len(heights)
        max_area = 0

        for i in range(n):
            [n_l, n_r] = (self.getAllAdjacents(i, heights))

            area = heights[i] + (heights[i]*(n_l + n_r))
            if(area > max_area):
                max_area = area

        return max_area


