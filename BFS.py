import Graph
import queue
from enum import Enum

class Color(Enum):
    WHITE = 1
    GRAY = 2
    BLACK = 3

def bfs(G, s):
    """
    :param G: Graph G
    :param s: source node s
    实际编程时，一般情况下只需要WHITE(未访问过)和GRAY(已访问过(在队列中或者已经出队))两种颜色状态即可，黑色是不需要的
    :return:
    """
    color = []
    d = []
    pi = []
    for i in range(G.node_num):
        color.append(Color.WHITE)
        d.append(float('inf'))     # float('inf') means +inf
        pi.append(None)

    color[s-1] = Color.GRAY
    d[s-1] = 0
    pi[s-1] = None
    Q = queue.Queue()
    Q.put(s)
    while(not Q.empty()):
        u = Q.get()
        u_edges = G.getVertice(u).edges
        while(u_edges):
            cur_edge = u_edges
            if(color[cur_edge.v-1] == Color.WHITE):
                color[cur_edge.v-1] = Color.GRAY
                d[cur_edge.v-1] = d[u-1] + 1
                pi[cur_edge.v-1] = u
                Q.put(cur_edge.v)
            u_edges = u_edges.next
        color[u-1] = Color.BLACK
    for i in range(G.node_num):
        print(i+1, d[i])

def main():
    G = Graph.Graph()
    edges = [(1,2), (3,6), (4,2), (5,4), (6,6), (1,4), (2,5), (3,5), ]
    for i in range(len(edges)):
        G.insertEdge(Graph.Edge(edges[i][0], edges[i][1]))
    bfs(G, 1)

main()