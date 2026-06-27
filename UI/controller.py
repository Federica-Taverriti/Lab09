import flet as ft


class Controller:
    def __init__(self, view, model):
        # the view, with the graphical elements of the UI
        self._view = view
        # the model, which implements the logic of the program and holds the data
        self._model = model

    def handle_analizza(self, e):
        distTxt = self._view.txt_dist.value
        if distTxt is None or distTxt == "":
            self._view.txt_result.controls.clear()
            self._view.txt_result.controls.append(
                ft.Text("Inserire la distanza minima.", color="red"))
            self._view.update_page()
            return

        try:
            dist = int(distTxt)
        except ValueError:
            self._view.txt_result.controls.clear()
            self._view.txt_result.controls.append(
                ft.Text("Inserire un valore intero per la distanza minima.", color="orange"))
            self._view.update_page()
            return

        self._model.buildGraph(dist)
        numNodes, numEdges = self._model.getGraphDetails()
        edges = self._model.getEdges()

        self._view.txt_result.controls.clear()
        self._view.txt_result.controls.append(
            ft.Text("Grafo creato correttamente!", color="green"))

        self._view.txt_result.controls.append(
            ft.Text(f"Il grafo è composto da {numNodes} vertici."))
        self._view.txt_result.controls.append(
            ft.Text(f"Il grafo è composto da {numEdges} archi."))

        for e in edges:
            self._view.txt_result.controls.append(
                ft.Text(f"{e[0]} - {e[1]} :  {e[2]['weight']}"))

        self._view.update_page()
