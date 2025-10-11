class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        indegree = [0] * numCourses
        graph = defaultdict(list)

        for u,v in prerequisites:
            graph[u].append(v)
            indegree[v]+=1
        
        queue = deque()
        topo = list()

        for i in range(numCourses):
            if indegree[i] == 0:
                queue.append(i)
        
        while queue:
            node = queue.popleft()
            topo.append(node)
            for n in graph[node]:
                indegree[n]-=1
                if indegree[n] == 0:
                    queue.append(n)
        
        return topo[::-1] if len(topo) == numCourses else []