import random
from claseColaEncadenada import Cola
from claseCliente import Cliente

if __name__ == '__main__':
    cola_cajero = Cola()
    tiempo_atencion = int(input('Ingrese el tiempo de atencion al cliente: '))
    frecuencia__llegada = int(input('Ingrese la frecuencia de llegada de los clientes: '))
    t__llegada = 1/frecuencia__llegada#Conversion de frecuencia a tiempo (T= 1/F)
    tiempo_cajero = 0
    maximo = -1
    i = 0
    n_cliente = 0
    while i<=50:
        tiempo_cajero+=1
        if t__llegada == (1/random.randint(1,frecuencia__llegada)):
            print('Minuto {}: Ha llegado un cliente!'.format(i))
            nuevo_cliente = Cliente(n_cliente,i)
            cola_cajero.insertar(nuevo_cliente)
            n_cliente+=1
        if tiempo_cajero == tiempo_atencion:
            if not cola_cajero.vacio():
                cliente_atendido = cola_cajero.suprimir()
                print('Minuto {}: se atendio al cliente {}'.format(i,cliente_atendido.getNumeroCliente()))
                cliente_atendido.calcular_tiempo_espera(i)
                if maximo < cliente_atendido.getTiempoEspera():
                    maximo = cliente_atendido.getTiempoEspera()
                tiempo_cajero = 0
            else:
                tiempo_cajero = 0
        i+=1
    print('--- \tSimulacion finalizada \t---')
    print('Tiempo maximo de espera de los clientes en la cola: {} minutos'.format(maximo))
    
        
        
        
        
