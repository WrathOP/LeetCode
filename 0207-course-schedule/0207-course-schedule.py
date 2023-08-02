class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        indegree = [0] * numCourses
        adj = [[] for _ in range(numCourses)]

        for prerequisite in prerequisites:
            adj[prerequisite[1]].append(prerequisite[0])
            indegree[prerequisite[0]]+=1
        
        queue = deque()
        for i in range(numCourses):
            if indegree[i]==0:
                queue.append(i)
        
        nodesVisited = 0
        while queue:
            node = queue.popleft()
            nodesVisited += 1

            for nei in adj[node]:
                indegree[nei] -= 1
                if indegree[nei]==0:
                    queue.append(nei)
        return nodesVisited == numCourses
            