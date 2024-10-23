import pygame
from sys import exit

from model.factory import *
from model.circle import *
from model.sound import Sound
from model.square import *

from view.window import *



class Controller :
    
    def __init__(self) :
        
        #Pygame initilization
        pygame.init()
        pygame.mixer.init()
        
        #Game loop variable
        self.running = True
        
        #
        self.window = Window()
        self.circle = Circle(self.window)
        self.square = Square(self.window)
        self.factory = Factory()
    
    #main controller method
    def run(self) :
        
        pygame.display.set_caption(self.window.getTitle())
        # pygame.mixer.music.load("resources/sounds/map_music.wav")
        # pygame.mixer.music.play(-1)
        Sound.getAndPlaySound("resources/sounds/map_music.wav")
        buttons = self.factory.buttonFactory(self.window)
        
        #Game loop
        while self.running :
            
            self.eventHandler(buttons)
            
            if(self.window.getView() == "welcome") : 
                
                self.welcome(buttons)
            
            elif(self.window.getView() == "game") : 
                
                self.game(buttons)
                
            elif(self.window.getView() == "options") : 
                
                self.options(buttons)
            
        self.quit()
    
    def eventHandler(self, buttons) : 
        
        for event in pygame.event.get() :
            
            if event.type == pygame.QUIT :
                
                self.running = False
                
            for button in buttons :
                
                #Click event management 
                if(event.type == pygame.MOUSEBUTTONDOWN) :
                    
                    #Launch the game view.
                    if (button.checkPosition(pygame.mouse.get_pos()) and button.text_input == "Jouer") :
                        
                        self.window.setView("game")
                    
                    #Launch the options view.
                    if (button.checkPosition(pygame.mouse.get_pos()) and button.text_input == "Options") :
                        
                        self.window.setView("options")
                    
                    #Save the options(in the options view).
                    if (button.checkPosition(pygame.mouse.get_pos()) and button.text_input == "Enregistrer") :
                        
                        #action to save the options chose by the user (to define).
                        pass
                        
                    #Launch the options view.
                    if (button.checkPosition(pygame.mouse.get_pos()) and button.text_input == "Retour") :
                        
                        self.window.setView("welcome")
                        
                    #Close the window and quit the game
                    if (button.checkPosition(pygame.mouse.get_pos()) and button.text_input == "Quitter") :
                        
                        self.running == False
                        self.quit()
                        exit()
    
    def welcome(self, buttons) :
        
        self.window.welcomeView(buttons)
        pygame.display.flip()
        pygame.display.update()
    
    def game(self, buttons) :
        
        self.window.gameView(buttons)
        self.square.drawSprite()
        self.circle.drawSprite()
        self.square.move(self.window.dt)
        self.circle.move(self.window.dt)
        pygame.display.flip()
        pygame.display.update()
    
    def options(self, buttons) :
        
        self.window.optionsView(buttons)
        pygame.display.flip()
        pygame.display.update()
    
    def quit(self):
        
        pygame.quit()