from collections import deque
from datetime import date


class Pila:
    def __init__(self):
        self.items = []
    
    def esta_vacia(self):
        return len(self.items) == 0
    
    def apilar(self, item):
        self.items.append(item)
    
    def desapilar(self):
        if not self.esta_vacia():
            return self.items.pop()
        return None
    
    def ver_tope(self):
        if not self.esta_vacia():
            return self.items[-1]
        return None
    
    def tamano(self):
        return len(self.items)
    
    def __str__(self):
        return str(self.items)

def ordenar_con_pila(lista):
    """
    Ordena una lista usando el algoritmo de ordenamiento por pila
    """
    if not lista:
        return []
    
    pila_principal = Pila()
    pila_auxiliar = Pila()
    
    # Apilar el primer elemento
    pila_principal.apilar(lista[0])
    
    # Ordenar los elementos restantes
    for elemento in lista[1:]:
        # Desapilar elementos hasta encontrar la posición correcta
        while not pila_principal.esta_vacia() and elemento > pila_principal.ver_tope():
            pila_auxiliar.apilar(pila_principal.desapilar())
        
        # Apilar el elemento actual
        pila_principal.apilar(elemento)
        
        # Reapilar los elementos de la pila auxiliar
        while not pila_auxiliar.esta_vacia():
            pila_principal.apilar(pila_auxiliar.desapilar())
    
    # Convertir la pila ordenada a lista
    lista_ordenada = []
    while not pila_principal.esta_vacia():
        lista_ordenada.insert(0, pila_principal.desapilar())
    
    return lista_ordenada
   
    from collections import deque 

class PilaPrioridad:
    def __init__(self):
        self.items = []  # Guardamos tuplas (elemento, prioridad)
    
    def esta_vacia(self):
        return len(self.items) == 0
    
    def apilar(self, item, prioridad):
        self.items.append((item, prioridad))
    
    def desapilar(self):
        if self.esta_vacia():
            return None
        # Buscar el de mayor prioridad
        max_prioridad = max(self.items, key=lambda x: x[1])[1]
        
        # Recorrer desde el final (LIFO), sacar el primero que coincida
        for i in range(len(self.items) - 1, -1, -1):
            if self.items[i][1] == max_prioridad:
                return self.items.pop(i)
    
    def tamano(self):
        return len(self.items)
    
    def __str__(self):
        return str(self.items)


def ordenar_con_pila_prioridad(lista):
    """
    Ordena una lista de tuplas (elemento, prioridad)
    usando una pila de prioridad.
    """
    if not lista:
        return []
    
    pila = PilaPrioridad()
    
    # Insertamos todos los elementos
    for elemento, prioridad in lista:
        pila.apilar(elemento, prioridad)
    
    lista_ordenada = []
    
    # Vamos sacando según prioridad (y LIFO en empates)
    while not pila.esta_vacia():
        elemento, prioridad = pila.desapilar()
        lista_ordenada.append((elemento, prioridad))
    
    return lista_ordenada

class Cola:
    def __init__(self):
        self.items = deque()
    
    def esta_vacia(self):
        return len(self.items) == 0
    
    def encolar(self, item):
        self.items.append(item)  # entra al final
    
    def desencolar(self):
        if not self.esta_vacia():
            return self.items.popleft()  # sale el primero
        return None
    
    def ver_frente(self):
        if not self.esta_vacia():
            return self.items[0]
        return None
    
    def tamano(self):
        return len(self.items)
    
    def __str__(self):
        return str(list(self.items))
class ColaPrioridad:
    def __init__(self):
        self.items = []  # Guardamos tuplas (elemento, prioridad)
    
    def esta_vacia(self):
        return len(self.items) == 0
    
    def encolar(self, item, prioridad):
        self.items.append((item, prioridad))
    
    def desencolar(self):
        if self.esta_vacia():
            return None
        # Buscar el de mayor prioridad
        max_prioridad = max(self.items, key=lambda x: x[1])[1]
        
        # Recorrer desde el inicio (FIFO), sacar el primero que coincida
        for i in range(len(self.items)):
            if self.items[i][1] == max_prioridad:
                return self.items.pop(i)
    
    def tamano(self):
        return len(self.items)
    
    def __str__(self):
        return str(self.items)
def ordenar_con_cola(lista):
    """
    Ordena la lista usando cola.
    La idea es es encontrar el minimo, agregarlo a la cola y eliminarlo de la lista original.
    Repetir hasta que la lista original esté vacía.}
    """
    if not lista:
        return []
    
    cola=Cola()
    for elemento in lista:
        cola.encolar(elemento) 

    lista_ordenada = []

    while not cola.esta_vacia():
        # Encontrar el mínimo en la cola
        minimo = min(cola.items)

        # Reconstruir la cola sin el mínimo
        nueva_cola = Cola()
        while not cola.esta_vacia():
            valor=cola.desencolar()
            if valor == minimo:
                lista_ordenada.append(valor) # Agregar el minimo a la lista ordenada
            else: 
                nueva_cola.encolar(valor) 
        cola = nueva_cola

    return lista_ordenada
def ordenar_con_cola_prioridad(lista):
    """
    Ordena una lista de tuplas (elemento, prioridad)
    usando una cola de prioridad.
    """
    if not lista:
        return []
    
    cola = ColaPrioridad()
    
    # Insertamos todos los elementos
    for elemento, prioridad in lista:
        cola.encolar(elemento, prioridad)
    
    lista_ordenada = []
    
    # Vamos sacando según prioridad (y FIFO en empates)
    while not cola.esta_vacia():
        elemento, prioridad = cola.desencolar()
        lista_ordenada.append((elemento, prioridad))
    
    return lista_ordenada

def leer_archivo_txt(ruta_archivo):
    """
    Lee un archivo txt y devuelve una lista con las líneas
    """
    try:
        with open(ruta_archivo, 'r', encoding='utf-8') as archivo:
            lineas = [linea.strip() for linea in archivo if linea.strip()]
        return lineas
    except FileNotFoundError:
        print(f"❌ Error: No se encontró el archivo '{ruta_archivo}'")
        return None
    except Exception as e:
        print(f"❌ Error al leer el archivo: {e}")
        return None

def guardar_resultado(ruta_original, lista_ordenada):
    """
    Guarda la lista ordenada en un archivo txt
    """
    try:
        # Extraer el nombre del archivo sin la ruta completa
        from pathlib import Path
        nombre_archivo = Path(ruta_original).name
        nombre_salida = f"ordenado_{nombre_archivo}"
        
        with open(nombre_salida, 'w', encoding='utf-8') as archivo:
            for elemento in lista_ordenada:
                archivo.write(f"{elemento}\n")
        return nombre_salida
    except Exception as e:
        print(f"❌ Error al guardar el archivo: {e}")
        return None

def main():
    print("=" * 50)
    print("📚 ORGANIZADOR DE LISTAS POR PILA O COLA")
    print("=" * 50)
    
    # Solicitar la ruta del archivo al usuario
    ruta_archivo = input("📁 Ingrese la ruta completa del archivo txt: ").strip()
    
    # Leer archivo
    lista_original = leer_archivo_txt(ruta_archivo)
    
    if lista_original is None:
        return
    
    print(f"\n📊 Datos leídos del archivo:")
    print(f"   - Total de elementos: {len(lista_original)}")
    print(f"   - Primeros 20 elementos: {lista_original[:20]}")
    
    # Preguntar el método de ordenamiento
    print("\n🔽 Métodos disponibles:")
    print("   1. Pila")
    print("   2. Cola")
    print("   3. Pila con Prioridad")
    print("   4. Cola con Prioridad")
    metodo = input("👉 Ingrese el número del método que desea usar: ").strip()
    
    # Aplicar el método seleccionado
    if metodo == '1':
        lista_ordenada = ordenar_con_pila(lista_original)
    
    elif metodo == '2':
        lista_ordenada = ordenar_con_cola(lista_original)
    
    elif metodo in ['3', '4']:
        # Convertimos datos a (elemento, prioridad)
        lista_tuplas = []
        for elem in lista_original:
            partes = elem.split("|")
            if len(partes) == 2:
                nombre = partes[0].strip()
                try:
                    prioridad = int(partes[1].strip())
                    lista_tuplas.append((nombre, prioridad))
                except ValueError:
                    print(f"⚠️ Prioridad inválida en la línea: {elem}")
            else:
                print(f"⚠️ Línea ignorada (no tiene formato válido): {elem}")
        
        if metodo == '3':
            lista_ordenada = ordenar_con_pila_prioridad(lista_tuplas)
        else:
            lista_ordenada = ordenar_con_cola_prioridad(lista_tuplas)
    
    else:
        print("❌ Opción no válida. Saliendo del programa.")
        return
    
    # Mostrar resultados
    print(f"\n✅ Lista ordenada:")
    print(f"   - Total de elementos: {len(lista_ordenada)}")
    print(f"   - Primer elemento: {lista_ordenada[0]}")
    print(f"   - Último elemento: {lista_ordenada[-1]}")
    
    # Guardar resultado
    archivo_guardado = guardar_resultado(ruta_archivo, lista_ordenada)
    if archivo_guardado:
        print(f"\n💾 Resultado guardado en: '{archivo_guardado}'")
    
    # Verificar si está ordenado (solo aplica sin prioridad)
    if metodo in ['1', '2'] and lista_ordenada == sorted(lista_original):
        print("✓ Verificación: La lista está correctamente ordenada")

if __name__ == "__main__":
    main()
        