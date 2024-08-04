class Solution:
    def shortestDistanceAfterQueries(self, n: int, queries: List[List[int]]) -> List[int]:
        adj_list = defaultdict(list) 
        for i in range(0,n-1):
            adj_list[i].append(i+1)
        
        res = [] 
        for n1 , n2 in (queries):
            adj_list[n1].append(n2)
            min_dist = n #dist can't be greater than n
            queue = [[0,0]]
            visited = set()
            
            while queue:
                dist, node = heapq.heappop(queue)
                for num in adj_list[node]:
                    if num == n - 1:
                        min_dist = min(min_dist, dist+1)
                        continue 
                    if num not in visited:
                        visited.add(num)
                        heapq.heappush(queue, [dist + 1,num])

            res.append(min_dist) 

        return res
            
        
        
        