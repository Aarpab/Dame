import pygame
import sys

pygame.init()
screen = pygame.display.set_mode([944, 944])

font = pygame.font.SysFont("arialblack", 35)

class Figur :
    def __init__(self, x, y, farbe) :
        self.x = x
        self.y = y
        self.farbe = farbe
        self.dame = False
        self.geschlagen = False

    def figur_zeichnen(self) :
        pygame.draw.circle(screen, self.farbe, (self.x + 59, self.y + 59), 25)

        if self.dame :
            if self.farbe == (0, 0, 0) :
                text = font.render("D", True, (255, 255, 255))
            else :
                text = font.render("D", True, (0, 0, 0))

            text_Grund, text_Kasten = text, text.get_rect()
            text_Kasten.center = ((self.x + 59, self.y + 59))
            screen.blit(text_Grund, text_Kasten)

def felder_möglich_schlagen(figur) :
    felder_liste = []

    if figur.farbe == (0, 0, 0) :
        x = figur.x - 118
        y = figur.y + 118

        for feld in felder :
            if feld[0] == x and feld[1] == y :
                for f in figuren :
                    if f.x == x and f.y == y :
                        if f.farbe != figur.farbe :
                            for feld2 in felder :
                                if feld2[0] == x - 118 and feld2[1] == y + 118 :
                                    frei = True

                                    for f2 in figuren :
                                        if f2.x == feld2[0] and f2.y == feld2[1] :
                                            frei = False

                                    if frei :
                                        felder_liste.append(feld2)
                                        break
        
        x = figur.x + 118
        y = figur.y + 118

        for feld in felder :
            if feld[0] == x and feld[1] == y :
                for f in figuren :
                    if f.x == x and f.y == y :
                        if f.farbe != figur.farbe :
                            for feld2 in felder :
                                if feld2[0] == x + 118 and feld2[1] == y + 118 :
                                    frei = True

                                    for f2 in figuren :
                                        if f2.x == feld2[0] and f2.y == feld2[1] :
                                            frei = False

                                    if frei :
                                        felder_liste.append(feld2)
                                        break

    else :
        x = figur.x - 118
        y = figur.y - 118

        for feld in felder :
            if feld[0] == x and feld[1] == y :
                for f in figuren :
                    if f.x == x and f.y == y :
                        if f.farbe != figur.farbe :
                            for feld2 in felder :
                                if feld2[0] == x - 118 and feld2[1] == y - 118 :
                                    frei = True

                                    for f2 in figuren :
                                        if f2.x == feld2[0] and f2.y == feld2[1] :
                                            frei = False
                                    
                                    if frei :
                                        felder_liste.append(feld2)
                                        break
        
        x = figur.x + 118
        y = figur.y - 118

        for feld in felder :
            if feld[0] == x and feld[1] == y :
                for f in figuren :
                    if f.x == x and f.y == y :
                        if f.farbe != figur.farbe :
                            for feld2 in felder :
                                if feld2[0] == x + 118 and feld2[1] == y - 118 :
                                    frei = True

                                    for f2 in figuren :
                                        if f2.x == feld2[0] and f2.y == feld2[1] :
                                            frei = False

                                    if frei :
                                        felder_liste.append(feld2)
                                        break
    
    return felder_liste

def felder_möglich(figur) :
    möglich = []

    if figur.farbe == (255, 255, 255) :
        x = figur.x - 118
        y = figur.y - 118

        for feld in felder :
            if feld[0] == x and feld[1] == y :
                frei = True

                for f in figuren :
                    if f.x == x and f.y == y :
                        frei = False
                
                if frei :
                    möglich.append(feld)
                    break
        
        x = figur.x + 118
        y = figur.y - 118

        for feld in felder :
            if feld[0] == x and feld[1] == y :
                frei = True

                for f in figuren :
                    if f.x == x and f.y == y :
                        frei = False
                
                if frei :
                    möglich.append(feld)
                    break
    
    else :
        x = figur.x - 118
        y = figur.y + 118

        for feld in felder :
            if feld[0] == x and feld[1] == y :
                frei = True

                for f in figuren :
                    if f.x == x and f.y == y :
                        frei = False
                
                if frei :
                    möglich.append(feld)
                    break
        
        x = figur.x + 118
        y = figur.y + 118

        for feld in felder :
            if feld[0] == x and feld[1] == y :
                frei = True

                for f in figuren :
                    if f.x == x and f.y == y :
                        frei = False
                
                if frei :
                    möglich.append(feld)
                    break

    schlagen = felder_möglich_schlagen(figur)

    if schlagen != [] :
        return schlagen
    else :
        for f in figuren :
            if f.farbe == figur.farbe :
                if not f.dame :
                    if felder_möglich_schlagen(f) != [] :
                        return []
                else :
                    if felder_möglich_dame(f, True) :
                        return []

        return möglich

def felder_möglich_dame(figur, schlagen_bool=False) :
    möglich = []
    schlagen = []

    x = figur.x + 118
    y = figur.y - 118

    go2 = True
    while x < 944 and y >= 0 and go2 :
        for feld in felder :
            if feld[0] == x and feld[1] == y :
                frei = True

                for f in figuren :
                    if f.x == x and f.y == y :
                        if f.farbe != figur.farbe :
                            frei = False

                            for feld2 in felder :
                                if feld2[0] == x + 118 and feld2[1] == y - 118 :
                                    frei2 = True

                                    for figur2 in figuren :
                                        if figur2.x == feld2[0] and figur2.y == feld2[1] :
                                            frei2 = False
                                            go2 = False
                                            break

                                    if frei2 :
                                        schlagen.append(feld2)
                                        frei = False
                                        go2 = False
                                        break
                        
                        else :
                            frei = False
            
                if frei :
                    möglich.append(feld)
        
        x += 118
        y -= 118
    
    x = figur.x + 118
    y = figur.y + 118

    go2 = True
    while x < 944 and y < 944 and go2 :
        for feld in felder :
            if feld[0] == x and feld[1] == y :
                frei = True

                for f in figuren :
                    if f.x == x and f.y == y :
                        if f.farbe != figur.farbe :
                            frei = False

                            for feld2 in felder :
                                if feld2[0] == x + 118 and feld2[1] == y + 118 :
                                    frei2 = True

                                    for figur2 in figuren :
                                        if figur2.x == feld2[0] and figur2.y == feld2[1] :
                                            frei2 = False
                                            go2 = False
                                            break

                                    if frei2 :
                                        schlagen.append(feld2)
                                        frei = False
                                        go2 = False
                                        break
                        
                        else :
                            frei = False
            
                if frei :
                    möglich.append(feld)
        
        x += 118
        y += 118

    x = figur.x - 118
    y = figur.y + 118

    go2 = True
    while x >= 0 and y < 944 and go2 :
        for feld in felder :
            if feld[0] == x and feld[1] == y :
                frei = True

                for f in figuren :
                    if f.x == x and f.y == y :
                        if f.farbe != figur.farbe :
                            frei = False

                            for feld2 in felder :
                                if feld2[0] == x - 118 and feld2[1] == y + 118 :
                                    frei2 = True

                                    for figur2 in figuren :
                                        if figur2.x == feld2[0] and figur2.y == feld2[1] :
                                            frei2 = False
                                            go2 = False
                                            break

                                    if frei2 :
                                        schlagen.append(feld2)
                                        frei = False
                                        go2 = False
                                        break
                        
                        else :
                            frei = False
            
                if frei :
                    möglich.append(feld)
        
        x -= 118
        y += 118

    x = figur.x - 118
    y = figur.y - 118

    go2 = True
    while x >= 0 and y < 944 and go :
        for feld in felder :
            if feld[0] == x and feld[1] == y :
                frei = True

                for f in figuren :
                    if f.x == x and f.y == y :
                        if f.farbe != figur.farbe :
                            frei = False

                            for feld2 in felder :
                                if feld2[0] == x - 118 and feld2[1] == y - 118 :
                                    frei2 = True

                                    for figur2 in figuren :
                                        if figur2.x == feld2[0] and figur2.y == feld2[1] :
                                            frei2 = False
                                            go2 = False
                                            break

                                    if frei2 :
                                        schlagen.append(feld2)
                                        frei = False
                                        go2 = False
                                        break
                        
                        else :
                            frei = False
            
                if frei :
                    möglich.append(feld)
        
        x -= 118
        y -= 118

    if schlagen_bool and schlagen != [] :
        return True
    
    elif schlagen_bool and schlagen == [] :
        return False
    
    if schlagen != [] :
        return schlagen
    else :
        for f in figuren :
            if f.farbe == figur.farbe :
                if not f.dame :
                    if felder_möglich_schlagen(f) != [] :
                        return []
                else :
                    if felder_möglich_dame(f, True) :
                        return []

        return möglich

def gewonnen() :
    verloren = True

    if amZug == 1 :
        for figur in figuren :
            if figur.farbe == (0, 0, 0) :
                if not figur.dame :
                    if felder_möglich(figur) != [] :
                        verloren = False
                        break
                else :
                    if felder_möglich_dame(figur) != [] :
                        verloren = False
                        break

        if verloren :
            text = font.render("Weiß hat gewonnen!", True, (0, 0, 255))

            text_Grund, text_Kasten = text, text.get_rect()
            text_Kasten.center = ((472, 472))
            screen.blit(text_Grund, text_Kasten)

            pygame.display.update()
            pygame.time.wait(500)

            while True :
                for event in pygame.event.get() :
                    if event.type == pygame.QUIT: sys.exit()

                gedrückt = pygame.key.get_pressed() + pygame.mouse.get_pressed()

                for i in gedrückt :
                    if i :
                        sys.exit()
    
    else :
        for figur in figuren :
            if figur.farbe == (255, 255, 255) :
                if not figur.dame :
                    if felder_möglich(figur) != [] :
                        verloren = False
                        break
                else :
                    if felder_möglich_dame(figur) != [] :
                        verloren = False
                        break
                        
        if verloren :
            text = font.render("Schwarz hat gewonnen!", True, (0, 0, 255))

            text_Grund, text_Kasten = text, text.get_rect()
            text_Kasten.center = ((472, 472))
            screen.blit(text_Grund, text_Kasten)

            pygame.display.update()
            pygame.time.wait(500)

            while True :
                for event in pygame.event.get() :
                    if event.type == pygame.QUIT: sys.exit()

                gedrückt = pygame.key.get_pressed() + pygame.mouse.get_pressed()

                for i in gedrückt :
                    if i :
                        sys.exit()

def ziehen(pos) :
    global amZug

    for feld in felder :
        if pos[0] < feld[0] + 118 and pos[0] > feld[0] and pos[1] < feld[1] + 118 and pos[1] > feld[1] :
            for figur in figuren :
                if figur.x == feld[0] and figur.y == feld[1] :
                    if figur.farbe == (0, 0, 0) and amZug == 1 or figur.farbe == (255, 255, 255) and amZug == 2 :
                        stop = False
                        for f in figuren :
                            if f.geschlagen and f != figur :
                                stop = True
                                break

                        if stop :
                            break

                        pygame.time.wait(500)

                        if figur.dame :
                            möglich = felder_möglich_dame(figur)
                        else :
                            möglich = felder_möglich(figur)

                        for feld_möglich in möglich :
                            pygame.draw.circle(screen, (0, 255, 0), (feld_möglich[0] + 59, feld_möglich[1] + 59), 15)

                        pygame.draw.rect(screen, (150, 150, 0), (figur.x, figur.y, 118, 118))
                        figur.figur_zeichnen()

                        pygame.display.update()

                        go2 = True
                        while go2 :
                            for event in pygame.event.get() :
                                if event.type == pygame.QUIT: sys.exit()

                            maus = pygame.mouse.get_pressed()

                            if maus[0] :
                                pos2 = pygame.mouse.get_pos()

                                for feld in felder :
                                    if feld in möglich :
                                        if pos2[0] < feld[0] + 118 and pos2[0] > feld[0] and pos2[1] < feld[1] + 118 and pos2[1] > feld[1] :
                                            geschlagen = False
                                            figur.geschlagen = False

                                            for f in figuren :
                                                if f.x < figur.x and f.x > feld[0] and f.y < figur.y and f.y > feld[1] or f.x > figur.x and f.x < feld[0] and f.y < figur.y and f.y > feld[1] or f.x < figur.x and f.x > feld[0] and f.y > figur.y and f.y < feld[1] or f.x > figur.x and f.x < feld[0] and f.y > figur.y and f.y < feld[1] :
                                                    geschlagen = True
                                                    figuren.remove(f)

                                            figur.x = feld[0]
                                            figur.y = feld[1]
                                            go2 = False

                                            if figur.farbe == (0, 0, 0) and figur.y == 826 or figur.farbe == (255, 255, 255) and figur.y == 0 :
                                                figur.dame = True

                                            nochmal = False

                                            if geschlagen :
                                                if felder_möglich_schlagen(figur) != [] :
                                                    nochmal = True
                                                    figur.geschlagen = True

                                            if not nochmal :
                                                if amZug == 1 :
                                                    amZug = 2
                                                else :
                                                    amZug = 1

                                            gewonnen()

                                            pygame.time.wait(500)
                                            break

                            elif maus[2] :
                                go2 = False

def zeichnen() :
    for feld in felder :
        pygame.draw.rect(screen, feld[2], (feld[0], feld[1], 118, 118))

    for figur in figuren :
        figur.figur_zeichnen()

#Felder erstellen

felder = []

x = 0
y = 0

farbe = (245, 245, 245)

while y < 944 :
    felder.append([x, y, farbe])

    x += 118

    if x == 944 :
        x = 0
        y += 118
    else :
        if farbe == (245, 245, 245) :
            farbe = (139, 69, 19)
        else :
            farbe = (245, 245, 245)

#Figuren erstellen

figuren = []

farbe = (0, 0, 0)

x = 118
y = 0

for i in range(24) :
    figuren.append(Figur(x, y, farbe))

    x += 236

    if x == 1062 :
        x = 0
        y += 118

    elif x == 944 :
        x = 118
        y += 118

    if i == 11 :
        x = 0
        y = 590

        farbe = (255, 255, 255)

amZug = 1

go = True
while go :
    for event in pygame.event.get() :
        if event.type == pygame.QUIT: sys.exit()

    maus = pygame.mouse.get_pressed()

    if maus[0] :
        pos = pygame.mouse.get_pos()

        ziehen(pos)

    zeichnen()

    pygame.display.update()