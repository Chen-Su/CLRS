import Graph
import queue

def prim(G, r):
    """
    minimum spanning tree by prim algorithm
    :param G: Graph
    :param r: MST root node
    :return:
    """
    pi = []
    nodes = []
    inQ = []
    Q = queue.Queue()
    for i in range(G.node_num):
        nodes.append([float('inf'), i+1])
        pi.append(None)
        inQ.append(True)

    nodes[r-1][0] = 0
    for i in range(G.node_num):
        Q.put(nodes[i])
    while(not Q.empty()):
        cur_node = Q.get()
        u = cur_node[1]
        inQ[u-1] = False # u 出队
        u_edge = G.getVertice(u).edges
        while(u_edge):
            v = u_edge.v
            cost = u_edge.cost
            ...



def main():
    d = {'a':1,'gsdf':4,'b':2,'asdf':3,}
    l = []
    for key, value in d.items():
        l.append((value,key))
    l = sorted(l,key=lambda x : x[1])
    print(l)
    q = queue.PriorityQueue()
    for x in l:
        q.put(x)
    print(q.get())
    print(q.get())
    print(q.get())
    print(q.get())

main()