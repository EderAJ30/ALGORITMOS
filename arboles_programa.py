class Nodo:
    def __init__(self, datos, hijos=None):
        self.datos = datos
        self.hijos = hijos
        self.padre = None

    def set_hijos(self, hijos):
        self.hijos = hijos
        if self.hijos is not None:
            for hij in self.hijos:
                hij.padre = self

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

    def igual(self, nodo):
        return self.get_datos() == nodo.get_datos()

    def en_lista(self, lista_nodos):
        return any(self.igual(n) for n in lista_nodos)

    def __str__(self):
        return str(self.get_datos())

def busqueda_amplitud(estado_inicial, solucion):
    solucionado = False
    nodos_visitados = []
    nodos_pendientes = []
    movimientos = 0  
    nodo_inicial = Nodo(estado_inicial)
    nodos_pendientes.append(nodo_inicial)

    while not solucionado and len(nodos_pendientes) != 0:
        nodo = nodos_pendientes.pop(0)
        nodos_visitados.append(nodo)
        movimientos += 1  

        print(f"Iteración {movimientos}: {nodo.get_datos()}")  

        if nodo.get_datos() == solucion:
            solucionado = True
            return nodo
        else:
            dato_nodo = nodo.get_datos()

            for i in range(len(dato_nodo) - 1):
                hijo = Nodo(dato_nodo[:])  
                hijo.datos[i], hijo.datos[i + 1] = hijo.datos[i + 1], hijo.datos[i]  
                if not hijo.en_lista(nodos_pendientes) and not hijo.en_lista(nodos_visitados):
                    nodos_pendientes.append(hijo)

            nodo.set_hijos(nodos_pendientes)  

if __name__ == "__main__":
    estado_inicial = [7, 2, 1, 4, 5, 6, 3, 8]  
    solucion = [1, 2, 3, 4, 5, 6, 7, 8]  
    nodo_solucion = busqueda_amplitud(estado_inicial, solucion)

    resultado = []
    nodo = nodo_solucion
    while nodo.get_padre() is not None:
        resultado.append(nodo.get_datos())
        nodo = nodo.get_padre()
    resultado.append(estado_inicial)
    resultado.reverse()
    print("Solución encontrada en los siguientes movimientos:")
    for r in resultado:
        print(r)
    print(f"Total movimientos: {len(resultado)}")
