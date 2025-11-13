'''
CSC263 Winter 2025
Problem Set 4 Starter Code
University of Toronto Mississauga
'''


# Do NOT add any "import" statements
# Do NOT use Python dictionaries


# essentially copied from CLRs & class notes
class Graph:
    def __init__(self, vertices):

        n = len(vertices)
        self.G = []
        for i in range(n):
            self.G.append([])

        self.color = ['white'] * n
        self.s = [0] * n
        self.f = [0] * n
        self.pi = [None] * n
        self.time = 0

        self.valid = True

    def add_edge(self, u, v):
        self.G[u].append(v)

    def dfs_visit(self, u):
        self.color[u] = 'grey'
        self.time += 1
        self.s[u] = self.time

        for v in self.G[u]:
            if self.color[v] == 'white':
                self.pi[v] = u
                self.dfs_visit(v)

            # CYCLE FOUND
            elif self.color[v] == 'grey':
                self.valid = False

        self.color[u] = 'black'
        self.time += 1
        self.f[u] = self.time


def can_visit_all_cities(numCities, dependencies):
    '''
      Pre:  numCities is the number of cities to be visited
            dependencies is a list of 2-tuples representing (city1,city2) with city1 can only be visited after city2
      Post: return whether visiting all cities is possible or not
      '''
    # topological sort stuff. check if cycle -> if not then do the topological sort? read clr
    vertices = []
    for city1, city2 in dependencies:
        if city1 not in vertices:
            vertices.append(city1)
        if city2 not in vertices:
            vertices.append(city2)

    graph = Graph(vertices)
    for city1, city2 in dependencies:
        u = vertices.index(city2)
        v = vertices.index(city1)
        graph.add_edge(u, v)

    # print(graph.G)
    # print(vertices)

    for u in range(len(vertices)):
        if graph.color[u] == 'white':
            graph.dfs_visit(u)

    if graph.valid:
        return 1
    else:
        return 0


if __name__ == '__main__':
    # some small test cases
    # Case 1
    numCities1: int = 25
    dependencies1 = [('reykjavik', 'stjohns'), ('limerick', 'dublin'), ('london', 'dublin'), ('brighton', 'london'),
                     ('heidelberg', 'frankfurt'), ('frankfurt', 'london'), ('frankfurt', 'dublin'),
                     ('batam', 'singapore'), ('newcastle', 'sydney'), ('sandiego', 'honolulu')]

    # Case 2
    numCities2: int = 10
    dependencies2 = [('paris', 'madrid'), ('madrid', 'lisbon'), ('lisbon', 'paris')]

    # Case 3
    numCities3: int = 0
    dependencies3 = []

    # Case 4
    numCities4 = 5
    dependencies4 = [('a', 'b'), ('b', 'c'), ('c', 'd'), ('d', 'e')]

    # Case 5
    numCities5 = 7
    dependencies5 = [('a', 'b'), ('b', 'c'), ('c', 'a'), ('x', 'y')]

    # Case 6
    numCities6 = 10
    dependencies6 = [('a', 'b'), ('b', 'c'), ('c', 'd'), ('e', 'f'), ('f', 'g'), ('g', 'h')]

    assert 1 == can_visit_all_cities(numCities1, dependencies1)
    assert 0 == can_visit_all_cities(numCities2, dependencies2)
    assert 1 == can_visit_all_cities(numCities3, dependencies3)
    assert 1 == can_visit_all_cities(numCities4, dependencies4)
    assert 0 == can_visit_all_cities(numCities5, dependencies5)
    assert 1 == can_visit_all_cities(numCities6, dependencies6)
