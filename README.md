# Genetic-Algorithm

This repository contains an visual thing about genetic algorithmns, applying the concept of crossover and mutation in an spaceship


### How This Works

The game starts with n spaceships (Squares), and every spaceship has random genes, where genes like 0, means go forward, 1 means go backward, and so on for left, right and do nothing. The fitness metrics are the inverse of the euclidian distance between the center top of the spaceship and the center of the finish circle. After the time of 200 ticks, the system make a crossover between the best gene to all the other, followed by and mutation.


Here's gif of the beggining of the genetic algorithm:

![](teste2.gif)


And then, we can see how every spaceship evolved to the best gene, so everyone gets to the finish circle


![](teste.gif)


### Can i use this?

Of course, i authorize to download, distribute, modify and do everything you want, specially envolving the study of the genetic algorithm.


### How To Run

Simply download, stay clear that i used the python 3.7.6, and do

> pip install -r requirements.txt

and run

> python main.py 
