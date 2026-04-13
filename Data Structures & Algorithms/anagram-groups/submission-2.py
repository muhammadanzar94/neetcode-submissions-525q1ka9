class Solution:

    def isAnagram(self, s: str, t: str):

        l = len(s)

        if(l != len(t)):
            return False

        h_map = {}

        for i in range(l):
            if s[i] in h_map:
                h_map[s[i]] = h_map[s[i]] + 1
            else:
                h_map[s[i]] = 1

        for i  in range(l):
            if t[i] in h_map:
                h_map[t[i]] = h_map[t[i]] - 1
                if(h_map[t[i]] == 0):
                    h_map.pop(t[i], None)
            else:
                return False

        if(len(h_map) == 0):
            return True

    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        length = len(strs)
        h_map = {}
        i_map = {}

        for i in range(length):
            for j in range(i+1, length):

                if(strs[j]+str(j) not in i_map):
                    if(self.isAnagram(strs[i], strs[j])):
                        if strs[i] in h_map:
                            h_map[strs[i]].append(strs[j])
                        else:
                            h_map[strs[i]] = [strs[j]]
                        i_map[strs[j]+str(j)] = True
                        i_map[strs[i]+str(i)] = True

        
        new_strs = []

        for key, val in h_map.items():
            val.append(key)
            new_strs.append(val)


        for i in range(length):
            if(strs[i]+str(i) not in i_map):
               new_strs.append([strs[i]])
            
        return new_strs



