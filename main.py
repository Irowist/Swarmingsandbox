# SciCo Abschlussprojekt "Swarming"
# Universität Potsdam, SS 2023
# @Richard Lehm, @Robert Schulz
# v1.0

if __name__ == '__main__':  # So gehen wir sicher, dass das Programm von hier aus gestartet wird
    # Notwendig für das Programm: pygame, pymunk, matplotlib, numpy
    import pygame     # Für visuelle Ausgabe
    import pymunk     # Für Physik
    from pymunk import Vec2d
    import numpy
    import matplotlib.pyplot as plt

    import random
    import threading                # Für Multithreading
    import sys                      # Für Programmbeendung
    from itertools import combinations #Für Stoßmodelle durch WW
    import numpy as np #Für Spaßige Stoßmodelle

    import database                             # Zugriff auf die globalen Variablen
    from console import start_console               #
    import plots
    from plots import start_plots

    print("main online")

    CONSOLE = threading.Thread(target=start_console)

    CONSOLE.start()

    X, Y = 0, 1
    ### Physics collision types (Nach PyMunk)
    COLLTYPE_DEFAULT = 0
    COLLTYPE_MOUSE = 1
    COLLTYPE_BALL = 2



    def flipy(y):
        """Konvertierung der chipmunk physics zu pygame Koordinaten (Korrigierung einer Abweichung zwischen zwei Paketen)"""
        return -y + 600

    def main():

        pygame.init()
        screen = pygame.display.set_mode((1080, 600))
        clock = pygame.time.Clock()
        running = True

        ### Physics stuff
        space = pymunk.Space()
        attrac = pygame.Vector2(database.endpos) - pygame.Vector2(database.startpos)
        normvec = database.acc * pygame.math.Vector2.normalize(attrac)
        space.gravity = database.acc * normvec.x, database.acc * normvec.y
        handler = space.add_collision_handler(2, 2)

        scaled_screen = pygame.transform.scale(screen, (1080, 600))
        pygame.display.set_mode((1080, 600))

        ## Balls
        balls = []

        ### Static line
        line_point1 = None
        static_lines = []
        run_physics = database.start
        timecounter = 0
        while running:
            if database.end == True:
                print("Simulation wird beendet")
                sys.exit()
            if database.reset == True:
                balls = []
                for line in static_lines:
                    space.remove(line)
                static_lines = []
                print("Simulation reseted")
                database.reset = False

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    database.end = True
                elif event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                    database.end = True
                elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                    if pygame.key.get_mods() & pygame.KMOD_SHIFT:
                        database.endpos = event.pos[X], flipy(event.pos[Y])
                        print(database.endpos)
                    else:
                        balls = []
                        database.Bodies=[]
                        database.Globaltime=[]
                        velrem=[]
                        timecounter = 0
                        database.startpos = event.pos[X], flipy(event.pos[Y])
                        print(database.startpos)
                        px = event.pos[X]
                        py = flipy(event.pos[Y])
                        for j in range(database.num):
                            rnd1 = random.uniform(-2.0, 2.0)
                            rnd2 = random.uniform(-2.0, 2.0)
                            body = pymunk.Body(10, 100)
                            body.position = px + rnd1, py + rnd2
                            shape = pymunk.Circle(body, 10, (0, 0))
                            shape.friction = 0.5
                            shape.collision_type = COLLTYPE_BALL
                            space.add(body, shape)
                            balls.append(shape)
                            database.Bodies.append(database.datahandler(1))
                            velrem.append(Vec2d(0,0))

                elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 3:
                    if line_point1 is None:
                        line_point1 = Vec2d(event.pos[X], flipy(event.pos[Y]))
                elif event.type == pygame.MOUSEBUTTONUP and event.button == 3:
                    if line_point1 is not None:
                        line_point2 = Vec2d(event.pos[X], flipy(event.pos[Y]))
                        shape = pymunk.Segment(
                            space.static_body, line_point1, line_point2, 0.0
                        )
                        shape.friction = 0.99
                        space.add(shape)
                        static_lines.append(shape)
                        line_point1 = None

                elif event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                    if database.colltp < 1:
                        handler.begin = lambda arbiter, space, data: True # aktiviert die pymunkinterne Kollision
                    else:
                        handler.begin = lambda arbiter, space, data: False  # deaktiviert die Kollision
                    run_physics = not run_physics

            p = pygame.mouse.get_pos()
            mouse_pos = Vec2d(p[X], flipy(p[Y]))

            if len(balls) > 0 and run_physics == True:  # Massenmittelpunkt Ort und Geschwindigkeit bestimmen
                sum_x = 0
                sum_y = 0
                sum_vx = 0
                sum_vy = 0
                database.Globaltime.append(timecounter/database.FPS)
                timecounter = timecounter + 1
                for i in range(len(balls)):
                    sum_x += balls[i].body.position.x
                    sum_y += balls[i].body.position.y

                    sum_vx += balls[i].body.velocity.x
                    sum_vy += balls[i].body.velocity.y

                    ##Datenübergabe in die database
                    database.Bodies[i].getdat(balls[i].body.position.x, balls[i].body.position.y,
                                              balls[i].body.velocity.x, balls[i].body.velocity.y,
                                              (balls[i].body.velocity.x - velrem[i].x),
                                              (balls[i].body.velocity.y - velrem[i].y))
                    velrem[i]=Vec2d( balls[i].body.velocity.x, balls[i].body.velocity.x) # hilfsmittel zur Beschleunigungsbestimmung

                center_x = sum_x / len(balls)
                center_y = sum_y / len(balls)
                center_vx = sum_vx / len(balls)
                center_vy = sum_vy / len(balls)

                # Massenmittelpunkt auf Bildschirm malen
                pygame.draw.circle(screen, pygame.Color("black"), [int(center_x), int(flipy(center_y))], 10, 2)

                ### Schreibe Daten auf database
                database.mmp.append(pygame.Vector2(center_x, center_y))
                database.mmpv.append(pygame.Vector2(center_vx, center_vy))

                attrac = pygame.Vector2(database.endpos) - pygame.Vector2(center_x, center_y)
                normvec = database.acc * attrac.normalize()
                space.gravity = normvec.x, normvec.y

                ### Physik auf die Bälle berechnen

                if database.colltp < 0 or database.colltp !=10:    ##Stoßmodelle durch WW
                    for b1, b2 in combinations(balls, 2):
                        match database.colltp:
                            case 1: # ~1/r Abstoßung
                                try:
                                    b1.body.force -= 10*b1.body.mass * b2.body.mass *(b2.body.position - b1.body.position )\
                                                   /((b2.body.position - b1.body.position ).length)**2
                                    b2.body.force -= 100*b1.body.mass * b2.body.mass *(b1.body.position - b2.body.position )\
                                                   /((b2.body.position - b1.body.position ).length)**2
                                except:
                                    b1.body.force += pymunk.Vec2d(0, 0)
                                    b2.body.force += pymunk.Vec2d(0, 0)
                            case 2: # ~1/r**2 Abstoßung
                                try:
                                    b1.body.force -= 10*b1.body.mass * b2.body.mass * (b2.body.position - b1.body.position) \
                                                    / ((b2.body.position - b1.body.position).length) ** 3
                                    b2.body.force -= 10*b1.body.mass * b2.body.mass * (b1.body.position - b2.body.position) \
                                                    / ((b2.body.position - b1.body.position).length) ** 3
                                except:
                                    b1.body.force += pymunk.Vec2d(0, 0)
                                    b2.body.force += pymunk.Vec2d(0, 0)
                            case 3: # ~1/r**3 Abstoßung
                                try:
                                    b1.body.force -= b1.body.mass * b2.body.mass * (b2.body.position - b1.body.position) \
                                                    / ((b2.body.position - b1.body.position).length) ** 4
                                    b2.body.force -= b1.body.mass * b2.body.mass * (b1.body.position - b2.body.position) \
                                                    / ((b2.body.position - b1.body.position).length) ** 4
                                except:
                                    b1.body.force += pymunk.Vec2d(0, 0)
                                    b2.body.force += pymunk.Vec2d(0, 0)
                            case 4: # ~ln(r) Abstoßung und Anziehung
                                try:
                                    b1.body.force +=   b1.body.mass * b2.body.mass * normvec((b2.body.position - b1.body.position))\
                                                    * np.log((b2.body.position - b1.body.position).length/(100* b1.radius))
                                    b2.body.force +=   b1.body.mass * b2.body.mass * normvec((b1.body.position - b2.body.position)) \
                                                    * np.log((b2.body.position - b1.body.position).length/(100* b2.radius))
                                except:
                                    b1.body.force += pymunk.Vec2d(0, 0)
                                    b2.body.force += pymunk.Vec2d(0, 0)
                            case 5:  # ~exp{1/r} Abstoßung
                                try:
                                    b1.body.force -=  b1.body.mass * b2.body.mass * normvec(
                                                b2.body.position - b1.body.position) \
                                                     * np.exp(
                                        1/(b2.body.position - b1.body.position).length -1)
                                    b2.body.force -=  b1.body.mass * b2.body.mass * normvec(
                                                b1.body.position - b2.body.position) \
                                                     * np.exp(
                                        1/(b2.body.position - b1.body.position).length -1)
                                except:
                                    b1.body.force += pymunk.Vec2d(0, 0)
                                    b2.body.force += pymunk.Vec2d(0, 0)

                if database.colltp < 0:  ##Stoßmodelle durch WW
                    for b1, b2 in combinations(balls, 2):
                        match database.colltp:
                            case -1:  # ~1/r Abstoßung
                                try:
                                    b1.body.force -= 10 * b1.body.mass * b2.body.mass * (
                                            b2.body.position - b1.body.position) \
                                                     / ((b2.body.position - b1.body.position).length) ** 2
                                    b2.body.force -= 100 * b1.body.mass * b2.body.mass * (
                                            b1.body.position - b2.body.position) \
                                                     / ((b2.body.position - b1.body.position).length) ** 2
                                except:
                                    b1.body.force += pymunk.Vec2d(0, 0)
                                    b2.body.force += pymunk.Vec2d(0, 0)
                            case -2:  # ~1/r**2 Abstoßung
                                try:
                                    b1.body.force -= 10 * b1.body.mass * b2.body.mass * (
                                            b2.body.position - b1.body.position) \
                                                     / ((b2.body.position - b1.body.position).length) ** 3
                                    b2.body.force -= 10 * b1.body.mass * b2.body.mass * (
                                            b1.body.position - b2.body.position) \
                                                     / ((b2.body.position - b1.body.position).length) ** 3
                                except:
                                    b1.body.force += pymunk.Vec2d(0, 0)
                                    b2.body.force += pymunk.Vec2d(0, 0)
                            case -3:  # ~1/r**3 Abstoßung
                                try:
                                    b1.body.force -= b1.body.mass * b2.body.mass * (
                                            b2.body.position - b1.body.position) \
                                                     / ((b2.body.position - b1.body.position).length) ** 4
                                    b2.body.force -= b1.body.mass * b2.body.mass * (
                                            b1.body.position - b2.body.position) \
                                                     / ((b2.body.position - b1.body.position).length) ** 4
                                except:
                                    b1.body.force += pymunk.Vec2d(0, 0)
                                    b2.body.force += pymunk.Vec2d(0, 0)
                            case -4:  # ~ln(r) Abstoßung und Anziehung
                                try:
                                    b1.body.force += b1.body.mass * b2.body.mass * normvec(
                                        (b2.body.position - b1.body.position)) \
                                                     * np.log(
                                        (b2.body.position - b1.body.position).length / (100 * b1.radius))
                                    b2.body.force += b1.body.mass * b2.body.mass * normvec(
                                        (b1.body.position - b2.body.position)) \
                                                     * np.log(
                                        (b2.body.position - b1.body.position).length / (100 * b2.radius))
                                except:
                                    b1.body.force += pymunk.Vec2d(0, 0)
                                    b2.body.force += pymunk.Vec2d(0, 0)
                            case -5:  # ~exp{1/r} Abstoßung
                                try:
                                    b1.body.force -= b1.body.mass * b2.body.mass * normvec(
                                        b2.body.position - b1.body.position) \
                                                     * np.exp(
                                        1 / (b2.body.position - b1.body.position).length - 1)
                                    b2.body.force -= b1.body.mass * b2.body.mass * normvec(
                                        b1.body.position - b2.body.position) \
                                                     * np.exp(
                                        1 / (b2.body.position - b1.body.position).length - 1)
                                except:
                                    b1.body.force += pymunk.Vec2d(0, 0)
                                    b2.body.force += pymunk.Vec2d(0, 0)

                for ball in balls:
                    rnd1 = random.uniform(- float(database.rndm), float(database.rndm))
                    rnd2 = random.uniform(- float(database.rndm), float(database.rndm))
                    o = ball.body.position.x, ball.body.position.y
                    v = ball.body.velocity
                    ball.body.velocity = ball.body.velocity.x + rnd1, ball.body.velocity.y + rnd2
                    v_length = abs(v.length)

                    if v_length > database.maxv * 10:       # Maximalgeschwindigkeit festgelegt
                        ball.body.velocity = database.maxv * v.normalized()

            ### Update physics
            if run_physics:
                dt = 1.0 / database.FPS
                for x in range(1):
                    space.step(dt)

            if run_physics == False:
                if database.showplot:       ##Hier werden Plots gestartet. Evtl. später Try: Except: hinzufügen
                    print("Plot wird ausgegeben")
                    start_plots()
                    database.showplot = False

            ### Draw stuff
            screen.fill(pygame.Color("white"))

            # Display some text
            font = pygame.font.Font(None, 16)
            text = """
        LMB: set Startposition
        LMB + Shift: set Endposition
        RMB: Drag to create wall, release to finish
        Space: Pause physics simulation"""
            y = 5
            for line in text.splitlines():
                text = font.render(line, True, pygame.Color("black"))
                screen.blit(text, (5, y))
                y += 10

            for ball in balls:
                r = ball.radius
                v = ball.body.position
                rot = ball.body.rotation_vector
                p = int(v.x), int(flipy(v.y))
                p2 = p + Vec2d(rot.x, -rot.y) * r * 0.9
                p2 = int(p2.x), int(p2.y)
                pygame.draw.circle(screen, pygame.Color("blue"), p, int(r), 2)
                pygame.draw.line(screen, pygame.Color("red"), p, p2)

            if line_point1 is not None:
                p1 = int(line_point1.x), int(flipy(line_point1.y))
                p2 = mouse_pos.x, flipy(mouse_pos.y)
                pygame.draw.lines(screen, pygame.Color("black"), False, [p1, p2])

            for line in static_lines:
                body = line.body

                pv1 = body.position + line.a.rotated(body.angle)
                pv2 = body.position + line.b.rotated(body.angle)
                p1 = int(pv1.x), int(flipy(pv1.y))
                p2 = int(pv2.x), int(flipy(pv2.y))
                pygame.draw.lines(screen, pygame.Color("lightgray"), False, [p1, p2])

            ### Flip screen
            pygame.display.flip()
            clock.tick(database.FPS)
            pygame.display.set_caption("fps: " + str(clock.get_fps()))


    main()      # Starten

else:
    import sys  # Für Programmbeendung
    print("Programm muss über main.py gestartet werden")
    print("Scripts werden jetzt beendet")
    sys.exit()