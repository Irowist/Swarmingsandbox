# Swarming Projekt

SciCo WS 22/23

######  Swarming-Simulation von Robert Schulz und Richard Lehm  ######
## Gebrauchsanleitung                           
   
   Zum Start der Simulation öffnet sich ein Fenster, dies ist das 
   graphische Interface auf welchem Sie die Simulation beobachten
   können.
   Sie können die Startbedingungen sowie die graphische Analyse des
   Teilchenschwarmes mithilfe von Konsolenbefehlen einstellen, welche
   im Allgemeinen die Form, '<Prädikat> <Integer-Argument>' haben
   Folgende Befehle dieser Form haben folgende Funktion:
   
   setnum <Zahlwert>: setzt die Anzahl der Teilchen innerhalb des
                      Schwarmes auf <Zahlwert>; nur nichtnegative Integer
   
   setacc <Zahlwert>: setzt den Multiplikator, mit dem die
                      Gravitation des setzbaren Gravitationszentrums
                      auf <Zahlwert>
   
   setmaxv <Zahlwert>: setzt die Maximalgeschwindigkeit der Teilchen auf
                       <Zahlwert>; nur positive Integer
   
   setfps <Zahlwert>: setzt die maximale Bildrate mit welcher die
                      Simulation läuft auf <Zahlwert>; nur posistive
                      Integer
   
   setrandom <Zahlwert>: setzt die stärke/ maximale schrittweite der
                         Randomwalks auf <Zahlwert>
   
   setbasket <Zahlwert>: setzt die Anzahl an diskreten Intervallen für die
                         Verteilungen auf <Zahlwert>; nur positive Integer
   
   colltype <Zahlwert>: setzt das Stoßmodell, welches für die Simulation
                        verwendet wird auf <Zahlwert> gesetzt.
                        Folgende <Zahlwert> legen folgende Stoßmodelle
                        fest:
   
                        -1:~1/r abstoßende Kräfte der Teilchen aufeinander
                           + Standard
   
                        -2:~1/r^2 abstoßende Kräfte der Teilchen aufeinander
                           + Standard
   
                        -3:~1/r^3 abstoßende Kräfte d. Teilchen aufeinander
   
                        -4:~ln() abstoßende u. anziehende Kräfte + Standard
   
                        -5:~exp(1/r) abstoßende Kräfte + Standard
   
                        0:Standard, instantane Abstoßung bei Kollision
   
                        1:~1/r abstoßende Kräfte der Teilchen aufeinander
   
                        2:~1/r^2 abstoßende Kräfte der Teilchen aufeinander
   
                        3:~1/r^3 abstoßende Kräfte d. Teilchen aufeinander
   
                        4:~ln() abstoßende u. anziehende Kräfte
   
                        5:~exp(1/r) abstoßende Kräfte
   
   
   plottype <Zahlwert>: dieser Befehl erzeugt beim Pausieren der Simulation
                        einen Plot, entsprechend <Zahlwert>.
                        Folgende <Zahlwert> erzeugen folgende Plots:
   
                       -2: Phasenraum der y-Koordinate
   
                       -1: Phasenraum der x-Koordinate
   
                        0: Bewegungsverläufe aller Teilchen
   
                        1: Mittlerer Abstand gegen Zeit
   
                        2: Position des Massenmittelpunktes (CM) gegen Zeit
   
                        3: Mittlerer Geschwindigkeitsbetrag gegen Zeit
   
                        4: Geschwindigkeitsverteilung
   
                        5: Betrag d. mittleren Geschwindigkeitsvektors
                           gegen Zeit
   
                        6: Isometrie d. Geschwindigkeit gegen d. Zeit
   
                        7: Mittlerer Beschleunigungsbetrag gegen Zeit
   
                        8: Beschleunigungsverteilung
   
                        9: Betrag d. mittleren Beschleunigungsvektors
                           gegen Zeit
   
                        10: Isometrie d. Beschleunigung
   
   Mit Ausnahme von <Zahlwert>=0 gibt eine Erhöhung von <Zahlwert> um 10  
   dieselben Daten welche geplottet werden in die Konsole aus
   
   Zusätzlich zu diesen 'Prädikat-Argument' Befehlen gibt es auch eine
   Reihe von Ein-Wortbefehlen, diese Lauten:
   
   checknum: Gibt die aktuelle Teilchenzahl des Schwarmes aus
   
   checkacc: Gibt den aktuellen Multiplikator der Kraft des Gravita-
             tionszentrums aus.
   
   checkmaxv: Gibt die aktuelle Maximalgeschwindigkeit der Teilchen aus
   
   checkrandom: Gibt die Stärke/ die maximale Schrittweite der Random-
                walks aus
   
   checktype: Gibt den Wert des aktuell ausgewählten Plottes aus
   
   checkcoll: Gibt den Wert des aktuell ausgewählten Stoßmodells aus
   
   checkbasket: Gibt die aktuelle Anzahl an Intervallen der
                Verteilungen aus
   
   start: Startet die Simulation
   
   reset: setzt die Simulation auf ihre Grundeinstellungen zurück
   
   clrmeasurement: löscht alle bisher aus der Simulation gesammelten
                   Daten
   
   quit: Beendet die gesamte Anwendung
   
   
   Simulation kann weiterhin im Interface direkt gesteuert werden.
   Durch Linksklicken mit der Maus auf einen Punkt des Interface
   können Sie die Startposition des Schwarmes festlegen.
   Durch halten der rechten Maustaste und ziehen mit Maus über das
   Interface können sie Begrenzung ziehen, welche die Teilchen (im
   Allgemeinen) nicht passieren können.
   Durch Linksklicken bei gehaltener Feststelltaste auf einen Punkt
   des Interfaces setzen Sie das Zentrum des Gravitationsfeldes.
   Durch bestätigen der Leertaste können sie die Simulation starten
   und pausieren.
   
   Anmerkung zu den Fehlermeldungen:
   
   Error S01: Form der Terminaleingabe ist unzulässig, d.h. die Eingabe
              im Terminal hat weder die Form '<Prädikat> <Integer>'
              noch die Form 'Prädikat>'
   
   Error S02: Der im Terminal eingegebene Befehl hat zwar eine gültige
              Form, jedoch existiert dass verwendete Prädikat nicht
   Error S03: Die Form und das aufgerufene Prädikat sind korrekt,
              aber das verwendete Argument ist für dieses Prädikat
              ungültig