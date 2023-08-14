class Ahorro:
    def __init__(self, nombre, cantidad):
        self.nombre = nombre
        self.cantidad = cantidad

    def __str__(self):
        return f"{self.nombre}: ${self.cantidad:.2f}"

class GestorAhorros:
    def __init__(self):
        self.ahorros = []

    def agregar_ahorro(self, ahorro):
        self.ahorros.append(ahorro)

    def mostrar_ahorros(self):
        for ahorro in self.ahorros:
            print(ahorro)

def main():
    gestor = GestorAhorros()

    while True:
        print("Opciones:")
        print("1. Agregar ahorro")
        print("2. Mostrar ahorros")
        print("3. Saldo Total")
        print("4. Salir")
        opcion = input("Selecciona una opción: ")

        if opcion == "1":
            nombre = input("Ingrese el nombre del ahorro: ")
            cantidad = float(input("Ingrese la cantidad ahorrada: "))
            ahorro = Ahorro(nombre, cantidad)
            gestor.agregar_ahorro(ahorro)
            print("Ahorro agregado exitosamente.")

        elif opcion == "2":
            print("Lista de ahorros:")
            gestor.mostrar_ahorros()

        elif opcion == "3":
            total = sum(ahorro.cantidad for ahorro in gestor.ahorros)
            print(f"Saldo total ahorrado: ${total:.2f}")
        
        elif opcion == "4":
            print("¡Hasta luego!")
            break

        else:
            print("Opción no válida. Por favor, elija una opción válida.")

if __name__ == "__main__":
    main()

