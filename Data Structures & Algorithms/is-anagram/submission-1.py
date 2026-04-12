class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        l = len(s)

        # if lengths does not match
        if(l != len(t)):
            return False

        harr = {}

        for i in range(l):
            harr[s[i]] = harr.get(s[i], 0) + 1

        for i in range(l):
            val = harr.get(t[i], None) 

            # if value not set or zero
            if(val == None or val == 0): 
                return False
            else:
                harr[t[i]] = val - 1

                if val - 1 == 0:
                    harr.pop(t[i], None)


        
        if(len(harr) == 0):
            return True
        else:
            return False