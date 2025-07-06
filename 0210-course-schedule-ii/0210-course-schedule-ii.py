class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        graph = defaultdict(list)
        for a,b in prerequisites:
            graph[b].append(a)
        
        VISITED = 2
        VISITING = 1
        UNVISITED = 0

        status = [UNVISITED] * numCourses
        res = []
        def is_cycle(root):
            if status[root] == VISITED:
                return False
            elif status[root] == VISITING:
                return True
            else:
                status[root] = VISITING
                for n in graph[root]:
                    if is_cycle(n):
                        return True
                status[root] = VISITED
                res.append(root)
                return False
        
        for i in range(numCourses):
            if is_cycle(i):
                return []
        return res[::-1]