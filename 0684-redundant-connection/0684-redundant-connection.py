class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        
        graph = defaultdict(list)

        visited = set()

        def cycle(node1, node2):
            if node1 == node2:
                return True
            
            visited.add(node1)
    
            for neighbor in graph[node1]:
                if neighbor not in visited:
                    if cycle(neighbor, node2):
                        return True
            
            return False

        
        for a,b in edges:
            if a in graph and b in graph:
                visited.clear()
                if cycle(a,b):
                    return [a,b]
            graph[a].append(b)
            graph[b].append(a)
        
        return []
            