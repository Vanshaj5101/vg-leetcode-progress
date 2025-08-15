class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        graph = defaultdict(list)
        for a, b in prerequisites:
            graph[b].append(a)
        
        UNVISITED = 0
        VISITING = 1
        VISITED = 2
        status = [UNVISITED] * numCourses
        order = []

        def is_cycle(node):
            if status[node] == VISITING:
                return True
            elif status[node] == VISITED:
                return False
            else:
                status[node] = VISITING
                for n in graph[node]:
                    if is_cycle(n):
                        return True
                status[node] = VISITED
                order.append(node)

        
        for i in range(numCourses):
            if is_cycle(i):
                return []
        return order[::-1]
