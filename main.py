class Graph:

    def __init__(self, vertex):
        self.V = vertex
        self.graph = [[0 for i in range(vertex)] for i in range(vertex)]
        self.connections = {}

    def colorNodes(self):
        colorMap = {}
        # проверяем вершины по убыванию количества соседей
        for node in sorted(self.connections, key=lambda x: len(self.connections[x]), reverse=True):
            neighborСolors = set(colorMap.get(neigh) for neigh in self.connections[node]) # находим цвета соседей
            colorMap[node] = [color for color in range(len(self.connections)) if color not in neighborСolors][0]
            # берем все возможные цвета убираем из них те которые у соседей и берем первый из оставшихся
        return colorMap



def graphInit(g, gm):
    for i in range(g.V):
        iConnected = []
        for j in range(g.V):
            if gm[i][j] != 0:
                iConnected.append(j)
                g.graph[i][j] = 1
                g.graph[j][i] = 1
        g.connections.update({i: iConnected})
    return g


gMat = [
    [0, 1, 0, 0, 0, 0, 1],
    [1, 0, 1, 0, 0, 1, 1],
    [0, 1, 0, 1, 1, 1, 0],
    [0, 0, 1, 0, 1, 0, 0],
    [0, 0, 1, 1, 0, 1, 1],
    [0, 1, 1, 0, 1, 0, 1],
    [1, 1, 0, 0, 1, 1, 0],
]
gMat2 = [
    [0, 0, 0, 0, 0, 1, 1, 0, 0, 0],
    [0, 0, 0, 0, 1, 0, 0, 1, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 1, 1, 0],
    [0, 0, 0, 0, 0, 1, 0, 1, 1, 1],
    [0, 1, 0, 0, 0, 1, 1, 0, 1, 0],
    [1, 0, 0, 1, 1, 0, 1, 0, 0, 0],
    [1, 0, 0, 0, 1, 1, 0, 1, 0, 0],
    [0, 1, 1, 1, 0, 0, 1, 0, 0, 0],
    [0, 0, 1, 1, 1, 0, 0, 0, 0, 1],
    [0, 0, 0, 1, 0, 0, 0, 0, 1, 0]
]
g = Graph(10)
g = graphInit(g, gMat2)
print(g.colorNodes())

