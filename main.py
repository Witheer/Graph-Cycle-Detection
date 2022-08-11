def has_cycle(graph):
  status = {}

  # initialize them as new
  for vertex in graph:
    status[vertex] = 'NEW'

  for vertex in graph:
    # check if each vertex not visited has a cycle
    if status[vertex] == 'NEW':
      if has_cycle_dfs(vertex, graph, status):
        return True

  return False


def has_cycle_dfs(v, graph, status):
  status[v] = 'SEEN'

  for neigh in graph.get(v):
    if status[neigh] == 'SEEN':
      return True

    elif status[neigh] == 'NEW':
      # don't return right away for the false case
      if has_cycle_dfs(neigh, graph, status):
        return True
        
  status[v] = 'VISITED'
  return False

# -----------------------------------
# Test Cases
graph = {1: [2, 4], 2: [3], 3: [], 4: [2, 5, 6], 5: [6], 6: []}

graph_with_cycle = {'A': ['B'], 'B': ['C'], 'C': ['D'], 'D': ['A']}

# Should print False
print(has_cycle(graph))
# Should print True
print(has_cycle(graph_with_cycle))
