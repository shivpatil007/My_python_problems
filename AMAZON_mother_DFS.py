from collections import defaultdict

graph = defaultdict(list)
VERTEX_NUMBER = 5


def DFSUtil(v, visited):
    visited[v] = True
    for i in graph[v]:
        if visited[i] == False:
            DFSUtil(i, visited)


def mother_vertex():
    visited = [False] * 5
    for i in range(VERTEX_NUMBER):
        if visited[i] == False:
            DFSUtil(i, visited)
            v = i
