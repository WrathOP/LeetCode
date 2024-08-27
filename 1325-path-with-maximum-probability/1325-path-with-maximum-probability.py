import heapq
from collections import defaultdict
from typing import List

class Solution:
    def maxProbability(
        self,
        n: int,
        edges: List[List[int]],
        succProb: List[float],
        start_node: int,
        end_node: int,
    ) -> float:
        adjList = defaultdict(list)
        for i, edge in enumerate(edges):
            n1, n2 = edge
            adjList[n1].append((succProb[i], n2))
            adjList[n2].append((succProb[i], n1))

        # Max-heap: store (-probability, node)
        queue = [(-1.00, start_node)]
        visited = set()
        maxProb = 0

        while queue:
            prob, node = heapq.heappop(queue)
            prob = -prob 

            if node == end_node:
                return prob

            if node in visited:
                continue

            visited.add(node)
            
            for nextProb, nextNode in adjList[node]:
                if nextNode not in visited:
                    heapq.heappush(queue, (-prob * nextProb, nextNode))
        
        return 0.0 
