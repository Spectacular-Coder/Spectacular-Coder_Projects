import pgzrun
import random
import pygame

bomb2 = Actor ("bomb")
bomb1 = Actor ("bomb")
fruit5 = Actor ("apple")
fruit4 = Actor("orange1")
fruit3 = Actor("kiwi1")    
fruit2 = Actor("orange")    
fruit = Actor("mango")
variable_score = 0 

       

   
def draw():
    screen.clear()
    screen.blit('fruit ninga bg',(0, 0))
    screen.draw.text("Score: "+ str(variable_score ), topleft =(10, 10))
    fruit.draw()
    fruit2.draw()
    fruit3.draw()
    fruit4.draw()
    fruit5.draw()
    bomb1.draw()
    bomb2.draw()
    
    

def place_fruit():
    fruit.x = random.randint(30, 770)
    fruit.y = (10)
    
def place_fruit2():
    fruit2.x = random.randint(30, 770)
    fruit2.y = (10)

def place_fruit3():
    fruit3.x = random.randint(30, 770)
    fruit3.y = (10)

def place_fruit4():
    fruit4.x = random.randint(30, 770)
    fruit4.y = (10)

    
def place_fruit5():
    fruit5.x = random.randint(30, 770)
    fruit5.y = (10)

def place_bomb1():
    bomb1.x = random.randint(30, 770)
    bomb1.y = (10)

def place_bomb2():
    bomb2.x = random.randint(30, 770)
    bomb2.y = (10)
        
def on_mouse_down(pos) :
   
    
    global variable_score
    if fruit.collidepoint(pos):
       variable_score = variable_score + 1
       print("Good shot")
       place_fruit()
   
       
    if fruit2.collidepoint(pos):
       variable_score = variable_score + 1
       print("Good shot")
       place_fruit2()

    if fruit3.collidepoint(pos):
       variable_score = variable_score + 1
       print("Good shot")
       place_fruit3()

    if fruit4.collidepoint(pos):
       variable_score = variable_score + 1
       print("Good shot")
       place_fruit4()

    if fruit5.collidepoint(pos):
       variable_score = variable_score + 1
       print("Good shot")
       place_fruit5()
       
    if bomb1.collidepoint(pos) :
       variable_score = variable_score - 1
       print("*explodes*")
       place_bomb1()
    if bomb2.collidepoint(pos) :
       variable_score = variable_score - 1
       print("*explodes*")
       place_bomb2()
    else:
        print("You missed!")
    print(variable_score) 

def update():
    fruit.y = fruit.y + 1
    fruit2.y = fruit2.y + 2
    fruit3.y = fruit3.y + 2
    fruit4.y = fruit4.y + 2
    fruit5.y = fruit5.y + 3
    bomb1.y = bomb1.y + 2
    bomb2.y = bomb1.y + 2

place_fruit()


pgzrun.go()
