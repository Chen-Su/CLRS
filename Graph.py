class Edge:
    def __init__(self, u, v, cost=1):
        self.u = u
        self.v = v
        self.cost = cost
        self.next = None

    def print(self):
        print((self.u, self.v, self.cost), end=' ')

class Vertice:
    def __init__(self, u):
        self.u = u
        self.edges = None

    def print(self):
        print(self.u, end=' : ')
        if(self.edges == None):
            print(None)
        else:
            tmp = self.edges
            while(tmp):
                tmp.print()
                tmp = tmp.next

class Graph:
    def __init__(self, node_num = 0):
        self.node_num = node_num
        self.vertices = [Vertice(i) for i in range(node_num)]

    def insertEdge(self, e):
        if(max(e.u, e.v) > self.node_num):
            tmp = self.node_num
            self.node_num = max(e.u, e.v)
            for i in range(self.node_num - tmp):
                self.vertices.append(Vertice(i+tmp))

        if(self.vertices[e.u-1].edges == None):
            self.vertices[e.u-1].edges = e
        else:
            # insert edge e
            tmp = self.vertices[e.u-1].edges.next
            self.vertices[e.u-1].edges.next = e
            e.next = tmp

    def getVertice(self, node_num):
        return self.vertices[node_num-1]

    def print(self):
        for i in range(self.node_num):
            self.vertices[i].print()
            print()


def main():
    edges = [(1,2), (3,6), (4,2), (5,4), (6,6), (1,4), (2,5), (3,5), ]
    g = Graph()
    for i in range(len(edges)):
        g.insertEdge(Edge(edges[i][0], edges[i][1]))

    g.print()

main()

