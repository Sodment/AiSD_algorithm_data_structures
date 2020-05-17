import sys
import time
from _collections import defaultdict
sys.setrecursionlimit(10 ** 9)


## Classes ##

class GraphL:
    def __init__(self, vert):
        self.graph = defaultdict(list)
        self.V = vert
        self.In = [0] * vert

    def AddEdge(self, u, v):
        self.graph[u].append(v)
        self.In[v] += 1

    ## Hamilton Cycle ##

    def IsSafe(self, v, pos, path):
        try:
            if v not in self.graph[path[pos - 1]]:
                return False
        except IndexError:
            pass
        for vertex in path:
            if vertex == v:
                return False
        return True

    def Hamiltonian(self, path, pos):
        if pos == self.V:
            if path[0] in self.graph[path[-1]]:
                return True
            else:
                return False

        for v in range(1, self.V):
            if self.IsSafe(v, pos, path):
                path[pos] = v
                # print(path)
                if self.Hamiltonian(path, pos + 1):
                    return True
                path[pos] = -1
        return False

    def HamiltonCycle(self):
        path = [-1] * self.V
        path[0] = 0
        if not self.Hamiltonian(path, 1):
            print("Graf nie jest grafem Hamiltona")
            return False
        self.PrintSolutionHamilton(path)
        return True

    def PrintSolutionHamilton(self, path):
        print("Cykl Hamiltona w podanym grafie:")
        for v in path:
            print(v, end=" ")
        print(path[0])

    ## Euler Circuit ##

    def DFSUtil(self, v, visited):
        visited[v] = True
        for node in self.graph[v]:
            if visited[node] == False:
                self.DFSUtil(node, visited)

    def GetTranspose(self):
        graphTransponsed = GraphL(self.V)
        for node in range(self.V):
            for child in self.graph[node]:
                graphTransponsed.AddEdge(child, node)
        return graphTransponsed

    def IsStronglyConnected(self):
        visited = [False] * self.V
        v = 0
        for v in range(self.V):
            if len(self.graph[v]) > 0:
                break
        self.DFSUtil(v, visited)

        for i in range(self.V):
            if visited[i] == False:
                return False
        graphTransponsed = self.GetTranspose()
        visited = [False] * self.V
        graphTransponsed.DFSUtil(v, visited)
        for i in range(self.V):
            if visited[i] == False:
                return False
        return True

    def IsEulerianCycle(self):
        if self.IsStronglyConnected() == False:
            return False
        for v in range(self.V):
            if len(self.graph[v]) != self.In[v]:
                return False
        return True

    def Hierholzers(self):
        edgeCount = dict()
        for i in range(len(self.graph)):
            edgeCount[i] = len(self.graph[i])
        currPath = []
        circuit = []
        currPath.append(0)
        currV = 0

        while len(currPath):
            if edgeCount[currV]:
                currPath.append(currV)
                nextV = self.graph[currV][-1]
                edgeCount[currV] -= 1
                self.graph[currV].pop()
                currV = nextV
            else:
                circuit.append(currV)
                currV = currPath[-1]
                currPath.pop()
        print("Cykl Eulera w podanym grafie:")
        for i in range(len(circuit) - 1, -1, -1):
            print(circuit[i], end='')
            if i:
                print(" -> ", end="")
        print()


class GraphM:
    def __init__(self, vert):
        self.graph = [[0 for column in range(vert)] for row in range(vert)]
        self.V = vert
        self.path = []

    def AddEdge(self, i, j):
        self.graph[i][j] = 1
        self.graph[j][i] = 1

    ## Hamilton Cycle ##

    def SafetyCheck(self, v, pos, path):
        if self.graph[path[pos - 1]][v] == 0:
            return False

        for vert in path:
            if vert == v:
                return False
        return True

    def Hamiltonian(self, path, pos):
        if pos == self.V:
            if self.graph[path[pos - 1]][path[0]] == 1:
                return True
            else:
                return False
        for v in range(1, self.V):
            if self.SafetyCheck(v, pos, path) == True:
                path[pos] = v

                if self.Hamiltonian(path, pos + 1) == True:
                    return True
                path[pos] = -1
        return False

    def HamiltonCycle(self):
        path = [-1] * self.V
        path[0] = 0

        if self.Hamiltonian(path, 1) == False:
            print("Graf nie zawiera Cyklu Hamiltona")
            return False
        self.PrintSolutionHamilton(path)
        return True

    def PrintSolutionHamilton(self, path):
        print("Cykl Hamiltona w podanym grafie:")
        for v in path:
            print(v, end=" ")
        print(path[0])

    ## Euler Circuit ##

    def findStartV(self):
        for i in range(self.V):
            deg = 0
            for j in range(self.V):
                if self.graph[i][j] == 1:
                    deg += 1
            if deg % 2 != 0:
                return i
        return 0

    def IsBridge(self, u, v):
        deg = 0
        for i in range(self.V):
            if self.graph[v][i] == 1:
                deg += 1
            if deg > 1:
                return False
        return True

    def EdgeCount(self):
        count = 0
        for i in range(self.V):
            for j in range(self.V):
                if self.graph[i][j] == 1:
                    count += 1
        # print(count)
        return count

    def Fleury(self, start):
        edges = self.EdgeCount()
        for v in range(self.V):
            if self.graph[start][v]:
                if edges <= 2 or not self.IsBridge(start, v):
                    self.path.append(start)
                    self.path.append(v)
                    self.graph[start][v] = self.graph[v][start] = 0
                    edges -= 1
                    self.Fleury(v)

    def PrintSolutionEuler(self):
        self.Fleury(self.findStartV())
        if self.path[0] == self.path[-1]:
            print("Cykl Eulera w podanym grafie:")
            print(self.path[0], end=' -> ')
            for i in range(1, len(self.path) - 1, 2):
                print(self.path[i], end=' -> ')
            print(self.path[-1])

            # ALT PRINT
            # for i in range(2, len(self.path)+1, 2):
            # print(self.path[i-2], "->", self.path[i-1], end = ", ")
            # print()
            # END
        else:
            print("W tym grafie nie ma cyklu Eulera")


def Read_From_Keyboard():
    global V
    global E
    i = 0
    retArray = []
    print("Podawaj polączone wierzcholki")
    while i < E:
        try:
            a, b = input().split()
            a = int(a)
            b = int(b)
        except ValueError:
            print("You fucked up input boi")
            i = 0
        if a == b:
            print("Bez petli wlasnych proszę")
            continue
        retArray.append((a, b))
        i += 1
    return retArray


## Driver Code ##

array = []
V = None
E = None
V_array = []

while True:
    print("Wybierz sposób odczytu: \n1.Z Klawiatury\n2.Z Graph.txt")
    choice = input()
    try:
        choice = int(choice)
    except ValueError:
        print("You fucked up input boi")
        continue
    if choice == 1:
        print("Podaj liczbę wierzchołkow i krawedzi:")
        try:
            V, E = input().split()
            V = int(V)
            E = int(E)
            V_array = Read_From_Keyboard()
            break
        except ValueError:
            print("You fucked up input boy")
            continue
    elif choice == 2:
        a = open("Graph.txt", "r")
        a = a.read()
        a = a.split()
        try:
            a = [int(x) for x in a]
        except ValueError:
            print("You fucked up input boy")
            continue
        V, E = a[0], a[1]
        a = a[2:]
        for i in range(2, 2 * (E + 1), 2):
            x = (a[i - 2], a[i - 1])
            V_array.append(x)
        break
    else:
        print("You fucked up input boi")
        continue

graphSasiedztwa = GraphM(V)
for i in range(E):
    graphSasiedztwa.AddEdge(V_array[i][0], V_array[i][1])
graphNastepnikow = GraphL(V)
for i in range(E):
    graphNastepnikow.AddEdge(V_array[i][0], V_array[i][1])

while True:
    actionChoice = 0
    print("Wybierz co chcesz zrobić:\n1.Znajdz cykl Hamiltona w grafie nieskierowanym\n2.Znajdz Cykl Eulera w grafie nieskierowanym")
    print("3.Znajdz cykl Hamiltona w grafie skierowanym\n4.Znajdz cykl Eulera w grafie skierowanym\n5.Zakoncz program")
    try:
        actionChoice = int(input())
    except ValueError:
        print("You fucked up input boi")
        continue
    if actionChoice == 1:
        startTime1 = time.perf_counter()
        graphSasiedztwa.HamiltonCycle()
        print("Time of running this:", time.perf_counter() - startTime1, "sec")
    elif actionChoice == 2:
        startTime2 = time.perf_counter()
        graphSasiedztwa.PrintSolutionEuler()
        print("Time of running this:", time.perf_counter() - startTime2, "sec")
    elif actionChoice == 3:
        startTime3 = time.perf_counter()
        graphNastepnikow.HamiltonCycle()
        print("Time of running this:", time.perf_counter() - startTime3, "sec")
    elif actionChoice == 4:
        startTime4 = time.perf_counter()
        if graphNastepnikow.IsEulerianCycle():
            graphNastepnikow.Hierholzers()
        else:
            print("To nie jest graf Eulera")
        print("Time of running this:", time.perf_counter() - startTime4, "sec")
    elif actionChoice == 5:
        break

# HAMILTON TEST ALSO EULER LOL
# 8 11 0 1 0 5 0 7 0 4 1 2 2 4 4 5 4 6 5 3 3 6 7 5
# EULER TEST
# 8 10 0 1 0 2 1 2 2 4 2 3 3 5 3 7 3 6 4 6 5 7
# HAMILTON DIRECT TEST
# 7 9 0 1 0 4 1 2 2 0 3 5 3 6 4 3 5 1 6 5
# EULER DIRECTED
# 7 10 0 1 0 6 1 2 2 0 2 3 3 4 4 2 4 5 5 0 6 4
