def start_console():
    import database
    import sys
    print("console online")

    while True:
            if database.end == True:
                sys.exit()

            inp = str(input())

            if database.start == False :                             # Simulation in der Präparation

                    inp = list(map(str, inp.split(' ')))
                    skill = True

                    try:                                    # Überprüfung, ist erstes Wort int und zweites float?
                        com = str(inp[0])   # command
                        zahl = int(inp[1])   # Int (später: Float. Achtung: Anzahl und Graph dürfen nur int)
                    except:
                        skill = False

                    if len(inp) == 2 and skill == True:

                        match com:
                            case "setnum":                            # Anzahl umdefinieren

                                if zahl >= 0:
                                    database.num = zahl
                                    print("Ein Set mit " + str(database.num) )
                                else:
                                    print("Syntaxfehler, kein gültiges Argument. Siehe Anleitung: 'manual'. Error S03")

                            case "setacc":                             # Beschleunigung umdefinieren

                                database.acc = zahl
                                print("Beschleunigungsmultiplikator " + str(database.acc) )

                            case "setmaxv":                             # Maximalgeschwindigkeit umdefinieren

                                database.maxv = zahl
                                print("Maximalgeschwindigkeit " + str(database.maxv))

                            case "setpull":                             # Anziehung des Schwarms umdefinieren

                                database.pull = zahl
                                print("Anziehung des Schwarms " + str(database.pull))

                            case "setgraph":                             # Verlauf der Geschwindigkeit umdefinieren
                                                                         # Nur bestimmte int zugelassen
                                database.graph = zahl
                                print("Verlauf der Geschwindigkeit des Schwarms: Typ  " + str(database.graph))

                            case "setfps":

                                database.FPS = zahl
                                print(str(zahl) + " frames per second")

                            case "setrandom":

                                database.rndm = zahl
                                print("Stärke der Randomwalks ist " + str(zahl))

                            case "setbasket":

                                if zahl > 0:                            #### and isinstance(zahl, int) == True:
                                    database.basknum = zahl
                                    print("Die Intervallzahl für die Verteilungen ist "+ str(int(zahl)))
                                else:
                                    print("Syntaxfehler, kein gültiges Argument. Siehe Anleitung: 'manual'. Error S03")

                            case "plottype":

                                if zahl > -3 and zahl <= 20:
                                    database.setplot = zahl
                                    print("Plottyp ist nun " + str(zahl))
                                    database.showplot = True
                                else:
                                    print("Syntaxfehler, kein gültiges Argument. Siehe Anleitung: 'manual'. Error S03")

                            case "colltype":
                                if (zahl in range(-5, 5)) or zahl == 10:
                                    database.colltp = zahl
                                    print("Stoßmodell ist nun " + str(zahl))
                                else:
                                    print("Syntaxfehler, kein gültiges Argument. Siehe Anleitung: 'manual'. Error S03")

                            case other:                                  # Debug ungültiger Command bei Zweiwortcommand

                                print("Syntaxfehler, kein gültiger command. Siehe Anleitung: 'manual'. Error S02")

                    elif len(inp) == 1 and skill == False:

                        match com:
                            case "checknum":                   # Anzahl abfragen

                                print("Ein Set mit " + str(database.num))

                            case "checkacc":                    # Beschleunigung abfragen

                                print("Beschleunigungsmultiplikator " + str(database.acc))

                            case "checkmaxv":                   # Maximalgeschwindigkeit abfragen

                                print("Maximalgeschwindigkeit " + str(database.maxv))

                            case "checkpull":                   # Anziehung des Schwarms abfragen

                                print("Anziehung des Schwarms " + str(database.pull))

                            case "checkgraph":                  # Verlauf der Geschwindigkeit des Schwarms abfragen

                                print("Verlauf der Geschwindigkeit des Schwarms: Typ " + str(database.graph))

                            case "checktype":

                                print("der Plottyp ist: " + str(database.setplot))
                                match database.setplot:
                                    case -2:
                                        print("Phasenraum der y-Koordinate")
                                    case -1:
                                        print("Phasenraum der x-Koordinate")
                                    case 0:
                                        print("Trajektorien der Teilchen")
                                    case 1:
                                        print("Mittlerer Abstand gegen Zeit")
                                    case 2:
                                        print("Position des CM gegen Zeit")
                                    case 3:
                                        print("Mittlerer Geschwindigkeitsbetrag gegen Zeit")
                                    case 4:
                                        print("Geschwindigkeitsverteilung")
                                    case 5:
                                        print("Anisometrie d. Geschw. gegen Zeit")
                                    case 6:
                                        print("Isometrie d. Geschw. gegen Zeit")
                                    case 7:
                                        print("Mittlerer Beschleunigungsbetrag gegen Zeit")
                                    case 8:
                                        print("Beschleunigungsverteilung")
                                    case 9:
                                        print("Anisometrie d. Beschl. gegen Zeit")
                                    case 10:
                                        print("Isometrie d. Beschleunigung gegen Zeit")
                                    case 11:
                                        print("Mittlerer Abstand gegen Zeit, nur Datenausgabe")
                                    case 12:
                                        print("Position des CM gegen Zeit, nur Datenausgabe")
                                    case 13:
                                        print("Mittlerer Geschwindigkeitsbetrag gegen Zeit, nur Datenausgabe")
                                    case 14:
                                        print("Geschwindigkeitsverteilung, nur Datenausgabe")
                                    case 15:
                                        print("Anisometrie d. Geschw. gegen Zeit, nur Datenausgabe")
                                    case 16:
                                        print("Isometrie d. Geschw. gegen Zeit, nur Datenausgabe")
                                    case 17:
                                        print("Mittlerer Beschleunigungsbetrag gegen Zeit, nur Datenausgabe")
                                    case 18:
                                        print("Beschleunigungsverteilung, nur Datenausgabe")
                                    case 19:
                                        print("Anisometrie d. Beschl. gegen Zeit, nur Datenausgabe")
                                    case 20:
                                        print("Isometrie d. Beschleunigung gegen Zeit, nur Datenausgabe")

                            case "checkrandom":

                                print("Stärke der Randomwalks ist " + str(database.rndm))

                            case "checkbasket":

                                print("die Anzahl an Intervallen für die Verteilungen beträgt " +str(database.basknum))

                            case "checkcoll":

                                print("Das Stoßmodell ist " + str(database.colltp))
                                match database.colltp:
                                    case 0:
                                        print("Standard, instantane Abstoßung bei Kollision")
                                    case 1:
                                        print("~1/r abstoßende Kräfte der Teilchen aufeinander")
                                    case 2:
                                        print("~1/r^2 abstoßende Kräfte der Teilchen aufeinander")
                                    case 3:
                                        print("~1/r^3 abstoßende Kräfte der Teilchen aufeinander")
                                    case 4:
                                        print("~ln(r) abstoßende und anziehende Wechselwirkungskräfte")
                                    case 5:
                                        print("~exp{1/r} abstoßende Wechselwirkungskräfte")
                                    case 10:
                                        print("Keinerlei Interaktionen bzw. Stöße der Teilchen untereinander,")
                                        print("nur Randomwalks")
                                    case -1:
                                        print("~1/r abstoßende Kräfte der Teilchen aufeinander + Standard")
                                    case -2:
                                        print("~1/r^2 abstoßende Kräfte der Teilchen aufeinander + Standard")
                                    case -3:
                                        print("~1/r^3 abstoßende Kräfte der Teilchen aufeinander + Standard")
                                    case -4:
                                        print("~ln(r) abstoßende und anziehende Wechselwirkungskräfte + Standard")
                                    case -5:
                                        print("~exp{1/r} abstoßende Wechselwirkungskräfte + Standard")

                            case "start":

                                print("Simulation wird live geschalten")
                                database.start = True

                            case "quit":

                                print("Simulationsbeendung eingeleitet")
                                database.end = True              # gesamtes Programm wird beendet

                            case "clrmeasurement":

                                print("Messdaten werden zurückgesetzt")
                                for dath in database.Bodies:
                                    dath.clrdat()
                                database.Globaltime = []

                            case "manual":

                                print()
                                print("######  Swarming-Simulation von Robert Schulz und Richard Lehm  ######")
                                print("                         Gebrauchsanleitung                           ")
                                print()
                                print("Zum Start der Simulation öffnet sich ein Fenster, dies ist das ")
                                print("graphische Interface auf welchem Sie die Simulation beobachten")
                                print("können.")
                                print("Sie können die Startbedingungen sowie die graphische Analyse des")
                                print("Teilchenschwarmes mithilfe von Konsolenbefehlen einstellen, welche")
                                print("im Allgemeinen die Form, '<Prädikat> <Integer-Argument>' haben")
                                print("Folgende Befehle dieser Form haben folgende Funktion:")
                                print()
                                print("setnum <Zahlwert>: setzt die Anzahl der Teilchen innerhalb des")
                                print("                   Schwarmes auf <Zahlwert>; nur nichtnegative Integer")
                                print()
                                print("setacc <Zahlwert>: setzt den Multiplikator, mit dem die")
                                print("                   Gravitation des setzbaren Gravitationszentrums")
                                print("                   auf <Zahlwert>")
                                print()
                                print("setmaxv <Zahlwert>: setzt die Maximalgeschwindigkeit der Teilchen auf")
                                print("                    <Zahlwert>; nur positive Integer")
                                print()
                                print("setfps <Zahlwert>: setzt die maximale Bildrate mit welcher die")
                                print("                   Simulation läuft auf <Zahlwert>; nur posistive")
                                print("                   Integer")
                                print()
                                print("setrandom <Zahlwert>: setzt die stärke/ maximale schrittweite der")
                                print("                      Randomwalks auf <Zahlwert>")
                                print()
                                print("setbasket <Zahlwert>: setzt die Anzahl an diskreten Intervallen für die")
                                print("                      Verteilungen auf <Zahlwert>; nur positive Integer")
                                print()
                                print("colltype <Zahlwert>: setzt das Stoßmodell, welches für die Simulation")
                                print("                     verwendet wird auf <Zahlwert> gesetzt.")
                                print("                     Folgende <Zahlwert> legen folgende Stoßmodelle")
                                print("                     fest:")
                                print()
                                print("                     -1:~1/r abstoßende Kräfte der Teilchen aufeinander")
                                print("                        + Standard")
                                print()
                                print("                     -2:~1/r^2 abstoßende Kräfte der Teilchen aufeinander")
                                print("                        + Standard")
                                print()
                                print("                     -3:~1/r^3 abstoßende Kräfte d. Teilchen aufeinander")
                                print()
                                print("                     -4:~ln() abstoßende u. anziehende Kräfte + Standard")
                                print()
                                print("                     -5:~exp(1/r) abstoßende Kräfte + Standard")
                                print()
                                print("                     0:Standard, instantane Abstoßung bei Kollision")
                                print()
                                print("                     1:~1/r abstoßende Kräfte der Teilchen aufeinander")
                                print()
                                print("                     2:~1/r^2 abstoßende Kräfte der Teilchen aufeinander")
                                print()
                                print("                     3:~1/r^3 abstoßende Kräfte d. Teilchen aufeinander")
                                print()
                                print("                     4:~ln() abstoßende u. anziehende Kräfte")
                                print()
                                print("                     5:~exp(1/r) abstoßende Kräfte")
                                print()
                                print()
                                print("plottype <Zahlwert>: dieser Befehl erzeugt beim Pausieren der Simulation")
                                print("                     einen Plot, entsprechend <Zahlwert>.")
                                print("                     Folgende <Zahlwert> erzeugen folgende Plots:")
                                print()
                                print("                    -2: Phasenraum der y-Koordinate")
                                print()
                                print("                    -1: Phasenraum der x-Koordinate")
                                print()
                                print("                     0: Bewegungsverläufe aller Teilchen")
                                print()
                                print("                     1: Mittlerer Abstand gegen Zeit")
                                print()
                                print("                     2: Position des Massenmittelpunktes (CM) gegen Zeit")
                                print()
                                print("                     3: Mittlerer Geschwindigkeitsbetrag gegen Zeit")
                                print()
                                print("                     4: Geschwindigkeitsverteilung")
                                print()
                                print("                     5: Betrag d. mittleren Geschwindigkeitsvektors")
                                print("                        gegen Zeit")
                                print()
                                print("                     6: Isometrie d. Geschwindigkeit gegen d. Zeit")
                                print()
                                print("                     7: Mittlerer Beschleunigungsbetrag gegen Zeit")
                                print()
                                print("                     8: Beschleunigungsverteilung")
                                print()
                                print("                     9: Betrag d. mittleren Beschleunigungsvektors")
                                print("                        gegen Zeit")
                                print()
                                print("                     10: Isometrie d. Beschleunigung")
                                print()
                                print("Mit Ausnahme von <Zahlwert>=0 gibt eine Erhöhung von <Zahlwert> um 10  ")
                                print("dieselben Daten welche geplottet werden in die Konsole aus")
                                print()
                                print("Zusätzlich zu diesen 'Prädikat-Argument' Befehlen gibt es auch eine")
                                print("Reihe von Ein-Wortbefehlen, diese Lauten:")
                                print()
                                print("checknum: Gibt die aktuelle Teilchenzahl des Schwarmes aus")
                                print()
                                print("checkacc: Gibt den aktuellen Multiplikator der Kraft des Gravita-")
                                print("          tionszentrums aus.")
                                print()
                                print("checkmaxv: Gibt die aktuelle Maximalgeschwindigkeit der Teilchen aus")
                                print()
                                print("checkrandom: Gibt die Stärke/ die maximale Schrittweite der Random-")
                                print("             walks aus")
                                print()
                                print("checktype: Gibt den Wert des aktuell ausgewählten Plottes aus")
                                print()
                                print("checkcoll: Gibt den Wert des aktuell ausgewählten Stoßmodells aus")
                                print()
                                print("checkbasket: Gibt die aktuelle Anzahl an Intervallen der")
                                print("             Verteilungen aus")
                                print()
                                print("start: Startet die Simulation")
                                print()
                                print("reset: setzt die Simulation auf ihre Grundeinstellungen zurück")
                                print()
                                print("clrmeasurement: löscht alle bisher aus der Simulation gesammelten")
                                print("                Daten")
                                print()
                                print("quit: Beendet die gesamte Anwendung")
                                print()
                                print()
                                print("Simulation kann weiterhin im Interface direkt gesteuert werden.")
                                print("Durch Linksklicken mit der Maus auf einen Punkt des Interface")
                                print("können Sie die Startposition des Schwarmes festlegen.")
                                print("Durch halten der rechten Maustaste und ziehen mit Maus über das")
                                print("Interface können sie Begrenzung ziehen, welche die Teilchen (im")
                                print("Allgemeinen) nicht passieren können.")
                                print("Durch Linksklicken bei gehaltener Feststelltaste auf einen Punkt")
                                print("des Interfaces setzen Sie das Zentrum des Gravitationsfeldes.")
                                print("Durch bestätigen der Leertaste können sie die Simulation starten")
                                print("und pausieren.")
                                print()
                                print("Anmerkung zu den Fehlermeldungen:")
                                print()
                                print("Error S01: Form der Terminaleingabe ist unzulässig, d.h. die Eingabe")
                                print("           im Terminal hat weder die Form '<Prädikat> <Integer>'")
                                print("           noch die Form 'Prädikat>'")
                                print()
                                print("Error S02: Der im Terminal eingegebene Befehl hat zwar eine gültige")
                                print("           Form, jedoch existiert dass verwendete Prädikat nicht")
                                print("Error S03: Die Form und das aufgerufene Prädikat sind korrekt,")
                                print("           aber das verwendete Argument ist für dieses Prädikat")
                                print("           ungültig")

                            case "reset":
                                database.reset = True

                            case other:                         # Debug ungültiger Command bei Einwortcommand

                                print("Syntaxfehler, kein gültiger command. Siehe Anleitung: 'manual'. Error S02")


                    else:                                                                       # Debug Eingabe inkorrekt
                        print ("Syntaxfehler, Eingabe inkorrekt. Siehe Anleitung: 'manual'. Error S01")

            else:           # Wenn Simulation an ist, also start == True

                if inp == "Stop":
                    database.start = False
                else:
                    print("Für Änderung der Randbedingung Simulation mit dem Befehl Stop beenden.")

