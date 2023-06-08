


def start_plots():
    import numpy as np
    import matplotlib.pyplot as plt
    import pygame
    from itertools import combinations
    import database


    Value = []  # Eine Liste, welche später die Funktionswerte bekommt sodass Globaltime gegen Value
    # geplotet werden kann



    ####Zu plotende Daten werden berechnet
    match database.setplot:       #den verschiedenen Werten Für Graph werden in dieser match-Schleife
                                # die Verschiedenen Plots Generiert
        case - 2:  # x-Phasenraum
            title = "Phasenraum der y-Koordinate"
            ValueY = []
            Valuehelper = []
            ValueYhelper = []

            for b in database.Bodies:
                for i in range(len(database.Globaltime)):
                    Valuehelper.append(b.posyl[i])
                    ValueYhelper.append(b.velyl[i])

                Value.append(Valuehelper)
                ValueY.append(ValueYhelper)
                Valuehelper = []
                ValueYhelper = []

        case -1: # x-Phasenraum
            title ="Phasenraum der x-Koordinate"
            ValueY =[]
            Valuehelper =[]
            ValueYhelper =[]

            for b  in database.Bodies:
                for i in range(len(database.Globaltime)):
                    Valuehelper.append(b.posxl[i])
                    ValueYhelper.append(b.velxl[i])

                Value.append(Valuehelper)
                ValueY.append(ValueYhelper)
                Valuehelper =[]
                ValueYhelper =[]

        case 0: #absolute Bewegung d. einzelnen Teilchen
            title ="Trajektorien der Teilchen"
            ValueY =[]
            Valuehelper =[]
            ValueYhelper =[]

            for b  in database.Bodies:
                for i in range(len(database.Globaltime)):
                    Valuehelper.append(b.posxl[i])
                    ValueYhelper.append(b.posyl[i])

                Value.append(Valuehelper)
                ValueY.append(ValueYhelper)
                Valuehelper =[]
                ValueYhelper =[]



        case 1: #c1() #(Betrag d. Mittleren Abstandes) (Pain)
            title = "Betrag d. Mittleren Abstandes"

            for k in range(len(database.Globaltime)):
                dist = 0
                n = 0
                for k1, k2 in combinations(database.Bodies, 2):
                    dist = dist + np.sqrt((k1.posxl[k] - k2.posxl[k]) ** 2 + (k1.posyl[k] - k2.posyl[k]) ** 2)
                    n = n + 1
                Value.append(dist / n)

        case 2:  # c11()
            title = "Position des CM"

            ValueY = []
            for k in range(len(database.Globaltime)):
                Value.append(database.mmp[k].x)
                ValueY.append(database.mmp[k].y)
                #    mavx = 0
                #    mavy = 0
                #    Masss = 0
                # for i in range(len(Bodies)):
                #    mavx = mavx + Bodies[i].posx[k] * Bodies[i].mass
                #    mavy = mavy + Bodies[i].posy[k] * Bodies[i].mass
                #    Masss = Masss + Bodies[i].mass
                # Value.append(mavx / Masss)
                # ValueY.append(mavy / Masss)

        case 3: #c2()
            title = "Mittlerer Betrag d. Geschwindigkeiten"

                                            #Es folgt die Berechnung des Arithmetischen mittleren Geschwindigkeitsbetrages
            for k in range(len(database.Globaltime)):    #hier wird nun jedem Zeitpunkt ein Geschwindigkeitsbetrag zugeordnet
                velabs = 0                      #eine Hilfsvariable
                for i in range(len(database.Bodies)):
                    velabs = velabs + np.sqrt(database.Bodies[i].velxl[k]**2+database.Bodies[i].velyl[k]**2)
                Value.append(velabs/len(database.Bodies))

        case 4:
            title = "Geschwindigkeitsverteilung"
            basket = []
            count = 0
            for b in database.Bodies:
                basket.append(np.sqrt(b.velxl[-1] ** 2 + b.velyl[-1] ** 2))
            basksize = 1.5 * max(basket) / database.basknum
            basket = []
            for k in range(database.basknum):
                basket.append(k * basksize)
                Value.append(0)
            for b in database.Bodies:
                for k in range(len(basket)):
                    if (np.sqrt(b.velxl[-1] ** 2 + b.velyl[-1] ** 2) < (basket[k] + basksize / 2)) and (
                            (basket[k] - basksize / 2) <= np.sqrt(b.velxl[-1] ** 2 + b.velyl[-1] ** 2)):
                        Value[k] += 1
                        count += 1
            print("Gesamtsumme: " + str(count))

        case 5:  # c12()
            title = "Anisometrie d. Geschwindigkeiten"

            # Einfach nur die Berechung der Mittleren Geschwindigkeit
            for k in range(len(database.Globaltime)):
                veliso = pygame.Vector2(0, 0)  # eine Hilfsvariable
                for i in range(len(database.Bodies)):
                    veliso = veliso + pygame.Vector2(database.Bodies[i].velxl[k], database.Bodies[i].velyl[k])

                Value.append(np.sqrt(veliso.x ** 2 + veliso.y ** 2) / len(database.Bodies))

        case 6:
            title = "Relative Isometrie d. Geschwindigkeiten"

            for k in range(len(database.Globaltime)):
                veliso = pygame.Vector2(0, 0)  # eine Hilfsvariable
                velabs = 0
                for i in range(len(database.Bodies)):
                    veliso = veliso + pygame.Vector2(database.Bodies[i].velxl[k], database.Bodies[i].velyl[k])
                    velabs = velabs + np.sqrt(database.Bodies[i].velxl[k] ** 2 + database.Bodies[i].velyl[k] ** 2)
                if velabs == 0 or veliso.length() ==0:
                    Value.append(1)
                else:
                    Value.append(np.exp(-np.sqrt(veliso.x ** 2 + veliso.y ** 2) / velabs) - np.exp(-velabs/(np.sqrt(veliso.x ** 2 + veliso.y ** 2))))

        case 7: #c3()
            title = "Mittlerer Betrag d. Beschleunigungen"

            # Es folgt die Berechnung des Arithmetischen mittleren Beschleunigungsbetrages
            for k in range(len(database.Globaltime)):  # hier wird nun jedem Zeitpunkt ein Beschleunigungsbetrag zugeordnet
                accabs = 0  # eine Hilfsvariable
                for i in range(len(database.Bodies)):
                    accabs = accabs + np.sqrt(database.Bodies[i].accxl[k] ** 2 + database.Bodies[i].accyl[k] ** 2)
                Value.append(accabs / len(database.Bodies))


        case 8:
            title = "Beschleunigungssverteilung"
            basket = []
            count = 0
            for b in database.Bodies:
                basket.append(np.sqrt(b.accxl[-1] ** 2 + b.accyl[-1] ** 2))
            basksize = 1.5 * max(basket) / database.basknum
            basket = []
            for k in range(database.basknum):
                basket.append(k * basksize)
                Value.append(0)
            for b in database.Bodies:
                for k in range(len(basket)):
                    if (np.sqrt(b.accxl[-1] ** 2 + b.accyl[-1] ** 2) < (basket[k] + basksize / 2)) and (
                            (basket[k] - basksize / 2) <= np.sqrt(b.accxl[-1] ** 2 + b.accyl[-1] ** 2)):
                        Value[k] += 1
                        count += 1
            print("Gesamtsumme: " + str(count))


        case 9: #c13()
            dim = "2d"
            title = "Anisometrie d. Beschleunigungen"
            for k in range(len(database.Globaltime)):
                acciso = pygame.Vector2(0, 0)  # eine Hilfsvariable
                for i in range(len(database.Bodies)):
                    acciso = acciso + pygame.Vector2(database.Bodies[i].accxl[k],  database.Bodies[i].accyl[k])
                Value.append(np.sqrt(acciso.x**2 + acciso.y**2) / len(database.Bodies))

        case 10:
            title = "Relative Isometrie d. Beschleunigungen"

            for k in range(len(database.Globaltime)):
                acciso = pygame.Vector2(0, 0)  # eine Hilfsvariable
                accabs = 0
                for i in range(len(database.Bodies)):
                    acciso = acciso + pygame.Vector2(database.Bodies[i].accxl[k], database.Bodies[i].accyl[k])
                    accabs = accabs + np.sqrt(database.Bodies[i].accxl[k] ** 2 + database.Bodies[i].accyl[k] ** 2)
                if accabs == 0 or acciso.length()==0:
                    Value.append(1)
                else:
                    Value.append( np.exp(-np.sqrt(acciso.x ** 2 + acciso.y ** 2) / accabs) - np.exp(-accabs/(np.sqrt(acciso.x ** 2 + acciso.y ** 2))))


        case 11:  # c1() #(Betrag d. Mittleren Abstandes) (Pain)
            title = "Betrag d. Mittleren Abstandes print"

            for k in range(len(database.Globaltime)):
                dist = 0
                n = 0
                for k1, k2 in combinations(database.Bodies, 2):
                    dist = dist + np.sqrt((k1.posxl[k] - k2.posxl[k]) ** 2 + (k1.posyl[k] - k2.posyl[k]) ** 2)
                    n = n + 1
                Value.append(dist / n)

        case 12:  # c11()
            title = "Position des CM print"

            ValueY = []
            for k in range(len(database.Globaltime)):
                Value.append(database.mmp[k].x)
                ValueY.append(database.mmp[k].y)
                #    mavx = 0
                #    mavy = 0
                #    Masss = 0
                # for i in range(len(Bodies)):
                #    mavx = mavx + Bodies[i].posx[k] * Bodies[i].mass
                #    mavy = mavy + Bodies[i].posy[k] * Bodies[i].mass
                #    Masss = Masss + Bodies[i].mass
                # Value.append(mavx / Masss)
                # ValueY.append(mavy / Masss)

        case 13:  # c2()
            title = " Mittlerer Betrag d. Geschwindigkeiten print"

            # Es folgt die Berechnung des Arithmetischen mittleren Geschwindigkeitsbetrages
            for k in range(
                    len(database.Globaltime)):  # hier wird nun jedem Zeitpunkt ein Geschwindigkeitsbetrag zugeordnet
                velabs = 0  # eine Hilfsvariable
                for i in range(len(database.Bodies)):
                    velabs = velabs + np.sqrt(database.Bodies[i].velxl[k] ** 2 + database.Bodies[i].velyl[k] ** 2)
                Value.append(velabs / len(database.Bodies))

        case 14:
            title = "Geschwindigkeitsverteilung print"
            basket = []
            count = 0
            for b in database.Bodies:
                basket.append(np.sqrt(b.velxl[-1] ** 2 + b.velyl[-1] ** 2))
            basksize = 1.5 * max(basket) / database.basknum
            basket = []
            for k in range(database.basknum):
                basket.append(k * basksize)
                Value.append(0)
            for b in database.Bodies:
                for k in range(len(basket)):
                    if (np.sqrt(b.velxl[-1] ** 2 + b.velyl[-1] ** 2) < (basket[k] + basksize / 2)) and (
                            (basket[k] - basksize / 2) <= np.sqrt(b.velxl[-1] ** 2 + b.velyl[-1] ** 2)):
                        Value[k] += 1
                        count += 1
            print("Gesamtsumme: " + str(count))

        case 15:  # c12()
            title = "Anisometrie d. Geschwindigkeiten print"

            # Einfach nur die Berechung der Mittleren Geschwindigkeit
            for k in range(len(database.Globaltime)):
                veliso = pygame.Vector2(0, 0)  # eine Hilfsvariable
                for i in range(len(database.Bodies)):
                    veliso = veliso + pygame.Vector2(database.Bodies[i].velxl[k], database.Bodies[i].velyl[k])

                Value.append(np.sqrt(veliso.x ** 2 + veliso.y ** 2) / len(database.Bodies))

        case 16:
            title = "Relative Isometrie d. Geschwindigkeiten print"

            for k in range(len(database.Globaltime)):
                veliso = pygame.Vector2(0, 0)  # eine Hilfsvariable
                velabs = 0
                for i in range(len(database.Bodies)):
                    veliso = veliso + pygame.Vector2(database.Bodies[i].velxl[k], database.Bodies[i].velyl[k])
                    velabs = velabs + np.sqrt(database.Bodies[i].velxl[k] ** 2 + database.Bodies[i].velyl[k] ** 2)
                Value.append(np.exp(-np.sqrt(veliso.x ** 2 + veliso.y ** 2) / velabs))
                if velabs == 0 or veliso.length() == 0:
                    Value.append(1)
                else:
                    Value.append (np.exp(-np.sqrt(veliso.x ** 2 + veliso.y ** 2) / velabs) - np.exp(
                        -velabs / (np.sqrt(veliso.x ** 2 + veliso.y ** 2))))

        case 17:  # c3()
            title = " Mittlerer Betrag d. Beschleunigungen print"

            # Es folgt die Berechnung des Arithmetischen mittleren Beschleunigungsbetrages
            for k in range(
                    len(database.Globaltime)):  # hier wird nun jedem Zeitpunkt ein Beschleunigungsbetrag zugeordnet
                accabs = 0  # eine Hilfsvariable
                for i in range(len(database.Bodies)):
                    accabs = accabs + np.sqrt(database.Bodies[i].accxl[k] ** 2 + database.Bodies[i].accyl[k] ** 2)
                Value.append(accabs / len(database.Bodies))

        case 18:
            title = "Beschleunigungssverteilung print"
            basket = []
            count = 0
            for b in database.Bodies:
                basket.append(np.sqrt(b.accxl[-1] ** 2 + b.accyl[-1] ** 2))
            basksize = 1.5 * max(basket) / database.basknum
            basket = []
            for k in range(database.basknum):
                basket.append(k * basksize)
                Value.append(0)
            for b in database.Bodies:
                for k in range(len(basket)):
                    if (np.sqrt(b.accxl[-1] ** 2 + b.accyl[-1] ** 2) < (basket[k] + basksize / 2)) and (
                            (basket[k] - basksize / 2) <= np.sqrt(b.accxl[-1] ** 2 + b.accyl[-1] ** 2)):
                        Value[k] += 1
                        count += 1
            print("Gesamtsumme: " + str(count))

        case 19:  # c13()
            dim = "2d"
            title = "Anisometrie d. Beschleunigungen print"
            for k in range(len(database.Globaltime)):
                acciso = pygame.Vector2(0, 0)  # eine Hilfsvariable
                for i in range(len(database.Bodies)):
                    acciso = acciso + pygame.Vector2(database.Bodies[i].accxl[k], database.Bodies[i].accyl[k])
                Value.append(np.sqrt(acciso.x ** 2 + acciso.y ** 2) / len(database.Bodies))

        case 20:
            title = "Relative Isometrie d. Beschleunigungen print"

            for k in range(len(database.Globaltime)):
                acciso = pygame.Vector2(0, 0)  # eine Hilfsvariable
                accabs = 0
                for i in range(len(database.Bodies)):
                    acciso = acciso + pygame.Vector2(database.Bodies[i].accxl[k], database.Bodies[i].accyl[k])
                    accabs = accabs + np.sqrt(database.Bodies[i].accxl[k] ** 2 + database.Bodies[i].accyl[k] ** 2)
                if accabs == 0 or acciso.length() == 0:
                    Value.append(1)
                else:
                    Value.append(np.exp(-np.sqrt(acciso.x ** 2 + acciso.y ** 2) / accabs) - np.exp(
                        -accabs / (np.sqrt(acciso.x ** 2 + acciso.y ** 2))))


    title = str(database.setplot) + ": " + title #Parameter können kolgen


    if len(database.Globaltime) == 0:
        print("keine Messdaten vorhanden")
    else:
        if database.setplot <11:
            match database.setplot:

                case - 2:
                    ax = plt.figure(title).add_subplot()
                    for i in range(len(Value)):
                        ax.plot(Value[i], ValueY[i])
                    ax.set_xlabel("y")
                    ax.set_ylabel(r"$\frac{d}{dt}y$")

                    ax.set_xlim(-1080, 2 * 1080)
                    ax.set_ylim(-600, 2 * 600)

                case -1:
                    ax= plt.figure(title).add_subplot()
                    for i in range(len(Value)):
                        ax.plot(Value[i], ValueY[i])
                    ax.set_xlabel("x")
                    ax.set_ylabel(r"$\frac{d}{dt}x$")

                    ax.set_xlim(-1080, 2 * 1080)
                    ax.set_ylim(-600, 2*600)

                case 0:
                    ax= plt.figure(title).add_subplot()  #projection="3d")
                    for i in range(len(Value)):
                        ax.plot( Value[i], ValueY[i]) #(database.Globaltime,
                    ax.scatter(database.Bodies[0].posxl[0], database.Bodies[0].posyl[0])
                    ax.text(database.Bodies[0].posxl[0], database.Bodies[0].posyl[0], "Start", color='r')

                    #ax.set_xlabel("t in s")
                    ax.set_xlabel("x")
                    ax.set_ylabel("y")

                    #ax.set_xlim(database.Globaltime[0], database.Globaltime[-1])
                    ax.set_xlim(-1080, 2*1080)
                    ax.set_ylim(-600, 2*600)

                case 1:
                    ax = plt.figure(title).add_subplot()  # eine Plotumgebung wird generiert
                    ax.plot(database.Globaltime, Value, label=(title))
                    ax.set_xlabel("t in s")
                    ax.set_ylabel("Mittlerer Abstand")

                    ax.set_ylim(0, np.sqrt(600 * 600 + 1080 * 1080))

                case 2:
                    ax = plt.figure(title).add_subplot(projection="3d")  # eine Plotumgebung wird generiert
                    ax.scatter(database.Globaltime[0], Value[0], ValueY[0])
                    ax.text(database.Globaltime[0], Value[0], ValueY[0], "Start", color='r')

                    ax.scatter(database.Globaltime[-1], Value[-1], ValueY[-1])
                    ax.text(database.Globaltime[-1], Value[-1], ValueY[-1], r"$\Gamma \eta \delta \epsilon$", color='b')

                    ax.set_xlabel("t in s")
                    ax.set_ylabel("x" + r"$_{CM}$")
                    ax.set_zlabel("y" + r"$_{CM}$")

                    ax.plot(database.Globaltime, Value, ValueY, label=(title))
                    ax.set_xlim(database.Globaltime[0], database.Globaltime[-1])
                    ax.set_ylim(0, 1080)
                    ax.set_zlim(0, 600)

                case 3:
                    ax = plt.figure(title).add_subplot()  # eine Plotumgebung wird generiert
                    ax.plot(database.Globaltime, Value, label=(title))
                    ax.set_xlabel("t in s")
                    ax.set_ylabel("mittlerer Geschwindigkeitsbetrag")

                    ax.set_ylim(0, np.sqrt(600 * 600 + 1080 * 1080) / 10)

                case 4:

                    ax = plt.figure(title).add_subplot()  # eine Plotumgebung wird generiert
                    ax.bar(basket, Value, label=(title), width=basksize)
                    ax.set_xlabel("Geschwindigkeitsbetrag")
                    ax.set_ylabel("Anzahl")

                case 5:
                    ax = plt.figure(title).add_subplot()  # eine Plotumgebung wird generiert
                    ax.plot(database.Globaltime, Value, label=(title))
                    ax.set_xlabel("t in s")
                    ax.set_ylabel("Betrag des mittleren Geschwindigkeitsvektors")

                    ax.set_ylim(0, np.sqrt(600 * 600 + 1080 * 1080) / 10)

                case 6:
                    ax = plt.figure(title).add_subplot()  # eine Plotumgebung wird generiert
                    ax.plot(database.Globaltime, Value, label=(title))
                    ax.set_xlabel("t in s")
                    ax.set_ylabel("I(" + r"$t$" + ")= " + r"$ e^{- |\overline{\overrightarrow{v}}|/\overline{v}}} $"
                                                        + r"$- e^{-\overline{v}/|\overline{\overrightarrow{v}}|}$")

                    ax.set_ylim(0, 1)

                case 7:
                    ax = plt.figure(title).add_subplot()  # eine Plotumgebung wird generiert
                    ax.plot(database.Globaltime, Value, label=(title))
                    ax.set_xlabel("t in s")
                    ax.set_ylabel("mittlerer Beschleunigungsbetrag")

                    ax.set_ylim(0, np.sqrt(600 * 600 + 1080 * 1080) / 10)

                case 8:
                    ax = plt.figure(title).add_subplot()  # eine Plotumgebung wird generiert
                    ax.bar(basket, Value, label=(title), width=basksize)
                    ax.set_xlabel("Beschleunigungsbetrag")
                    ax.set_ylabel("Anzahl")

                case 9:
                    ax = plt.figure(title).add_subplot()  # eine Plotumgebung wird generiert
                    ax.plot(database.Globaltime, Value, label=(title))
                    ax.set_xlabel("t in s")
                    ax.set_ylabel("Betrag des mittleren Beschleunigungsvektors")

                    ax.set_ylim(0, np.sqrt(600 * 600 + 1080 * 1080) / 10)

                case 10:
                    ax = plt.figure(title).add_subplot()  # eine Plotumgebung wird generiert
                    ax.plot(database.Globaltime, Value, label=(title))
                    ax.set_xlabel("t in s")
                    ax.set_ylabel("I(" + r"$t$" + ")= " + r"$ e^{- |\overline{\overrightarrow{a}}|/\overline{a}}} $"
                                                        + r"$- e^{-\overline{a}/|\overline{\overrightarrow{a}}|}$")

                    ax.set_ylim(0, 1)
            plt.show()
        else:
            if database.setplot == 12:
                for i in range(len(database.Globaltime)):
                    print( str(database.Globaltime[i]) + "; " + str(Value[i]) + ", " + str(ValueY[i]))

            elif database.setplot == 14 or database.setplot == 18:
                for i in range(len(basket)):
                    print( str( basket[i] - basksize/2) + " - " + str(basket[i] + basksize/2) + "; " + str(Value[i]))

            else:
                    for i in range(len(database.Globaltime)):
                        print(str(database.Globaltime[i]) + "; " + str(Value[i]))

                    #ax.set_ylim(-np.sqrt(600 * 600 + 1080 * 1080)/10, np.sqrt(600 * 600 + 1080 * 1080)/10)


        #filename = title + ".pdf"
        #plt.savefig(filename) #Plot(s) werden gespeichert




