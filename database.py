# Präparation oder Simulationsphase
start = False
end = False            # Wird diese Variable True gesetzt, beendet sich das gesamte Programm


# Dient als Live Datenbank der floats für die Simulation

# Anzahl
num = 10

# Radius (aktuell kein Command zum verändern)
rad = 1

# Beschleunigung (Multiplikator für die in festgelegte Beschleunigung)
acc = 0

# Maximalgeschwindigkeit (Multiplikator für die festgelegte Maximalgeschwindigkeit)
maxv = 100

# Anziehung des Schwarms in sein Zentrum (Multiplikator für die in festgelegte Anziehung)
pull = 1

# Verlauf der Geschwindigkeit (lin=[1,2,3,...]; Werden in einer Funktion zugeordnet)
graph = 1

# Stärke der Random Walks
rndm = 5

# Reset Variable
reset = False

# FPS
FPS = 60

# Stoßtyp
colltp = 0

# Typ des Plotes

setplot = 1
showplot = False

# Default Start und Endposition
startpos = (1200, 400)
endpos = (200, 400)

# Massenmittelpunkt
# Ort
mmp = []
# Geschwindigkeit
mmpv = []
# Intervallzahl
basknum = 10

#

#


Bodies =[]
Globaltime = []
class datahandler:  # Hilfsmittel zur Erfassung der Daten aller Teilchen der Simulation
    def __init__(self, mass):
        self.posxl = []  # an diesen Listen können nun für EIN Teilchen
        self.posyl = []  # alle Werte pro Zeiteinheit angehangen werden
        self.velxl = []
        self.velyl = []
        self.accxl = []
        self.accyl = []
        self.mass = mass

    def getdat(self, posx, posy, velx, vely, accx,
                  accy):  # Die Funktion sollte nach jeder aktualisierung von Globaltime für alle Körper aufgerufen werden
        self.posxl.append(posx)
        self.posyl.append(posy)
        self.velxl.append(velx)
        self.velyl.append(vely)
        self.accxl.append(accx)
        self.accyl.append(accy)
    def clrdat(self):
        self.posxl = []  # an diesen Listen können nun für EIN Teilchen
        self.posyl = []  # alle Werte pro Zeiteinheit angehangen werden
        self.velxl = []
        self.velyl = []
        self.accxl = []
        self.accyl = []