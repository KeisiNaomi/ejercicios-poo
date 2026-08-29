# Clase Scooter
class Scooter:
    # Constructor con datos por defecto
    def __init__(self, id: str = "x-000", nivelBateria: int = 0, disponibilidad: bool = False):
        # Atributos privados
        self.__id = id
        self.__nivelBateria = nivelBateria
        self.__disponibilidad = disponibilidad

    # Metodos publicos
    def desbloquear(self):
        if self.__disponibilidad and self.__nivelBateria >= 20:
            self.__disponibilidad = False
            return True
        return False

    def finalizarViaje(self):
        self.__disponibilidad = True

    def llenarBateria(self):
        self.__nivelBateria = 100

#Clase Usuario
class Usuario:
    # Constructor con datos por defecto
    def __init__(self, nombre: str = "Sin definir", saldo: float = 0.0):
        # Atributos privados
        self.__nombre = nombre
        self.__saldo = saldo

    # Metodos publicos
    def agregarSaldo(self, monto: float):
        self.__saldo += monto

    def rentarScooter(self, scooter: Scooter):
        return scooter.desbloquear()

# Clase Main Sistema de Scooters
# Creacion de un scooter y un usuario
scooter1 = Scooter("S-001", 15, True)
usuario1 = Usuario("Kitty", 100.0)

# Intento de renta del scooter
rentaExitosa = usuario1.rentarScooter(scooter1)
if rentaExitosa:
    print("Renta exitosa. ¡Disfruta tu viaje! :D")
else:
    print("No fue posible rentar el scooter :c")