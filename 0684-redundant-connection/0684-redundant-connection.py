class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        parent = [i for i in range(len(edges)+1)]

        def find(x):
            if parent[x] != x:
                parent[x] = find(parent[x])
            return parent[x]
        
        def union(x, y):
            rootx = find(x)
            rooty = find(y)
            if rootx != rooty:
                parent[rooty] = rootx
                return True
            return False
        
        for u,v in edges:
            if not union(u,v):
                return [u,v]