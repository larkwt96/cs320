import sys
import queue

def read(fnm,db):
  """  
  read file fnm into dictionary
  each line has a nodeName followed by its adjacent nodeNames
  """
  file = open(fnm)
  graph = {} #dictionary
  for line in file:
    l = line.strip().split(" ")
    if db: print("l:",l,"len(l):",len(l))
    # remove empty lines
    if l==['']:continue
    # dict: key: nodeName  value: (color, adjList of names)
    graph[l[0]]= ('white',l[1:]) 
  return graph

def dump(graph):
  print("dumping graph: nodeName (color, [adj list]) ")
  for node in graph:
    print(node, graph[node])

def getGrey(tup):
  """Makes the tuple of the form (str,arr) to ("grey",arr)"""
  return ('grey', tup[1])

def getBlack(tup):
  """Makes the tuple of the form (str,arr) to ("black",arr)"""
  return ('black', tup[1])

def bfs(graph,list):
  """  
  breadth first search graph from root in list
  return list: array of tuples [(nodename, distance from root), ...]
  """
  toProc = queue.Queue()
  for kid in graph[list[0][0]][1]:
    toProc.put((kid, 1))
  while not toProc.empty():
    node, dist = toProc.get()
    if graph[node][0] == 'black':
        continue
    graph[node] = getBlack(graph[node])
    list.append((node, dist))
    for kid in graph[node][1]:
      if graph[kid][0] == 'white':
        toProc.put((kid, dist+1))
  return list

def white(graph) :
  """
   paint all graph nodes white
  """
  for node in graph :
    gr[node] = ('white',gr[node][1])

def dfs(r):
  """
  depth first left to right search dd from r for cycles if cycle found (grey
  node encountered) print( "cycle in", nodename)
  """
  stack = []
  stack.append(r)
  while stack: # non-empty
    node = stack[-1] # peek
    gr[node] = getGrey(gr[node]) # mark grey
    numkids = len(gr[node][1])
    for kid in gr[node][1]:
        color = gr[kid][0]
        if color == 'grey': # cycle
            print("cycle in", node)
            numkids -= 1
        elif color == 'black': # not cycle
            numkids -= 1
        else:
            stack.append(kid)
            break
    if numkids == 0: # all kids grey or black, or no kids
        gr[node] = getBlack(gr[node]) # mark black
        stack.pop()

if __name__ == "__main__":
  # db: debug flag
  db = len(sys.argv)>3
  gr = read(sys.argv[1],db)
  root = sys.argv[2]
  if db: dump(gr)
  print("root key:", root)
  # don't need grey for bfs
  gr[root] = ('black',gr[root][1])
  q = bfs(gr,[(root,0)])
  print("BFS")
  print(q)
  if db: dump(gr)
  white(gr)
  if db: dump(gr)
  print("DFS");
  dfs(root)
  if db: dump(gr)
