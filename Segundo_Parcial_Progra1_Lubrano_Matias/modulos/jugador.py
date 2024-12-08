
class Jugador:
    
    __instanciado = None
    
    def __init__(self, nombre: str = 'MATI'):
        
        if Jugador.__instanciado is None:
            Jugador.__instanciado = self
        
        self.nombre = nombre
        self.puntaje_total = 0
    
    @staticmethod
    def get_jugador():
        if Jugador.__instanciado is None:
            Jugador()
        return Jugador.__instanciado
    
    @staticmethod
    def esta_instanciado():
        return Jugador.__instanciado != None
    
    def get_nombre(self):
         return self.nombre

    def set_nombre(self, nombre: str):
         self.nombre = nombre
    
    def set_puntaje(self, puntaje: int):
        self.puntaje_total = puntaje

    def get_puntaje_total(self):
        return self.puntaje_total
    
    def to_csv_format(self):
        return f'\n{self.nombre},{self.puntaje_total}'
    
        
        