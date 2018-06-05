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