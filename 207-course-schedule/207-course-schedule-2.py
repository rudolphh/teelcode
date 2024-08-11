from collections import deque

class Solution:
    def canFinish(self, numCourses: int, prerequisites: list[list[int]]) -> bool:

        graph = { i : [] for i in range(numCourses) }
        in_degree = { i: 0 for i in range(numCourses) }

        for course, pre in prerequisites:
            graph[pre].append(course)
            in_degree[course] += 1


        q = deque(node for node in in_degree if in_degree[node] == 0)
        count = 0

        while q:
            node = q.popleft()
            count += 1

            for neighbor in graph[node]:
                in_degree[neighbor] -= 1
                if in_degree[neighbor] == 0:
                    q.append(neighbor)

        
        return count == numCourses