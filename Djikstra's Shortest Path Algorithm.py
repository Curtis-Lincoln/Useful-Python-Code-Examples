#Djikstra's Shortest Path Alogrithm
#Intractable Problem - Problems for which there exist no efficient algorithms to solve them 
#Rules:
#1. We need the map represented as a graph
#2. The graph should be weighted  - the weights indicate a meaurement we're interested in minimising (distance, time, costs etc...)
#3. Each vertex on the graph should be labelled to show what the current shortest total distance is to this vertex
#   (infinity is a good starting point), and the last vertex that was visited on order to calculate this distnace (to begin with this would be blank.)
#4. Identify the starting vertex of our journey
#Djikstra's algorithm will calculate the shortest distance from the strating vertex to every other vetex on the graph.

#map = [list of vertices and their weights]
#for each vertex in the map do
#   for each connected_vertex to vertex do
#       if connected_weight + shortest_distance to vertex < total_shortest_distance then
#           replace total_shortest_distance with the shortest_distance + connection_weight
#           replace last_visited_vertex with vertex


my_map = {
    'a': {'b':4, 'c':7},
    'b': {'a':4, 'd':11},
    'c': {'a':7, 'd':2},
    'd': {'b':11, 'c':2, 'e':6, 'f':12},
    'e': {'d':6, 'g':8},
    'f': {'d':12, 'g':9},
    'g': {'e':8, 'f':12},
    }
