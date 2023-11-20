import networkx as nx
import matplotlib.pyplot as plt
class RedSocial:
    def __init__(self):
        self.usuarios = {}
        self.grafo = nx.Graph()
    
    def registrar_usuario(self, nombre, edad):
        # Implementa la creación de un nuevo nodo (usuario) en el grafo
        self.usuarios[nombre] = edad
        self.grafo.add_node(nombre)
    
    def agregar_amigo(self, usuario1, usuario2):
        # Implementa la creación de una arista entre dos usuarios en el grafo
        self.grafo.add_edge(usuario1, usuario2)
    
    def visualizar_red(self):
        nx.draw(self.grafo, with_labels=True)
        plt.show()
    
    def calcular_grado_separacion(self, usuario1, usuario2):
        # Verificar si los usuarios existen en la red social
        if usuario1 not in self.usuarios or usuario2 not in self.usuarios:
            return -1
        
        # Inicializar la cola y el diccionario de visitados
        cola = [(usuario1, 0)]
        visitados = {usuario1}
        
        while cola:
            usuario, grado = cola.pop(0)
            
            # Verificar si se ha encontrado el usuario2
            if usuario == usuario2:
                return grado
            
            # Obtener los amigos del usuario actual
            amigos = self.grafo.neighbors(usuario)
            
            # Agregar los amigos a la cola si no han sido visitados
            for amigo in amigos:
                if amigo not in visitados:
                    cola.append((amigo, grado + 1))
                    visitados.add(amigo)
        
        # Si no se encontró un camino entre los usuarios, retornar -1
        return -1
    
    def eliminar_amigo(self, usuario1, usuario2):
        # Verificar si los usuarios existen en la red social
        if usuario1 not in self.usuarios or usuario2 not in self.usuarios:
            return
        
        # Verificar si existe una arista entre los usuarios
        if self.grafo.has_edge(usuario1, usuario2):
            self.grafo.remove_edge(usuario1, usuario2)
    
# Ejemplo de uso:
red_social = RedSocial()
red_social.registrar_usuario("Usuario1", 25)
red_social.registrar_usuario("Usuario2", 30)
red_social.agregar_amigo("Usuario1", "Usuario2")
red_social.visualizar_red()
grado_separacion = red_social.calcular_grado_separacion("Usuario1", "Usuario2")
print(f"Grado de separación: {grado_separacion}")
red_social.eliminar_amigo("Usuario1", "Usuario2")
red_social.visualizar_red()
