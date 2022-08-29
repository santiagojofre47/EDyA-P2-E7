class Cliente:
    __numero = None
    __tiempo_llegada = None
    __tiempo_espera = None
    
    def __init__(self, numero, tiempo_llegada):
        self.__numero = numero
        self.__tiempo_llegada = tiempo_llegada
        self.__tiempo_espera = 0
    
    def getNumeroCliente(self):
        return self.__numero
    
    def calcular_tiempo_espera(self, tiempo_actual):
        self.__tiempo_espera = tiempo_actual - self.__tiempo_llegada
    
    def getTiempoEspera(self):
        return self.__tiempo_espera

        