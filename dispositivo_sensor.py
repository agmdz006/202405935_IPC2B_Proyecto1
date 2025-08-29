from nodo_dinamico import ListaDinamica

class DispositivoSensor:
    def __init__(self, codigo_sensor, descripcion):
        self.codigo_sensor = codigo_sensor
        self.descripcion = descripcion
        self.datos_transmision = ListaDinamica()
