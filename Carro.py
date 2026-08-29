class Carro:
    # 1. Nuestro único constructor (__init__)
    # Le ponemos valores por defecto para que funcione como constructor vacío Y con parámetros
    # self: Referencia al objeto que se está creando
    def __init__(self, color: str = "Sin definir", año: int = 0, serie: str = "0000-0000"):
        # 2. Atributos privados (usando los dobles guiones bajos __ )
        self.__color = color
        self.__año = año
        self.__serie = serie

    # 3. GETTERS
    def get_color(self) -> str:
        return self.__color
        
    def get_año(self) -> int:
        return self.__año
        
    def get_serie(self) -> str:
        return self.__serie

    # 4. SETTERS
    def set_color(self, color: str):
        self.__color = color
        
    def set_año(self, año: int):
        self.__año = año
        
    def set_serie(self, serie: str):
        self.__serie = serie

# ==========================================
# CLASE MAIN (Aquí instanciamos los objetos)
# ==========================================

# Carro 1: Usamos el "constructor vacío" (tomará los valores por defecto)
carro_1 = Carro()

# Carro 2: Usamos el constructor con parámetros
carro_2 = Carro("Negro", 2026, "XV-777")

# Imprimimos para comprobar que los getters funcionan
print("CARRO 1 (Constructor vacío):")
print(f"Color: {carro_1.get_color()} | Año: {carro_1.get_año()} | Serie: {carro_1.get_serie()}\n")

print("CARRO 2 (Constructor con parámetros):")
print(f"Color: {carro_2.get_color()} | Año: {carro_2.get_año()} | Serie: {carro_2.get_serie()}")