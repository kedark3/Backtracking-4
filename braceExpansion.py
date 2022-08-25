# Approach: Recursion with Backtracking
# TC: O(k^(n/k)) where k is avg len of the block
# SC: O(n)
class Solution:
    def expand(self, s: str) -> List[str]:
        self.result = []
        groups, ptr = [], 0
        
        while ptr < len(s):
            if s[ptr] == '{':
                ptr += 1
                tmp = []
                while s[ptr] != '}':
                    if s[ptr] != ',':
                        tmp.append(s[ptr])
                    ptr+=1 
            else:
                tmp = [s[ptr]]
            ptr += 1
            tmp.sort()
            groups.append(tmp)
        self.helper(groups, 0, [])
        return self.result
    
    def helper(self, groups, idx, path):
        # base case
        if len(path) == len(groups):
            self.result.append(''.join(path))
            return
        
        # logic
        for i in groups[idx]:
            # action
            path.append(i)
            # recurse
            self.helper(groups, idx+1, path)
            # backtrack
            path.pop()

                        