import random
import math
import time as timer

import numpy as np
import pygame

img_nave = pygame.image.load("sq.png")
img_nave2 = pygame.image.load("sq2.png")
clock = pygame.time.Clock()
time = 30
width = 600
height = 600
pygame.font.init()
generation = 0
myfont = pygame.font.SysFont('Arial', 24)
myfont2 = pygame.font.SysFont('Arial', 12)
population = 500
lenGenes = 200
gra = [0]
button1 = pygame.Rect(650, 500, 30, 30)
button2 = pygame.Rect(650+40, 500, 30, 30)
button4 = pygame.Rect(650+80, 500, 30, 30)
button8 = pygame.Rect(650+120, 500, 30, 30)

nn = 0


class cromossomo:
    genes = None
    fit = None

    def __init__(self, gene, f):
        self.fit = f
        self.genes = gene


class navezinha:
    x = 140
    y = 550
    encostou = False
    genes = []
    fitness = 0
    imgs = img_nave
    imgs2 = img_nave2
    tempo = 0

    def __init__(self, gen):
        self.x = 140
        self.y = 550
        self.genes = gen
        self.fitness = 0
        self.vely = 0
        self.velx = 0
        self.img = self.imgs
        self.img2 = self.imgs2
        self.encosto = self.encostou
        self.tempo = 0

    def move(self, gene):
        if gene == 0:
            self.vely -= 1
        elif gene == 1:
            self.vely += 1
        elif gene == 2:
            self.velx -= 1
        elif gene == 3:
            self.velx += 1

    def draw(self, win, i):

        if(i <=20):
            win.blit(self.img2, (self.x, self.y))
        else:
            win.blit(self.img, (self.x, self.y))

    def runMove(self, start):
        if (self.x + self.imgs.get_width() >= 300 and self.x <= 330 and self.y >= 0 and self.y <= 20):
            final = int(round(timer.time() * 1000))
            delta = (final - max(start,0))/100
            print(delta)
            if(self.encosto == False):
                self.tempo = delta/10
                self.encosto = True

        elif(self.x+self.imgs.get_width()>=50 and self.x <=300 and self.y + self.imgs.get_width() >= 400 and self.y <= 420):
            pass
        elif (self.x + self.imgs.get_width() >= 200 and self.x <= 450 and self.y + self.imgs.get_width() >= 220 and self.y <= 220):
            pass
        elif (self.x + self.imgs.get_width() >= 0 and self.x <= 250 and self.y + self.imgs.get_width() >= 100 and self.y <= 120):
            pass
        elif (self.x + self.imgs.get_width() >= 350 and self.x <= 600 and self.y + self.imgs.get_width() >= 100 and self.y <= 120):
            pass
        else:
            self.x = self.x + self.velx
            if (self.x <= 1 and self.velx < 0): self.x = 2
            if (
                    self.x >= width - self.imgs.get_width() - 5 and self.velx > 0): self.x = width - self.img.get_width() - 8

            self.y = self.y + self.vely
            if (self.y <= 1 and self.vely < 0): self.y = 2
            if (
                    self.y >= width - self.imgs.get_width() - 5 and self.vely > 0): self.y = width - self.img.get_width() - 8


multi = 10


def draw_win(win, naves, gen, f, wf, mf, gra):
    aaa = nn

    win.fill((0, 0, 0))

    pygame.draw.rect(win, [255, 255, 255], button1)
    pygame.draw.rect(win, [255, 255, 255], button2)
    pygame.draw.rect(win, [255, 255, 255], button4)
    pygame.draw.rect(win, [255, 255, 255], button8)
    pygame.draw.rect(win, [255, 255, 255], pygame.Rect(50,400,250,20))
    pygame.draw.rect(win, [255, 255, 255], pygame.Rect(200, 200, 250, 20))
    pygame.draw.rect(win, [255, 255, 255], pygame.Rect(0, 100, 250, 20))
    pygame.draw.rect(win, [255, 255, 255], pygame.Rect(350, 100, 250, 20))

    pygame.draw.circle(win, (255, 255, 255), (300, 10), 10)
    pygame.draw.line(win, (255, 255, 255), (601, 0), (601, 600))
    pygame.draw.line(win, (255, 255, 255), (649, 399), (649, 300))
    pygame.draw.line(win, (255, 255, 255), (649, 399), (850, 399))
    n=0
    for nave in naves:
        n+=1
        nave.draw(win,n)
    textsurface = myfont.render('Generation: ' + str(gen), False, (255, 255, 255))
    win.blit(textsurface, (605, 0))
    textsurface = myfont.render('Best Fitness: ' + str(round(f * 100, 2)), False, (255, 255, 255))
    win.blit(textsurface, (605, 40))
    textsurface = myfont.render('Worst Fitness: ' + str(round(wf * 100, 2)), False, (255, 255, 255))
    win.blit(textsurface, (605, 80))

    textsurface = myfont.render('Fitness Mean: ' + str(round(mf * 100, 2)), False, (255, 255, 255))
    win.blit(textsurface, (605, 120))

    textsurface = myfont2.render('1x', False, (0, 0, 0))
    win.blit(textsurface, (657, 508))

    textsurface = myfont2.render('2x', False, (0, 0, 0))
    win.blit(textsurface, (697, 508))

    textsurface = myfont2.render('4x', False, (0, 0, 0))
    win.blit(textsurface, (737, 508))

    textsurface = myfont2.render('8x', False, (0, 0, 0))
    win.blit(textsurface, (777, 508))

    if (len(gra) >= 2 and len(gra) < 20):

        for i in range(len(gra) - 1):
            pygame.draw.line(win, (255, 255, 255), (650 + i * multi, 400 - int(gra[i] * 10)),
                             (650 + (i + 1) * multi, 400 - int(gra[i + 1] * 10)))
    elif len(gra)> 20:
        n = 0
        for i in range(len(gra) - 20,len(gra) - 1):

            pygame.draw.line(win, (255, 255, 255), (650 + (n*10) , 400 - int(gra[i] * 10)),
                             (650 +   ((n+1)*10), 400 - (int(gra[i + 1] *10))))
            n+=1
    pygame.display.update()


def main(bestNaves, gen, f, wf, mf, gra, start):
    pygame.init()
    global time
    screen = pygame.display.set_mode([width + 300, height])
    run = True
    naves = bestNaves
    ticks = 0

    cromossomos = []

    while run:
        clock.tick(time)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                run = False
            if event.type == pygame.KEYUP:
                pass
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = event.pos  # gets mouse position



                if button1.collidepoint(mouse_pos):
                    time = 30
                if button2.collidepoint(mouse_pos):
                    time = 60
                if button4.collidepoint(mouse_pos):
                    time = 120
                if button8.collidepoint(mouse_pos):
                    time = 960

        draw_win(screen, naves, gen, f, wf, mf, gra)
        for nave in naves:
            nave.move(nave.genes[ticks])
            nave.runMove(start)
        ticks += 1

        if (ticks == lenGenes):
            run = False

            for nave in naves:
                d = math.sqrt(((nave.x + nave.imgs.get_width() / 2 - (310)) ** 2 + (nave.y - 20) ** 2))
                if(nave.tempo != 0):
                    cromossomos.append(cromossomo(nave.genes, (1 / d )+ (1/(nave.tempo))*1))
                else:
                    cromossomos.append(cromossomo(nave.genes, (1 / d)))
    return cromossomos


def crossover(genes):
    TheBestGene = genes[0].genes
    a = False
    for i in range(1, len(genes)):
        if(genes[i].fit<8000000):
            a = True
            random.seed()
            partOneCross = random.randrange(0, len(genes[i].genes))
            partTwoCross = random.randrange(0, len(genes[i].genes))
            while partOneCross == partTwoCross:
                partOneCross = random.randrange(0, len(genes[i].genes))

            partOneBest = random.randrange(0, len(genes[0].genes) - abs(partOneCross - partTwoCross))
            partTwoBest = partOneBest + abs(partOneCross - partTwoCross)

            n = 0
            for z in range(min(partOneCross, partTwoCross), max(partOneCross, partTwoCross)):
                genes[i].genes[z] = TheBestGene[min(partOneCross, partTwoCross) + n]
                n += 1
    return genes


def mutate(genes):

    for i in range(len(genes)-10, len(genes)):
        for j in range(len(genes[i].genes)):
            random.seed()
            aux = random.randrange(0, 100)
            prob = (aux*100)/random.randrange(max(aux,1), 100+1)
            if (prob >= 0 and prob <= 40 and genes[i].fit <= 0.25):
                aux = random.randrange(0, 5)
                while aux == genes[i].genes[j]:
                    aux = random.randrange(0, 5)
                genes[i].genes[j] = aux
    return genes


def genetic():
    gen = 0
    random.seed()
    bestNaves = []

    for i in range(population):
        genes = []
        for j in range(lenGenes):
            genes.append(random.randrange(0, 5))
        bestNaves.append(navezinha(genes))
    start = int(round(timer.time() * 1000))
    Cromossomos = (sorted(main(bestNaves, gen, 0, 0, 0, [],start), key=lambda x: x.fit, reverse=True))
    aux_fit = 0

    run = True
    while run:
        start = int(round(timer.time() * 1000))
        gen += 1
        naves = []
        child = crossover(Cromossomos)


        if (child[0].fit > aux_fit):
            aux_fit = child[0].fit
        gra.append(aux_fit)
        mf = 0
        for z in range(len(child)):
            mf += child[z].fit / len(child)

        for w in range(len(child)):
            naves.append(navezinha(child[w].genes))
        Cromossomos = (sorted(main(naves, gen, aux_fit, child[-1].fit, mf, gra, start), key=lambda x: x.fit, reverse=True))


genetic()
