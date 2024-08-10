class Solution:
    def canFinish(self, numCourses: int, prerequisites: list[list[int]]) -> bool:
        graph = { i: [] for i in range(numCourses) }
        
        # each course has edges to its prerequisites
        for course, pre in prerequisites:
            graph[course].append(pre)

        visited, curr_path = set(), set()

        def dfs_has_cycle(crs):
            if crs in curr_path: #  cycle detected
                return True
            if crs in visited: #  course has been processed
                return False

            visited.add(crs)
            curr_path.add(crs)

            for pre in graph[crs]:
                if dfs_has_cycle(pre):
                    return True

            # once finished processing crs, remove from the current path
            curr_path.remove(crs)

            return False
            

        for course in range(numCourses):
            if course not in visited:
                if dfs_has_cycle(course):
                    return False

        return True

        