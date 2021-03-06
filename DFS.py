from enum import Enum
import Graph

class Color(Enum):
    WHITE = 1
    GRAY = 2
    BLACK = 3


def dfs(G):
    color = []
    pi = []
    d = []
    f = []

    time = 0
    for i in range(G.node_num):
        color.append(Color.WHITE)
        pi.append(None)
        d.append(0)
        f.append(0)

    for i in range(G.node_num):
        if color[i] == Color.WHITE:
            color, pi, d, f, time = dfsVisit(G, color, pi, d, f, time, i)

    for i in range(G.node_num):
        print(i+1, d[i], f[i])

    # Topological
    l = [(i+1, f[i]) for i in range(G.node_num)]
    print(l)
    l = sorted(l, key=lambda x : x[1])
    print(l)
    for i in range(G.node_num):
        print(l[i][0], end='->')
    print()


def dfsVisit(G, color, pi, d, f, time, u):
    color[u] = Color.GRAY
    time += 1
    d[u] = time
    u_edge = G.getVertice(u+1).edges
    while(u_edge):
        cur_edge = u_edge
        if color[cur_edge.v-1] == Color.WHITE:
            pi[cur_edge.v-1] = u
            color, pi, d, f, time = dfsVisit(G, color, pi, d, f, time, cur_edge.v-1)
        u_edge = u_edge.next
    color[u] = Color.BLACK
    time += 1
    f[u] = time
    return color, pi, d, f, time

def main():
    # 结果不对，因为参数是传值形式而不是引用形式，待修改
    # 用了return返回需要更新的数据
    # 也可以用class
    G = Graph.Graph()
    # edges = [(1,2), (3,6), (4,2), (5,4), (6,6), (1,4), (2,5), (3,5), ]
    edges = [(1,2), (2,3), (2,5), (2,6), (3,4), (3,7), (4,3), (4,8), (5,1), (5,6), (6,7), (7,8), (8,8)]
    for i in range(len(edges)):
        G.insertEdge(Graph.Edge(edges[i][0], edges[i][1]))
    dfs(G)

main()