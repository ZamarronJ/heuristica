class Nodo:
    def __init__(self, datos, hijos=None):
        self.datos = datos
        self.hijos = hijos if hijos is not None else []
        self.padre = None
        self.coste = None

    def set_hijos(self, hijos):
        self.hijos = hijos
        for h in self.hijos:
            h.padre = self

    def get_hijos(self):
        return self.hijos

    def get_padre(self):
        return self.padre

    def set_padre(self, padre):
        self.padre = padre

    def set_datos(self, datos):
        self.datos = datos

    def get_datos(self):
        return self.datos

    def set_costo(self, coste):
        self.coste = coste

    def get_costo(self):
        return self.coste

    def igual(self, nodo):
        return self.get_datos() == nodo.get_datos()

    def en_lista(self, lista_nodos):
        for n in lista_nodos:
            if self.igual(n):
                return True
        return False

    def __str__(self):
        return str(self.get_datos())
