"""2) Módulo masa.py: Este módulo debe contener funciones para convertir entre diferentes unidades de masa, como kilogramos, libras y onzas.(0.5 puntos) """
def Kilogramos_a_Gramos(kg):
    g = kg * 1000
    return g

def Kilogramos_a_Toneladas(kg):
    t = kg / 1000
    return t

def Gramos_a_Kilogramos(g):
    kg = g / 1000
    return kg

def Gramos_a_Toneladas(g):
    t = g / 1000000
    return t

def Toneladas_a_Kilogramos(t):
    kg = t * 1000
    return kg

def Toneladas_a_Gramos(t):
    g = t * 1000000
    return g

if __name__ == "__main__":
    print("Ejemplos de conversión de masa:")
    print("25 kg a gramos:", Kilogramos_a_Gramos(25))
    print("98 kg a toneladas:", Kilogramos_a_Toneladas(98))
    print("23 g a kilogramos:", Gramos_a_Kilogramos(23))
    print("273 g a toneladas:", Gramos_a_Toneladas(273))
    print("40 t a kilogramos:", Toneladas_a_Kilogramos(40))
    print("100 t a gramos:", Toneladas_a_Gramos(100))