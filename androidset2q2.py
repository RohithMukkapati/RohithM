from typing import List
from collections import deque

class Solution:
    def hasCircularDependency(self, n: int, edges: List[List[int]]) -> bool:
        adj = [[] for _ in range(n)]
        indegree = [0] * n
        ans = []

        for i, edge in edges:
            adj[edge].append(i)
            indegree[i] += 1

        queue = deque()
        for i in range(n):
            if indegree[i] == 0:
                queue.append(i)

        while queue:
            current = queue.popleft()
            ans.append(current)

            for j in adj[current]:
                indegree[j] -= 1
                if indegree[j] == 0:
                    queue.append(j)

        return len(ans) == n


if __name__ == "__main__":
    try:
        n = int(input("Enter n: "))
        m = int(input("Enter the number of pairs: "))

        edges = []
        print(f"Enter {m}  pairs as two integers:")
        for _ in range(m):
            pair = list(map(int, input().strip().split()))
            edges.append(pair)

        solution = Solution()
        result = solution.hasCircularDependency(n, edges)
        print(not result)
    except ValueError:
        print("Invalid input. Please enter valid integers.")
 