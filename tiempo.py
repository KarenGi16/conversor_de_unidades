"""5) Módulo tiempo.py: Este módulo debe contener funciones para convertir entre diferentes unidades de tiempo, como segundos, minutos y horas. (1 punto) """
def Segundos_a_Minutos(sec):
    min = sec / 60
    return min

def Segundos_a_Horas(sec):
    hr = sec / 3600
    return hr

def Minutos_a_Segundos(min):
    sec = min * 60
    return sec

def Minutos_a_Horas(min):
    hr = min / 60
    return hr

def Horas_a_Segundos(hr):
    sec = hr * 3600
    return sec

def Horas_a_Minutos(hr):
    min = hr * 60
    return min

if __name__ == "__main__":
    print("Ejemplos de conversión de tiempo:")
    print("56 sec a minutos:", Segundos_a_Minutos(56))
    print("67 sec a Horas:", Segundos_a_Horas(67))
    print("23 min a segundos:", Minutos_a_Segundos(23))
    print("27 min a Horas:", Gramos_a_Toneladas(273))
    print("40 t a kilogramos:", Toneladas_a_Kilogramos(40))
    print("100 t a gramos:", Toneladas_a_Gramos(100))