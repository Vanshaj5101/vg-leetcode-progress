class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        indegree = [0] * numCourses
        queue = deque()
        graph = defaultdict(list)

        for u,v in prerequisites:
            indegree[v] += 1
            graph[u].append(v)
        
        for i in range(numCourses):
            if not indegree[i]:
                queue.append(i)
        
        topo = list()

        while queue:
            node = queue.popleft()
            topo.append(node)
            for n in graph[node]:
                indegree[n] -= 1
                if not indegree[n]:
                    queue.append(n)
        
        return list(reversed(topo)) if len(topo) == numCourses else []