import sys
from collections import defaultdict

class Node():
    def __init__(self, id, dist):
        self.id = id
        self.dist = dist

class MyHeap():
    def __init__(self):
        self.data = []
        self.size = 0
        self.pos = []

    def inHeap(self, u_id):
        for id in range(self.size):
            if u_id == self.data[id].id:
                return True
        return False

    def empty(self):
        return self.size == 0

    def swapHeapNode(self, a, b):
        self.data[a], self.data[b] = self.data[b], self.data[a]

    def minHeapify(self, idx):
        smallest = idx
        left = smallest*2 + 1
        right = smallest*2 + 2

        if left < self.size and self.data[left].dist < self.data[smallest].dist:
            smallest = left
        if right < self.size and self.data[right].dist < self.data[smallest].dist:
            smallest = right

        if smallest != idx:
            # update position
            self.pos[self.data[idx].id] = smallest
            self.pos[self.data[smallest].id] = idx
            self.swapHeapNode(idx, smallest)
            self.minHeapify(smallest)

    def decreaseKey(self, u_id, val):
        idx = self.pos[u_id]
        if(val >= self.data[idx].dist):
            print(val, "is not smaller than the node's distance")
            return

        self.data[idx].dist = val

        cur_id = idx
        while(cur_id > 0):
            pi = (cur_id-1) // 2
            if self.data[pi].dist > self.data[cur_id].dist:
                self.pos[self.data[pi].id] = cur_id
                self.pos[self.data[cur_id].id] = pi
                self.swapHeapNode(pi, cur_id)
                cur_id = pi
            else:
                break

    def insertHeapNode(self, u):
        self.size += 1
        self.pos.append(u.id)
        self.data.append(u)
        self.decreaseKey(u.id, u.dist)

    def extractMin(self):
        if self.size > 0:
            self.size -= 1
            self.pos[self.data[0].id] = self.size
            self.pos[self.data[self.size].id] = 0
            self.swapHeapNode(0, self.size)
            self.minHeapify(0)
            return self.data[self.size]

    def print(self):
        for it in self.data:
            print(it.id, it.dist)

class Graph():
    def __init__(self, node_num):
        self.node_num = node_num
        self.graph = defaultdict(list)

    def addEdge(self, src, dst, cost):
        self.graph[src].insert(0, Node(dst, cost))
        self.graph[dst].insert(0, Node(src, cost))

    def print(self):
        for i in range(self.node_num):
            for node in self.graph[i]:
                print(i, node.id, node.dist)

    def primMST(self, s):
        pi = []
        key = []
        Q = MyHeap()

        for i in range(self.node_num):
            pi.append(None)
            key.append(sys.maxsize)
            Q.insertHeapNode(Node(i, sys.maxsize))
        key[s] = 0
        pi[s] = -1
        Q.decreaseKey(s, 0)

        while(not Q.empty()):
            u = Q.extractMin()
            for edge in self.graph[u.id]:
                if Q.inHeap(edge.id) and edge.dist < key[edge.id]:
                    pi[edge.id] = u.id
                    key[edge.id] = edge.dist
                    Q.decreaseKey(edge.id, edge.dist)

        for i in range(self.node_num):
            print(i, pi[i])

def main():
    graph = Graph(9)
    graph.addEdge(0, 1, 4)
    graph.addEdge(0, 7, 8)
    graph.addEdge(1, 2, 8)
    graph.addEdge(1, 7, 11)
    graph.addEdge(2, 3, 7)
    graph.addEdge(2, 8, 2)
    graph.addEdge(2, 5, 4)
    graph.addEdge(3, 4, 9)
    graph.addEdge(3, 5, 14)
    graph.addEdge(4, 5, 10)
    graph.addEdge(5, 6, 2)
    graph.addEdge(6, 7, 1)
    graph.addEdge(6, 8, 6)
    graph.addEdge(7, 8, 7)
    graph.print()
    graph.primMST(0)

main()