class Solution:
    def canFinish(self, numCourses: int, prerequisites: list[list[int]]) -> bool:

        graph = { i : [] for i in range(numCourses) }

        in_degree = { i: 0 for i in range(numCourses) }

        for node in graph:
            for neighbor in graph[node]:
                in_degree[neighbor] += 1


        q = collections.deque(in_degree[i] for i in in_)