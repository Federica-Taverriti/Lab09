from model.model import Model

myModel = Model()

myModel.buildGraph(500)
nNodes, nEdges = myModel.getGraphDetails()
print(f"Num nodes: {nNodes}, num edges: {nEdges}")

edges = myModel.getEdges()
for e in edges:
    print(e)