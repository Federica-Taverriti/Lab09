import networkx as nx
from database.DAO import DAO


class Model:
    def __init__(self):
        self._graph = nx.Graph()
        self._nodes = DAO.getAllNodes()
        self._idMapAirports = {}  # mappa tra id aereoporti e aeroporti
        for a in self._nodes:
            self._idMapAirports[a.ID] = a


    def buildGraph(self, dist):
        self._graph.clear()
        #self._graph.add_nodes_from(self._nodes)
        #così ho tutti gli aeroporti, se non lo metto ho i nodi connessi grazie a addEdges() che fa in automatico
        self.addEdges(dist)


    def addEdges(self, dist):
        allRotte = DAO.getAllEdges(self._idMapAirports)

        for r in allRotte:
            if r.peso > dist:
                self._graph.add_edge(r.aeroportoP, r.aeroportoA, weight=r.peso)

    def getEdges(self):
        return self._graph.edges(data=True)

    def getGraphDetails(self):
        return len(self._graph.nodes), len(self._graph.edges)