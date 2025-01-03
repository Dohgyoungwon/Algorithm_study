# 방법의 수를 못 구하겠음.

import sys
input = sys.stdin.readline

from collections import deque

def my_bfs(start, end):
    queue.append(start)
    visited[start] = 0

    while queue:
        current = queue.popleft()

        if current == end:
            return line[current]
        
        # [current * 2, current - 1, current + 1] 이 순서로 안하면 틀림
        for next in [current * 2, current - 1, current + 1]:

            if next < 0 or next >= 200001 or visited[next] != -1:
                continue

            queue.append(next)

            line[next] = line[current] + 1
            visited[next] = visited[current] + 1


N, K = map(int, input().split())
visited = [-1] * 200001
line = [0] * 200001
queue = deque()

time = my_bfs(N, K)
print(time)

