#
# @lc app=leetcode.cn id=207 lang=python3
#
# [207] 课程表
#

# @lc code=start
from typing import List


class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        indegrees = [0 for _ in range(numCourses)]
        adj = [[] for _ in range(numCourses)]

        for cur, pre in prerequisites:
            indegrees[cur] += 1
            adj[pre].append(cur)

        queue = []

        for course, indegree in enumerate(indegrees):
            if indegree == 0:
                queue.append(course)

        while queue:
            cur_course = queue.pop(0)
            numCourses -= 1
            # 这个课后面的课可以学了
            for each in adj[cur_course]:
                indegrees[each] -= 1
                if indegrees[each] == 0:
                    queue.append(each)
        return numCourses <= 0


# @lc code=end
