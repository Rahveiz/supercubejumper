#Super Cube Jumper
#Python 3.X
#HENG Paul et FAESSEL Corentin

import pygame #importation de pygame
import traceback #module pour recuperer des infos sur les erreurs
from pygame.locals import * #on importe les constantes de pygame
import time
from maps import *
from random import shuffle, randint


#on definit une variable pour le mode de jeu
mode = "easy"


pygame.init() #on lance pygame

#on charge la police en 2 tailles
texte_pix = pygame.font.Font("hachicro.TTF", 40) #polices
texte_pix_s = pygame.font.Font("hachicro.TTF", 20)

clock=pygame.time.Clock()

def image(chaine):
    """fonctions qui charge les sprites"""
    im=pygame.image.load(chaine)
    return im

##########################################################################################
#fonction credits / fin du jeu
def f_credits(credits_img):
    global menu
    fenetre.blit(credits_img,(0,0)) #on blit l'image des credits
    continuer = 0
    while menu == False: #tant que le menu n'est pas "actif"
        pygame.display.flip() #on met à jour l'ecran
        for event in pygame.event.get():
            if event.type == KEYDOWN: #si on appuie sur espace, on retourne au menu
                if event.key == K_SPACE:
                    menu = True
##########################################################################################


##########################################################################################
#fonction menu
def menu():
    global menu
    menu = True #menu actif
    pygame.mixer.music.load("Nova.mp3") #on charge la musique
    pygame.mixer.music.play(-1,0.0) #la musique est jouee en boucle

    while menu:
        global continuer
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        fenetre.fill((192,192,192)) #on remplit le fond avec une couleur

#titre et position du titre
        text = image("bill.png")
        textpos = text.get_rect(centerx=fenetre.get_width()/2, centery=fenetre.get_height()/2 - 30)
        fenetre.blit(text, textpos)

#affichage de boutons-fonction pour lancer le jeu, afficher les credits et selectionner le mode de jeu (gamemode)
        bouton("Start",60,160,110,50,(0,150,0),(0,240,0),"jouer")
        bouton("Credits",570,150,140,50,(123,184,231),(102,202,145),"credits")
        gamemode(310,160,150,50)

        pygame.display.flip() #mise a jour de l'image affichee
        clock.tick(60)
##########################################################################################

######################################################################################
def bouton(texte,x,y,w,h,inactif,actif,action): #arguments pour la taille, les couleurs et l'action
    global menu, continuer
    action = action

    souris=pygame.mouse.get_pos() #detection de la position de la souris
    click=pygame.mouse.get_pressed() #detection des clics



    if x+w > souris[0] > x and y+h > souris[1] > y: #si le curseur se situe sur le rectangle
        pygame.draw.rect(fenetre,actif,(x,y,w,h)) #on affiche le rectangle d'une couleur
        if click[0] == 1:
            if action == "jouer":
                continuer = 1 #on va a la boucle du jeu
                menu = False #menu inactif
            if action == "credits":
                credits_img = image("Credits.png") #on charge l'image des credits
                menu = False #menu inactif
                f_credits(credits_img) #fonction credits

    else:
        pygame.draw.rect(fenetre,inactif,(x,y,w,h)) #sans le curseur, la couleur est differente

    police = texte_pix_s #chargement de la police
    texte = police.render(texte, 1, (10,10,10))
    textePos = texte.get_rect(centerx=x+(w/2), centery=y+(h/2))
    fenetre.blit(texte,textePos)

#######################################################################################
def gamemode(x,y,w,h):
    global mode

    souris=pygame.mouse.get_pos()
    click=pygame.mouse.get_pressed()


    if x+w > souris[0] > x and y+h > souris[1] > y: #curseur sur le bouton
        if click[0] == 1: #clic gauche
            if mode == "easy": #changement du mode
                mode = "medium"
                time.sleep(0.2)
            elif mode == "medium":
                mode = "hard"
                time.sleep(0.2)
            elif mode == "hard":
                mode = "insane"
                time.sleep(0.2)
            elif mode == "insane":
                mode = "easy"
                time.sleep(0.2)


    police = texte_pix_s
    texte = police.render(mode, 1, (10,10,10))
    textePos = texte.get_rect(centerx=x+(w/2), centery=y+(h/2))
    fenetre.blit(texte,textePos)
##########################################################################################




##########################################################################################
def detectCollisions(liste):    #fonction de detection de collisions entre 2 rectangles, retourne la valeur -1 s'il n'y a pas de collisions
    if player.pos.collidelist(liste) == -1:
        Collisions = False
    else:
        Collisions = True
    return Collisions
##########################################################################################


#on definit une classe avec toutes les donnees sur le personnage
class player(pygame.sprite.Sprite):
    def __init__(self,x,y): #initialisation
        self.pos = pygame.Rect(x,y,16,16) #rectangle correspondant a la position
        self.sol=False #le personnage est au sol
        self.skin = image("carre1.png")
        self.stateRight = True #le personnage est tourne vers la droite
        self.velocite = 0 #variable influant sur l'axe y

    def moveLeft(self,X): #fonctions de deplacement lateral
        self.pos.x -= X
    def moveRight(self,X):
        self.pos.x += X

    def pesanteur (self,gravite):
        if detectCollisions(currentMap.collisionsSol) == False or detectCollisions(currentMap.collisionsP1) == False or detectCollisions(currentMap.collisionsP2) == False:
            self.velocite +=gravite #on diminue la velocite si le personnage n'est pas en collision avec une plateforme
        self.pos.y -=self.velocite #on modifie la position y selon la velocite

    def saut(self):
        if detectCollisions(currentMap.collisionsSol) == True or detectCollisions(currentMap.collisionsP1) == True or detectCollisions(currentMap.collisionsP2) == True:
            self.velocite = 10 #on augmente la velocite donc la position y va augmenter



    def rendu (self,gravite):
        if detectCollisions(currentMap.collisionsSol) == True and self.velocite != 10: #on arrete le mouvement y quand le personnage entre en collision
            self.velocite = 0                                               #avec le saut
            self.pos.y = currentMap.ycharSol
        if detectCollisions(currentMap.collisionsP1) == True and self.velocite != 10:
            self.velocite = 0
            if self.downward == True:
                self.pos.y = currentMap.ycharP1_up
            else :
                self.pos.y = currentMap.ycharP1_down
        if detectCollisions(currentMap.collisionsP2) == True and self.velocite != 10:
            self.velocite = 0
            if self.downward == True:
                self.pos.y = currentMap.ycharP2_up
            else :
                self.pos.y = currentMap.ycharP2_down
        self.pesanteur(gravite)
        fenetre.blit(self.skin,self.pos)





#toujours encadrer vos programmes pygame par try et finally ce qui permet de fermer correctement la fenetre pygame en cas d'erreur

try:
    #creation d'une fenetre
    fenetre=pygame.display.set_mode((800,224))#fenetre de taille 800*600
    pygame.display.set_caption("Super Cube Jumper")
    continuer=0
    menu()
    if continuer == 1:
        pygame.mixer.music.load("We Don't Know.mp3") #changement de musique
        bgm = False


    #personnage
    player=player(100,120)

    #liste des fonds de maps
    background_list =[
    "Stage 1_1.png","Stage 1_2.png","Stage 1_3.png","Stage 1_4.png","Stage 1_5.png",
    "Stage 2_1.png","Stage 2_2.png","Stage 2_3.png","Stage 2_4.png","Stage 2_5.png",
    "Stage 3_1.png","Stage 3_2.png","Stage 3_3.png","Stage 3_4.png","Stage 3_5.png"]

    #liste des maps (fond + collisions)
    listMaps = [
    map1.stage1(),map1.stage2(),map1.stage3(),map1.stage4(),map1.stage5(),
    map2.stage1(),map2.stage2(),map2.stage3(),map2.stage4(),map2.stage5(),
    map3.stage1(),map3.stage2(),map3.stage3(),map3.stage4(),map3.stage5()]

    if mode=="insane":  #en mode insane, on melange aleatoirement les maps
        shuffle(listMaps)
    currentMap = listMaps[0]


    #rectangles de collisions
    rightWall=pygame.Rect(799,0,1,244)
    leftWall=pygame.Rect(0,0,1,244)
    #listes de collisions
    collisions = [leftWall,rightWall]
    endMap = [rightWall]
    gravite = -0.5 #on definit une valeur pour la gravite (negative)





    #boucle perpetuelle qui permet de garder la fenetre ouverte
    pygame.key.set_repeat(1,20)     #permet de repeter les evenements KEYDOWN tant que la touche est enfoncee
    while continuer != 0:
        for event in pygame.event.get():
            #pygame prend le premier evenement de la file
            if event.type==QUIT: #l'evenement QUIT correspond au clic sur la croix
                continuer=False #permet de quitter la boucle

            elif event.type==KEYDOWN:

                if detectCollisions(collisions) == True:
                    if player.stateRight == True:   #le personnage est tourne vers la droite
                        if detectCollisions(endMap) == True: #collision avec le mur de droite
                            if continuer <= 14:
                                currentMap = listMaps[continuer]
                            continuer = continuer +1

                            if continuer == 16: #fin du jeu / arrivee
                                endgame = image("endgame.png")
                                credits_img = image ("Credits.png")
                                timeout = time.time() + 10 #temps + 10sec
                                continuer = 0
                                fenetre.blit(endgame,(0,0))
                                while time.time() < timeout: #timer de 10sec
                                    pygame.display.flip()
                                f_credits(credits_img)
                            player.pos.x = 2 #replacement du personnage
                            player.pos.y = currentMap.ycharSol

                            if continuer == 6: #changement de niveau
                                pygame.mixer.music.load("Forgiven.mp3")
                                bgm = False
                            elif continuer == 11 : #changement de niveau
                                pygame.mixer.music.load("Evolving.mp3")
                                bgm = False

                        else:
                            player.pos.x -=1
                    else:            #le personnage est tourne vers la gauche
                        player.pos.x +=1

                else:       #deplacements
                    if event.key==K_RIGHT:
                        player.moveRight(5)
                        player.stateRight = True
                    elif event.key==K_LEFT:
                        player.moveLeft(5)
                        player.stateRight = False
                    elif event.key==K_UP:
                        player.saut()

        if player.velocite >=0 :
            player.upward = True
            player.downward = False #le personnage est en etat de saut
        else:
            player.downward = True
            player.upward = False


        if player.pos.y >224:
            if mode == "easy":
                player.pos.x = 2
                player.pos.y = currentMap.ycharSol
            if mode == "medium":
                if continuer <5:
                    continuer = 1
                    currentMap = listMaps[continuer-1] #changement de la carte en cours
                elif continuer <10:                     #indice-1 car une liste commence à [0] et pas a [1]
                    continuer = 6
                    currentMap = listMaps[continuer-1]
                else:
                    continuer =11
                    currentMap = listMaps[continuer-1]
                player.pos.x = 2
                player.pos.y = currentMap.ycharSol
            if mode == "hard":
                continuer = 1
                currentMap = listMaps[continuer-1]
                player.pos.x = 2
                player.pos.y = currentMap.ycharSol
            if mode =="insane":
                continuer = 1
                currentMap = listMaps[continuer-1]
                shuffle(background_list)
                player.pos.x = 2
                player.pos.y = currentMap.ycharSol


        if bgm == False :
            pygame.mixer.music.play(-1,0.0) #lancement(actualisation) de la musique
            bgm = True


        if mode !="insane":
            background = image(currentMap.background)
        else:   #gestion du fond (background) differente pour le mode insane (aleatoire)
            background = image(background_list[continuer])
        fenetre.blit(background, (0,0))
        player.rendu(gravite)
        pygame.display.flip()

        #nombre d'images/evenements par seconde
        clock.tick(60)



except :
    traceback.print_exc()

finally:
    pygame.quit()
    exit()
