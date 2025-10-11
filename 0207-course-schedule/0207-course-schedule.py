class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        indegree = [0] * numCourses
        graph = defaultdict(list)

        for u,v in prerequisites:
            indegree[v]+=1
            graph[u].append(v)

        que = deque()
        
        for i in range(numCourses):
            if indegree[i] == 0:
                que.append(i)
        topo = list()
        while que:
            node = que.popleft()
            topo.append(node)
            for n in graph[node]:
                indegree[n] -= 1
                if indegree[n] == 0:
                    que.append(n)
        
        return len(topo) == numCourses