class Equipo:
    def __init__(self, nombre, integrantes):
        self.nombre = nombre
        self.integrantes = integrantes
    
    def __str__(self):
        return f"Equipo {self.nombre}:\n" + "\n".join(self.integrantes)

class FS3:
    def __init__(self, equipos):
        self.equipos = equipos
    
    def __str__(self):
        return "\n\n".join(str(equipo) for equipo in self.equipos)

# Definir los equipos
equipo_toyota_legacy = Equipo("Toyota Legacy", [
    "Israel Chacon Rojo",
    "Dilan Mauricio Garcia Hernandez",
    "Jesus Elias Sierra Ruiz"
])

equipo_3_mosqueteros = Equipo("3 mosqueteros", [
    "Dania Denisse Benavides Figueroa",
    "Erick Lozano Duarte",
    "Ana Cristina Valenzuela Ruiz"
])

equipo_pinguino_galactico = Equipo("Pingüino Galáctico", [
    "Yahir Antonio Monje Ochoa",
    "Yesica Cristina Rodriguez Renteria"
])

equipo_los_polystation = Equipo("Los Polystation", [
    "Erick Fernando Siqueiros Zúñiga",
    "Paulina Ixchel Arreguin Ruiz"
])

equipo_webheros = Equipo("WebHeros", [
    "Jesus Manuel Arellano Merendon",
    "Axel Felipe Reyes Valadez",
    "Luis Daniel Delgado Enriquez"
])

# Crear objeto FS3 con referencias a los equipos
fs3 = FS3([
    equipo_toyota_legacy,
    equipo_3_mosqueteros,
    equipo_pinguino_galactico,
    equipo_los_polystation,
    equipo_webheros
])

# Imprimir los integrantes de cada equipo al convertir a cadena de texto
print(fs3)