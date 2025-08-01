import pygame as pg
from sys import exit
import random
import math
pg.init()
width=600
height=600
screen=pg.display.set_mode((width,height))
pg.display.set_caption('GAME NAME')
clock=pg.time.Clock()
objs=[]
max_dist=200
class obj:
    def __init__(self,xpos,ypos):
        self.clr=(200,0,0)
        self.len=20
        self.height=50
        self.xpos=xpos
        self.ypos=ypos
        self.vel=2
        objs.append(self)
    def draw(self,screen):
        pg.draw.rect(screen,self.clr,(self.xpos,self.ypos,self.len,self.height))
    def update(self):
        self.ypos+=self.vel
        if(self.ypos>height):
            objs.remove(self)
            
            
class Car:
    def __init__(self):
        self.clr=(255,255,255)
        self.xpos=width/2
        self.ypos=height/2
        self.velx=0
        self.len=20
        self.height=50
        self.mid_y=self.ypos+int(self.height/2)
        self.mid_x=self.xpos+int(self.len/2)
        self.dist_left=max_dist
        self.dist_right=max_dist
        self.right_dia_dist=max_dist
        self.left_dia_dist=max_dist
        self.left_line_clr=(0,255,0)
        self.right_line_clr=(0,255,0)
        self.ld_line_clr=(0,255,0)
        self.rd_line_clr=(0,255,0)
        
    def upadte(self):
        ##left check
        updated_left=False
        for object in objs:
            if(object.ypos<self.mid_y<object.ypos+object.height and object.xpos+object.len<self.xpos):
                self.dist_left=self.xpos-object.xpos-object.len
                updated_left=True
        if not updated_left:
            self.dist_left=max_dist
        ##

        ##right check
        updated_r=False
        for object in objs:
            if(object.ypos<self.mid_y<object.ypos+object.height and object.xpos>self.xpos+self.len):
                self.dist_right=object.xpos-self.xpos-self.len
                updated_r=True
        if not updated_r:
            self.dist_right=max_dist
        ##
        
        ## right dia
        updated_rd=False
        for object in objs:
            #line eqn->  y=x+(width-b-a)
            right_dia_intersecpt=self.mid_x+self.mid_y-object.xpos
            if(object.ypos<right_dia_intersecpt<object.ypos+object.height and object.xpos>self.xpos):
                self.right_dia_dist=math.hypot(abs(self.mid_x-object.xpos),abs(self.mid_y-right_dia_intersecpt))
                updated_rd=True
        if not updated_rd:
            self.right_dia_dist=max_dist
        ##
        
        ##
        updated_ld=False
        for object in objs:
            #line eqn-> y=-x+(width-b+a)
            left_dia_intersept=object.xpos+self.mid_y-self.mid_x
            if(object.ypos<left_dia_intersept<object.ypos+object.height and object.xpos<self.xpos):
                self.left_dia_dist=math.hypot(abs(self.mid_x-object.xpos),abs(self.mid_y-left_dia_intersept))
                updated_ld=True
        if not updated_ld:
            self.left_dia_dist=max_dist        
        
        #########
        
        ##left check
        if(self.dist_left>100):
            self.left_line_clr=(0,255,0)
        elif(50<self.dist_left<100):
            self.velx+=0.5
            self.left_line_clr=(255,255,0)
        elif(self.dist_left<50):
            self.velx+=1
            self.left_line_clr=(255,0,0)
        ##
        
        ## right dia check
        if(self.right_dia_dist>100):
            self.rd_line_clr=(0,255,0)
        elif(50<self.right_dia_dist<100):
            self.velx+=-0.5
            self.rd_line_clr=(255,255,0)
        elif(self.right_dia_dist<50):
            self.velx+=-1
            self.rd_line_clr=(255,0,0)
        ##
        
        ## left dia check
        if(self.left_dia_dist>100):
            self.ld_line_clr=(0,255,0)
        elif(50<self.left_dia_dist<100):
            self.velx+=0.5
            self.ld_line_clr=(255,255,0)
        elif(self.left_dia_dist<50):
            self.velx+=1
            self.ld_line_clr=(255,0,0)
        ##
        
        ##right check
        if(self.dist_right>100):
            self.right_line_clr=(0,255,0)
        elif(50<self.dist_right<100):
            self.velx+=-0.5
            self.right_line_clr=(255,255,0)
        elif(self.dist_right<50):
            self.velx+=-1
            self.right_line_clr=(255,0,0)
        ##
        self.xpos+=self.velx
        self.mid_y=self.ypos+int(self.height/2)
        self.mid_x=self.xpos+int(self.len/2)
        self.velx=0
    def draw(self,screen):
        pg.draw.rect(screen,self.clr,(self.xpos,self.ypos,self.len,self.height))
        pg.draw.line(screen,self.left_line_clr,(self.xpos,self.mid_y),(self.xpos-self.dist_left,self.mid_y))#left line
        pg.draw.line(screen,self.right_line_clr,(self.xpos+self.len,self.mid_y),(self.xpos+self.len+self.dist_right,self.mid_y))#right line
        pg.draw.line(screen,self.rd_line_clr,(self.mid_x,self.mid_y),(self.mid_x+self.right_dia_dist*math.sin(math.radians(45)),self.mid_y-self.right_dia_dist*math.cos(math.radians(45))))#rd line
        pg.draw.line(screen,self.ld_line_clr,(self.mid_x,self.mid_y),(self.mid_x-self.left_dia_dist*math.sin(math.radians(45)),self.mid_y-self.left_dia_dist*math.cos(math.radians(45))))#ld line
car=Car()

while(True):
    screen.fill((0,0,0))
    x,y=pg.mouse.get_pos()
    for event in pg.event.get():
        if(event.type == pg.MOUSEBUTTONDOWN):
            obj_=obj(x,y)
        if(event.type == pg.QUIT):
            print(objs)
            pg.quit()
            exit()
            
    for object in objs:
        object.update()
        object.draw(screen)
    car.upadte()
    car.draw(screen)
    
    pg.display.update()
    clock.tick(60)#NOT TO RUN FASTER THEN 60 FPS