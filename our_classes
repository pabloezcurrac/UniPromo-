from collections import deque

class Node():
  def __init__(self,name, rating):
    self.name = name
    self.rating = rating
    self.adjacencylist = []
    self.visited = False

  def bfs(self):
    search_queue = deque()
    search_queue.append(self)
    self.visited = True
    five = []
    four = []
    three = []
    two = []
    one = []
    
    while search_queue:
      
      actualNode = search_queue.popleft()
      
      for n in actualNode.adjacencylist:
        if not n.visited:
          if n.rating == 5:
            five.append(n.name)
          search_queue.append(n)
          if n.rating == 4:
            four.append(n.name)
          search_queue.append(n)
          if n.rating == 3:
            three.append(n.name)
          search_queue.append(n)
          if n.rating == 2:
            two.append(n.name)
          search_queue.append(n)
          if n.rating == 1:
            one.append(n.name)
          search_queue.append(n)
          n.visited = True
    return five, four, three, two, one
