# смотрим сразу все Edge между вершинами и это делаем количестов раз
# равное количеству вершинам, сложность алгоритма O(V * E)

import sys # for sys.maxsize

class Node(object): # наследование от object???

  def __init__(self, name):
    self.name = name
    self.predecessor = None
    self.visited = False
    self.minDistance = sys.maxsize
    self.adjacenciesList = []

class Edge(object):

  def __init__(self, weight, startVertex, targetVertex):
    self.weight = weight
    self.startVertex = startVertex
    self.targetVertex = targetVertex


class BellmanFord(object):

  HAS_CYCLE = False # есть отрицательные циклы или нет в графе

  def calculateShortestPath(self, vertexList, edgeList, startVertex):
    startVertex.minDistance = 0 # стартовая вершина

    # перебираем все возможные вершины
    for i in range(len(vertexList) - 1):
      # перебираем все возможные грани
      for edge in range(len(edgeList)):

        start = edge.startVertex
        target = edge.targetVertex

        if start.minDistance + edge.weight < target.minDistance:
          # если новый путь короче, чем старый предыдущий путь
          target.predecessor = start
          target.minDistance = start.minDistance + edge.weight

    # запускаем еще одну дополнительную проверку на негативные циклы
    # получается это подставная проверка, мы просто еще раз запускаем
    # цикл проверок и если есть меньше путь => есть негативный цикл
    # так как мы уже прошлись по всем возможным вариантам и ничего
    # лучше мы не должны найти!
    for edge in egeList:
      if self.hasCycle(edge):
        print('Negative cycle detected...')
        BellmanFord.HAS_CYCLE = True
        return

  # проверяем еще раз, если лучше нашли путь => есть отрицательные циклы
  def hasCycle(self, edge):
    if (edge.startVertex.minDistance + edge.weight)
      < edge.targetVertex.minDistance:
      return True
    else:
      return False

  def getShortestPathTo(self, targetVertex):
    if not BellmanFord.HAS_CYCLE:
      print('Shortest path exist')

      node = targetVertex

      while node:
        node = node.predecessor
        print(node.name)

    else:
      print('We have negative cycle!!! sooo we cant get shortest path')
