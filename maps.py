# Créé par Paul, le 12/04/2016 en Python 3.2
import pygame #importation de pygame
import traceback #module pour recuperer des infos sur les erreurs
from pygame.locals import * #on importe les constantes de pygame

pygame.init()
class map1():
    class stage1():
        def __init__(self):

            self.background = "Stage 1_1.png"

            self.solRect=pygame.Rect(0,195,800,24)      #Attention la valeur y (2e valeur) est minorée de 5 ! (choix esthetique)
            self.ycharSol = 200-16                      #Position Y du personnage sur la plateforme du sol

            self.p1_1 = pygame.Rect(353,133,92,23)
            self.p1_2 = pygame.Rect(662,133,46,23)
            self.ycharP1_up = 133-15                    #Position Y du personnage sur les plateformes de niveau 1
            self.ycharP1_down = 133+24                  #Position Y du personnage après collision sous les plateformes de niveau 1

            self.collisionsSol = [self.solRect]
            self.collisionsP1 = [self.p1_1,self.p1_2]
            self.collisionsP2 = []


    class stage2():
        def __init__(self):

            self.background = "Stage 1_2.png"

            self.solRect1=pygame.Rect(0,195,286,24)      #Attention la valeur y (2e valeur) est minorée de 5 !
            self.solRect2=pygame.Rect(332,195,243,24)
            self.solRect3=pygame.Rect(621,195,179,24)
            self.ycharSol = 200-16

            self.p1_1 = pygame.Rect(274,133,92,23)
            self.p1_2 = pygame.Rect(535,133,46,23)
            self.ycharP1_up = 133-15
            self.ycharP1_down = 133+24


            self.p2_1 = pygame.Rect(581,77,46,23)
            self.ycharP2_up = 77-15                     #Position Y du personnage sur les plateformes de niveau 2
            self.ycharP2_down = 77+24                   #Position Y du personnage après collision sur les plateformes de niveau 2


            self.collisionsSol = [self.solRect1,self.solRect2,self.solRect3]
            self.collisionsP1 = [self.p1_1,self.p1_2]
            self.collisionsP2 = [self.p2_1]

    class stage3():
        def __init__(self):

            self.background = "Stage 1_3.png"

            self.solRect1=pygame.Rect(0,195,202,24)      #Attention la valeur y (2e valeur) est minorée de 5 !
            self.solRect2=pygame.Rect(294,195,280,24)
            self.solRect3=pygame.Rect(602,195,203,24)
            self.ycharSol = 200-16

            self.p1_1 = pygame.Rect(151,133,184,23)
            self.ycharP1_up = 133-15
            self.ycharP1_down = 133+24


            self.collisionsSol = [self.solRect1,self.solRect2,self.solRect3]
            self.collisionsP1 = [self.p1_1]
            self.collisionsP2 = []

    class stage4():
        def __init__(self):

            self.background = "Stage 1_4.png"

            self.solRect1=pygame.Rect(0,195,61,24)      #Attention la valeur y (2e valeur) est minorée de 5 !
            self.solRect2=pygame.Rect(87,195,63,24)
            self.solRect3=pygame.Rect(176,195,50,24)
            self.solRect4=pygame.Rect(252,195,31,24)
            self.solRect5=pygame.Rect(311,195,494,24)

            self.ycharSol = 200-16

            self.p1_1 = pygame.Rect(387,133,92,23)
            self.p1_2 = pygame.Rect(525,133,92,23)
            self.ycharP1_up = 133-15
            self.ycharP1_down = 133+24


            self.p2_1 = pygame.Rect(457,77,92,23)
            self.ycharP2_up = 77-15
            self.ycharP2_down = 77+24


            self.collisionsSol = [self.solRect1,self.solRect2,self.solRect3,self.solRect4,self.solRect5]
            self.collisionsP1 = [self.p1_1,self.p1_2]
            self.collisionsP2 = [self.p2_1]

    class stage5():
        def __init__(self):

            self.background = "Stage 1_5.png"

            self.solRect=pygame.Rect(0,195,800,24)      #Attention la valeur y (2e valeur) est minorée de 5 !
            self.ycharSol = 200-16

            self.p1_1 = pygame.Rect(56,133,92,23)
            self.p1_2 = pygame.Rect(171,133,46,23)
            self.p1_3 = pygame.Rect(240,133,69,23)
            self.ycharP1_up = 133-15
            self.ycharP1_down = 133+24


            self.collisionsSol = [self.solRect]
            self.collisionsP1 = [self.p1_1,self.p1_2,self.p1_3]
            self.collisionsP2 = []

class map2():
    class stage1():
        def __init__(self):

            self.background = "Stage 2_1.png"

            self.solRect1=pygame.Rect(0,195,79,24)      #Attention la valeur y (2e valeur) est minorée de 5 !
            self.solRect2=pygame.Rect(309,195,134,24)
            self.solRect3=pygame.Rect(489,195,130,24)
            self.solRect4=pygame.Rect(665,195,135,24)
            self.ycharSol = 200-16

            self.p1_1 = pygame.Rect(102,133,92,23)
            self.ycharP1_up = 133-15
            self.ycharP1_down = 133+24

            self.p2_1 = pygame.Rect(217,77,92,23)
            self.ycharP2_up = 77-15
            self.ycharP2_down = 77+24


            self.collisionsSol = [self.solRect1,self.solRect2,self.solRect3,self.solRect4]
            self.collisionsP1 = [self.p1_1]
            self.collisionsP2 = [self.p2_1]

    class stage2():
        def __init__(self):

            self.background = "Stage 2_2.png"

            self.solRect1=pygame.Rect(0,195,189,24)      #Attention la valeur y (2e valeur) est minorée de 5 !
            self.solRect2=pygame.Rect(603,195,197,24)
            self.ycharSol = 200-16

            self.p1_1 = pygame.Rect(222,133,92,23)
            self.p1_2 = pygame.Rect(472,133,92,23)

            self.ycharP1_up = 133-15
            self.ycharP1_down = 133+24

            self.p2_1 = pygame.Rect(347,77,92,23)
            self.ycharP2_up = 77-15
            self.ycharP2_down = 77+24


            self.collisionsSol = [self.solRect1,self.solRect2]
            self.collisionsP1 = [self.p1_1,self.p1_2]
            self.collisionsP2 = [self.p2_1]

    class stage3():
        def __init__(self):

            self.background = "Stage 2_3.png"

            self.solRect1=pygame.Rect(0,195,50,24)      #Attention la valeur y (2e valeur) est minorée de 5 !
            self.solRect2=pygame.Rect(96,195,23,24)
            self.solRect3=pygame.Rect(165,195,23,24)
            self.solRect4=pygame.Rect(234,195,23,24)
            self.solRect5=pygame.Rect(303,195,23,24)
            self.solRect6=pygame.Rect(372,195,23,24)
            self.solRect7=pygame.Rect(441,195,23,24)
            self.solRect8=pygame.Rect(510,195,23,24)
            self.solRect9=pygame.Rect(579,195,23,24)
            self.solRect10=pygame.Rect(648,195,23,24)
            self.solRect11=pygame.Rect(717,195,83,24)
            self.ycharSol = 200-16


            self.collisionsSol = [self.solRect1,self.solRect2,self.solRect3,self.solRect4,self.solRect5,self.solRect6,
                                    self.solRect7,self.solRect8,self.solRect9,self.solRect10,self.solRect11]
            self.collisionsP1 = []
            self.collisionsP2 = []

    class stage4():
        def __init__(self):

            self.background = "Stage 2_4.png"

            self.solRect1=pygame.Rect(0,195,800,24)      #Attention la valeur y (2e valeur) est minorée de 5 !

            self.ycharSol = 200-16

            self.p1_1 = pygame.Rect(131,133,368,23)
            self.ycharP1_up = 133-15
            self.ycharP1_down = 133+24

            self.p2_1 = pygame.Rect(267,77,92,23)
            self.p2_2 = pygame.Rect(560,77,92,23)
            self.ycharP2_up = 77-15
            self.ycharP2_down = 77+24


            self.collisionsSol = [self.solRect1]
            self.collisionsP1 = [self.p1_1]
            self.collisionsP2 = [self.p2_1,self.p2_2]

    class stage5():
        def __init__(self):

            self.background = "Stage 2_5.png"

            self.solRect1=pygame.Rect(0,195,29,24)      #Attention la valeur y (2e valeur) est minorée de 5 !
            self.solRect2=pygame.Rect(75,195,23,24)
            self.solRect3=pygame.Rect(461,195,339,24)
            self.ycharSol = 200-16

            self.p1_1 = pygame.Rect(115,133,46,23)
            self.p1_2 = pygame.Rect(207,133,92,23)
            self.ycharP1_up = 133-15
            self.ycharP1_down = 133+24

            self.p2_1 = pygame.Rect(346,77,92,23)
            self.ycharP2_up = 77-15
            self.ycharP2_down = 77+24


            self.collisionsSol = [self.solRect1,self.solRect2,self.solRect3]
            self.collisionsP1 = [self.p1_1,self.p1_2]
            self.collisionsP2 = [self.p2_1]

class map3():
    class stage1():
        def __init__(self):

            self.background = "Stage 3_1.png"

            self.solRect1=pygame.Rect(0,195,23,24)      #Attention la valeur y (2e valeur) est minorée de 5 !
            self.solRect2=pygame.Rect(777,195,23,24)

            self.ycharSol = 200-16

            self.p1_1 = pygame.Rect(46,133,181,23)
            self.p1_2 = pygame.Rect(253,133,184,23)
            self.p1_3 = pygame.Rect(465,133,299,23)
            self.ycharP1_up = 133-15
            self.ycharP1_down = 133+24



            self.collisionsSol = [self.solRect1,self.solRect2]
            self.collisionsP1 = [self.p1_1,self.p1_2,self.p1_3]
            self.collisionsP2 = []

    class stage2():
        def __init__(self):

            self.background = "Stage 3_2.png"

            self.solRect1=pygame.Rect(0,195,23,24)      #Attention la valeur y (2e valeur) est minorée de 5 !
            self.solRect2=pygame.Rect(777,195,23,24)
            self.ycharSol = 200-16

            self.p1_1 = pygame.Rect(52,133,92,23)
            self.p1_2 = pygame.Rect(282,133,92,23)
            self.p1_3 = pygame.Rect(489,133,161,23)

            self.ycharP1_up = 133-15
            self.ycharP1_down = 133+24

            self.p2_1 = pygame.Rect(121,77,184,23)
            self.p2_2 = pygame.Rect(397,77,46,23)
            self.p2_3 = pygame.Rect(696,77,46,23)
            self.ycharP2_up = 77-15
            self.ycharP2_down = 77+24


            self.collisionsSol = [self.solRect1,self.solRect2]
            self.collisionsP1 = [self.p1_1,self.p1_2,self.p1_3]
            self.collisionsP2 = [self.p2_1,self.p2_2,self.p2_3]

    class stage3():
        def __init__(self):

            self.background = "Stage 3_3.png"

            self.solRect1=pygame.Rect(0,195,23,24)      #Attention la valeur y (2e valeur) est minorée de 5 !
            self.solRect2=pygame.Rect(777,195,23,24)
            self.ycharSol = 200-16

            self.p1_1 = pygame.Rect(53,133,23,23)
            self.p1_3 = pygame.Rect(155,133,3,23)
            self.p1_5 = pygame.Rect(237,133,23,23)
            self.p1_7 = pygame.Rect(352,133,46,23)
            self.p1_8 = pygame.Rect(444,133,46,23)
            self.p1_9 = pygame.Rect(536,133,46,23)
            self.p1_10 = pygame.Rect(628,133,92,23)
            self.ycharP1_up = 133-15
            self.ycharP1_down = 133+24


            self.collisionsSol = [self.solRect1,self.solRect2]
            self.collisionsP1 = [self.p1_1,self.p1_3,self.p1_5,self.p1_7,self.p1_8,self.p1_9,self.p1_10]
            self.collisionsP2 = []

    class stage4():
        def __init__(self):

            self.background = "Stage 3_4.png"

            self.solRect1=pygame.Rect(0,195,115,24)      #Attention la valeur y (2e valeur) est minorée de 5 !
            self.solRect2=pygame.Rect(685,195,115,24)

            self.ycharSol = 200-16

            self.p1_1 = pygame.Rect(138,133,138,23)
            self.p1_2 = pygame.Rect(414,133,115,23)
            self.ycharP1_up = 133-15
            self.ycharP1_down = 133+24

            self.p2_1 = pygame.Rect(299,77,92,23)
            self.p2_2 = pygame.Rect(552,77,92,23)
            self.ycharP2_up = 77-15
            self.ycharP2_down = 77+24


            self.collisionsSol = [self.solRect1,self.solRect2]
            self.collisionsP1 = [self.p1_1,self.p1_2]
            self.collisionsP2 = [self.p2_1,self.p2_2]

    class stage5():
        def __init__(self):

            self.background = "Stage 3_5.png"

            self.solRect1=pygame.Rect(0,195,23,24)      #Attention la valeur y (2e valeur) est minorée de 5 !
            self.solRect2=pygame.Rect(616,195,184,24)

            self.ycharSol = 200-16

            self.p1_1 = pygame.Rect(46,133,23,23)
            self.p1_2 = pygame.Rect(138,133,23,23)
            self.p1_3 = pygame.Rect(345,133,138,23)
            self.p1_4 = pygame.Rect(552,133,23,23)
            self.ycharP1_up = 133-15
            self.ycharP1_down = 133+24

            self.p2_1 = pygame.Rect(92,77,23,23)
            self.p2_2 = pygame.Rect(184,77,138,23)
            self.p2_3 = pygame.Rect(506,77,23,23)
            self.ycharP2_up = 77-15
            self.ycharP2_down = 77+24


            self.collisionsSol = [self.solRect1,self.solRect2]
            self.collisionsP1 = [self.p1_1,self.p1_2,self.p1_3,self.p1_4]
            self.collisionsP2 = [self.p2_1,self.p2_2,self.p2_3]