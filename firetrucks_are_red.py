"""
:Problem: Firetrucks are Red
:Authors: Stuart Harley, Hayden Klein, Brendan Ecker
"""
class Union:
    def __init__(self, n):
        self.parent = [-1] * n

    def find(self, x):
        if self.parent[x] < 0:
            return x
        self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def connect(self, a, b):
        ra = self.find(a)
        rb = self.find(b)
        if ra == rb:
            return False
        if self.parent[ra] > self.parent[rb]:
            self.parent[rb] += self.parent[ra]
            self.parent[ra] = rb
        else:
            self.parent[ra] += self.parent[rb]
            self.parent[rb] = ra
        return True


def kruskal(vertices, edges):
    uf = Union(vertices)
    span_tree = []
    while edges and len(span_tree) < vertices - 1:
        v, u, w = edges.pop()
        if not uf.connect(v, u):
            continue
        span_tree.append((v + 1, u + 1, w))
    if len(span_tree) != vertices - 1:
        print('Impossible')
    else:
        for edge in span_tree:
            print(*edge)


def edges(vertices):
    edg = []
    ntv = {}
    for v in range(vertices):
        _, *numbers = map(int, input().split())
        for w in numbers:
            if w not in ntv:
                ntv[w] = v
            else:
                edg.append((ntv[w], v, w))
    return edg


def main():
    vertices = int(input())
    edg = edges(vertices)
    kruskal(vertices, edg)


main()