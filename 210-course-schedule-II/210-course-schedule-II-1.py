from collections import deque

class Solution:
    def findOrder(self, numCourses: int, prerequisites: list[list[int]]) -> list[int]:
        graph = { course: [] for course in range(numCourses)}
        in_degree = { course: 0 for course in range(numCourses)}

        for course, prereq in prerequisites:
            graph[prereq].append(course)
            in_degree[course] += 1

        q = deque([course for course in in_degree if in_degree[course] == 0])
        results = []

        while q:
            prereq = q.popleft()
            results.append(prereq)

            for course in graph[prereq]:
                in_degree[course] -= 1
                if in_degree[course] == 0:
                    q.append(course)


        if len(results) == numCourses:
            return results
        else:
            return []